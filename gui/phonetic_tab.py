import tkinter as tk
from tkinter import ttk
from .shared_widgets import create_log_area, create_progress_bar

def create_phonetic_tab(main_app, parent_tab):
    """Tạo giao diện cho tab Tạo Phiên Âm."""
    
    # Khung cấu hình
    config_frame = ttk.LabelFrame(parent_tab, text="Cấu hình", padding="10")
    config_frame.pack(fill="x", padx=10, pady=5)

    anki_frame = ttk.Frame(config_frame)
    anki_frame.pack(fill="x", pady=5)
    
    ttk.Label(anki_frame, text="Tên bộ thẻ (Deck):").grid(row=0, column=0, sticky="w", padx=(0, 10))
    deck_name_entry = ttk.Entry(anki_frame, textvariable=main_app.deck_name_var, width=30)
    deck_name_entry.grid(row=0, column=1, sticky="w", padx=(0, 20))
    
    ttk.Label(anki_frame, text="Trường nguồn (Từ vựng):").grid(row=0, column=2, sticky="w", padx=(0, 10))
    source_field_entry = ttk.Entry(anki_frame, textvariable=main_app.source_field_var, width=15)
    source_field_entry.grid(row=0, column=3, sticky="w")
    
    ttk.Label(anki_frame, text="Trường đích (Phiên âm):").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(5, 0))
    target_field_entry = ttk.Entry(anki_frame, textvariable=main_app.target_field_var, width=30)
    target_field_entry.grid(row=1, column=1, sticky="w", pady=(5,0))

    # Khung điều khiển
    control_frame = ttk.Frame(parent_tab)
    control_frame.pack(fill="x", padx=10, pady=10)
    
    main_app.phonetic_start_button = ttk.Button(control_frame, text="Bắt đầu tạo phiên âm", command=main_app.start_phonetic_processing)
    main_app.phonetic_start_button.pack(side="left", padx=(0, 10))
    
    main_app.phonetic_stop_button = ttk.Button(control_frame, text="Dừng", command=main_app.stop_processing, state="disabled")
    main_app.phonetic_stop_button.pack(side="left")

    # Thanh tiến độ
    p_frame, main_app.phonetic_progress_bar, main_app.phonetic_progress_var = create_progress_bar(parent_tab)
    p_frame.pack(fill="x", padx=10, pady=5)
    
    # Khung kết quả và log
    results_container = ttk.Frame(parent_tab)
    results_container.pack(fill="both", expand=True, padx=10, pady=5)
    results_container.columnconfigure(0, weight=2)
    results_container.columnconfigure(1, weight=1)

    # Treeview hiển thị các từ đang xử lý
    word_list_frame = ttk.LabelFrame(results_container, text="Danh sách từ đang xử lý", padding="10")
    word_list_frame.grid(row=0, column=0, sticky="nsew", rowspan=2)

    columns = ("STT", "Từ vựng", "Phiên âm", "Trạng thái")
    main_app.phonetic_tree = ttk.Treeview(word_list_frame, columns=columns, show="headings", height=10)
    main_app.phonetic_tree.heading("STT", text="STT")
    main_app.phonetic_tree.heading("Từ vựng", text="Từ vựng")
    main_app.phonetic_tree.heading("Phiên âm", text="Phiên âm")
    main_app.phonetic_tree.heading("Trạng thái", text="Trạng thái")
    for col in columns: main_app.phonetic_tree.column(col, width=100)
    
    tree_scroll = ttk.Scrollbar(word_list_frame, orient="vertical", command=main_app.phonetic_tree.yview)
    main_app.phonetic_tree.configure(yscroll=tree_scroll.set)
    main_app.phonetic_tree.pack(side="left", fill="both", expand=True)
    tree_scroll.pack(side="right", fill="y")
    
    # Log area
    log_frame, main_app.log_text = create_log_area(results_container)
    log_frame.grid(row=0, column=1, sticky="nsew", padx=(10,0))