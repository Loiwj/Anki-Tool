import os
from dotenv import load_dotenv
from ttkthemes import ThemedTk
import tkinter as tk
from gui.main_window import MainWindow

def main():
    # Tải biến môi trường từ file .env
    load_dotenv()
    api_keys_str = os.getenv("GEMINI_API_KEYS")
    
    if not api_keys_str:
        print("LỖI: Không tìm thấy biến GEMINI_API_KEYS trong file .env.")
        print("Vui lòng tạo file .env và thêm vào dòng: GEMINI_API_KEYS=\"key1,key2,...\"")
        return

    # Khởi tạo giao diện
    try:
        root = ThemedTk(theme="arc")
    except tk.TclError:
        root = tk.Tk()
        
    app = MainWindow(root, api_keys_str)
    root.mainloop()

if __name__ == "__main__":
    main()