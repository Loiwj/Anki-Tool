import tkinter as tk
from tkinter import ttk, messagebox
import threading
from queue import Queue
import time
import os

from services.anki_connect import AnkiConnect
from services.gemini_client import GeminiClient
from services.google_tts import generate_audio, sanitize_filename
from .phonetic_tab import create_phonetic_tab
from .audio_tab import create_audio_tab

class MainWindow:
    def __init__(self, root, api_keys_str):
        self.root = root
        self.root.title("Công cụ Anki đa ngôn ngữ by Dương Quốc Lợi")
        
        # Khởi tạo clients
        self.anki_client = AnkiConnect()
        self.gemini_client = GeminiClient(api_keys_str)
        
        # Biến trạng thái và Queue
        self._is_running = False
        self._stop_flag = False
        self.queue = Queue()
        
        # Biến giao diện (StringVar, BooleanVar, etc.)
        self.language_var = tk.StringVar(value="Tiếng Hàn")
        self.deck_name_var = tk.StringVar(value="Tiếng Hàn Tổng Hợp SC1")
        self.source_field_var = tk.StringVar(value="Korean")
        self.target_field_var = tk.StringVar(value="Phonetic")
        self.audio_field_var = tk.StringVar(value="Audio")
        self.audio_speed_var = tk.StringVar(value="0.8")
        
        self.create_widgets()
        self.root.after(100, self.process_queue)

    def create_widgets(self):
        # Menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Trợ giúp", menu=help_menu)
        help_menu.add_command(label="Kiểm tra kết nối Anki", command=self.test_anki_connection)

        # Khung chọn ngôn ngữ
        lang_frame = ttk.Frame(self.root, padding=(10, 10, 10, 0))
        lang_frame.pack(fill="x")
        ttk.Label(lang_frame, text="Chọn ngôn ngữ:", font=('Helvetica', 10, 'bold')).pack(side="left", padx=(0, 10))
        lang_combo = ttk.Combobox(lang_frame, textvariable=self.language_var, values=["Tiếng Hàn", "Tiếng Nhật"], state="readonly", width=15)
        lang_combo.pack(side="left")
        lang_combo.bind("<<ComboboxSelected>>", self.on_language_change)
        
        # Notebook (Tabs)
        notebook = ttk.Notebook(self.root, style="TNotebook")
        notebook.pack(expand=True, fill="both", padx=10, pady=10)
        
        phonetic_tab = ttk.Frame(notebook, padding="10")
        audio_tab = ttk.Frame(notebook, padding="10")
        
        notebook.add(phonetic_tab, text="Tạo Phiên Âm")
        notebook.add(audio_tab, text="Tạo Audio")
        
        # Tạo nội dung cho các tab
        create_phonetic_tab(self, phonetic_tab)
        create_audio_tab(self, audio_tab)

    def on_language_change(self, event=None):
        lang = self.language_var.get()
        if lang == "Tiếng Nhật":
            self.source_field_var.set("Expression")
            self.target_field_var.set("Reading")
        else: # Tiếng Hàn
            self.source_field_var.set("Korean")
            self.target_field_var.set("Phonetic")
        self.log_message(f"Đã chuyển sang chế độ {lang}.")

    def test_anki_connection(self):
        try:
            version = self.anki_client.invoke('version')
            messagebox.showinfo("Thành công", f"Kết nối Anki thành công! Phiên bản AnkiConnect: {version}")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def log_message(self, message, target_log=None):
        log_widget = target_log if target_log else self.log_text
        current_time = time.strftime('%H:%M:%S')
        log_widget.config(state='normal')
        log_widget.insert(tk.END, f"{current_time} - {message}\n")
        log_widget.see(tk.END)
        log_widget.config(state='disabled')
        self.root.update_idletasks()

    def process_queue(self):
        try:
            while not self.queue.empty():
                msg_type, data = self.queue.get_nowait()
                # Xử lý các thông điệp cập nhật UI từ queue
                if msg_type == "log":
                    self.log_message(data['message'], data.get('log_widget'))
                elif msg_type == "progress_max":
                    data['bar'].config(maximum=data['value'])
                    data['var'].set(f"0/{data['value']}")
                elif msg_type == "progress_update":
                    data['bar'].config(value=data['value'])
                    max_val = data['bar'].cget("maximum")
                    data['var'].set(f"{data['value']}/{int(max_val)}")
                elif msg_type == "phonetic_add_item":
                    self.phonetic_tree.insert("", "end", values=data, iid=str(data[0]))
                elif msg_type == "phonetic_update_item":
                    self.phonetic_tree.item(str(data[0]), values=data)
                elif msg_type == "set_state":
                    for widget, state in data.items():
                        widget.config(state=state)
                elif msg_type == "finish":
                    self._is_running = False
                    self.log_message("Hoàn tất!", data.get('log_widget'))
                    
        finally:
            self.root.after(100, self.process_queue)

    def stop_processing(self):
        if self._is_running:
            self._stop_flag = True
            self.log_message("Đang yêu cầu dừng...")

    # --- Logic cho Tab Tạo Phiên Âm ---
    def start_phonetic_processing(self):
        if self._is_running: return
        self._is_running = True
        self._stop_flag = False
        
        for item in self.phonetic_tree.get_children(): self.phonetic_tree.delete(item)

        self.queue.put(("set_state", {
            self.phonetic_start_button: "disabled",
            self.phonetic_stop_button: "normal"
        }))
        
        thread = threading.Thread(target=self._phonetic_worker, daemon=True)
        thread.start()

    def _phonetic_worker(self):
        try:
            deck = self.deck_name_var.get().strip()
            source = self.source_field_var.get().strip()
            target = self.target_field_var.get().strip()
            if not all([deck, source, target]):
                raise ValueError("Vui lòng điền đầy đủ thông tin Deck và các trường.")

            query = f'deck:"{deck}" "{target}":'
            note_ids = self.anki_client.invoke('findNotes', query=query)
            if not note_ids:
                self.queue.put(("log", {'message': "Không tìm thấy thẻ nào cần xử lý.", 'log_widget': self.log_text}))
                return

            self.queue.put(("log", {'message': f"Tìm thấy {len(note_ids)} thẻ.", 'log_widget': self.log_text}))
            self.queue.put(("progress_max", {'bar': self.phonetic_progress_bar, 'var': self.phonetic_progress_var, 'value': len(note_ids)}))

            notes_info = self.anki_client.invoke('notesInfo', notes=note_ids)
            for i, note in enumerate(notes_info):
                if self._stop_flag: break
                
                vocab = note['fields'].get(source, {}).get('value', '').strip()
                if not vocab: continue
                
                self.queue.put(("phonetic_add_item", (i + 1, vocab, "", "Đang chờ...")))
                phonetic, error = self.gemini_client.get_phonetic(vocab, self.language_var.get())
                
                if self._stop_flag: break

                if phonetic:
                    self.anki_client.invoke('updateNoteFields', note={"id": note['noteId'], "fields": {target: phonetic}})
                    self.queue.put(("phonetic_update_item", (i + 1, vocab, phonetic, "Thành công")))
                else:
                    self.queue.put(("phonetic_update_item", (i + 1, vocab, "", f"Lỗi: {error}")))
                
                self.queue.put(("progress_update", {'bar': self.phonetic_progress_bar, 'var': self.phonetic_progress_var, 'value': i + 1}))
                time.sleep(1.5)

        except Exception as e:
            self.queue.put(("log", {'message': f"Lỗi nghiêm trọng: {e}", 'log_widget': self.log_text}))
        finally:
            self.queue.put(("set_state", {
                self.phonetic_start_button: "normal",
                self.phonetic_stop_button: "disabled"
            }))
            self.queue.put(("finish", {'log_widget': self.log_text}))
            self._is_running = False

    # --- Logic cho Tab Tạo Audio ---
    def scan_missing_audio(self):
        if self._is_running: return
        self.audio_log_text.config(state='normal')
        self.audio_log_text.delete(1.0, tk.END)
        self.audio_log_text.config(state='disabled')

        self.audio_missing_notes = []
        try:
            deck = self.deck_name_var.get().strip()
            source = self.source_field_var.get().strip()
            audio_field = self.audio_field_var.get().strip()
            
            query = f'deck:"{deck}"' if deck else ""
            note_ids = self.anki_client.invoke('findNotes', query=query)
            if not note_ids:
                self.log_message("Không tìm thấy note nào.", self.audio_log_text)
                return
            
            notes_info = self.anki_client.invoke('notesInfo', notes=note_ids)
            for note in notes_info:
                vocab = note['fields'].get(source, {}).get('value', '').strip()
                audio = note['fields'].get(audio_field, {}).get('value', '').strip()
                if vocab and (not audio or self.overwrite_audio_var.get()):
                    self.audio_missing_notes.append({'note_id': note['noteId'], 'vocab': vocab})
            
            if self.audio_missing_notes:
                self.log_message(f"Tìm thấy {len(self.audio_missing_notes)} từ cần tạo audio.", self.audio_log_text)
                self.audio_generate_button.config(state="normal")
            else:
                self.log_message("Tất cả các từ đã có audio!", self.audio_log_text)
        except Exception as e:
            self.log_message(f"Lỗi khi quét: {e}", self.audio_log_text)

    def start_audio_generation(self):
        if self._is_running or not hasattr(self, 'audio_missing_notes') or not self.audio_missing_notes: return
        self._is_running = True
        self._stop_flag = False
        
        self.queue.put(("set_state", {
            self.audio_scan_button: "disabled",
            self.audio_generate_button: "disabled",
            self.audio_stop_button: "normal"
        }))
        
        thread = threading.Thread(target=self._audio_worker, daemon=True)
        thread.start()

    def _audio_worker(self):
        try:
            media_path = self.anki_client.get_anki_media_path()
            if not media_path: raise ValueError("Không lấy được đường dẫn thư mục media của Anki.")
            
            lang_map = {"Tiếng Hàn": "ko", "Tiếng Nhật": "ja"}
            lang_code = lang_map.get(self.language_var.get(), "ko")
            audio_field = self.audio_field_var.get().strip()
            speed = float(self.audio_speed_var.get())
            total = len(self.audio_missing_notes)
            
            self.queue.put(("progress_max", {'bar': self.audio_progress_bar, 'var': self.audio_progress_var, 'value': total}))
            
            for i, note_info in enumerate(self.audio_missing_notes):
                if self._stop_flag: break
                
                vocab = note_info['vocab']
                self.queue.put(("progress_update", {'bar': self.audio_progress_bar, 'var': self.audio_progress_var, 'value': i + 1}))
                
                audio_data = generate_audio(vocab, lang_code, speed)
                if audio_data:
                    filename = f"auto_{lang_code}_{sanitize_filename(vocab)}_{int(time.time())}.mp3"
                    filepath = os.path.join(media_path, filename)
                    with open(filepath, 'wb') as f: f.write(audio_data)
                    
                    self.anki_client.invoke('updateNoteFields', note={"id": note_info['note_id'], "fields": {audio_field: f"[sound:{filename}]"}})
                    self.queue.put(("log", {'message': f"✅ Đã tạo audio: {vocab}", 'log_widget': self.audio_log_text}))
                else:
                    self.queue.put(("log", {'message': f"❌ Lỗi audio: {vocab}", 'log_widget': self.audio_log_text}))
                time.sleep(1)

        except Exception as e:
            self.queue.put(("log", {'message': f"Lỗi nghiêm trọng: {e}", 'log_widget': self.audio_log_text}))
        finally:
            self.queue.put(("set_state", {
                self.audio_scan_button: "normal",
                self.audio_generate_button: "normal",
                self.audio_stop_button: "disabled"
            }))
            self.queue.put(("finish", {'log_widget': self.audio_log_text}))
            self._is_running = False