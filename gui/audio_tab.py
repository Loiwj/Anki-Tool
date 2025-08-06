import tkinter as tk
from tkinter import ttk
from .shared_widgets import create_log_area, create_progress_bar
from .language_manager import lang_manager

def create_audio_tab(main_app, parent_tab):
    """Tạo giao diện cho tab Tạo Audio."""
    
    config_frame = ttk.LabelFrame(parent_tab, text=lang_manager.get("configuration", "Configuration"), padding="10")
    config_frame.pack(fill="x", padx=10, pady=5)
    
    ttk.Label(config_frame, text=lang_manager.get("deck_name_optional", "Deck Name (leave empty to scan all):")).pack(anchor="w")
    deck_entry = ttk.Entry(config_frame, textvariable=main_app.deck_name_var)
    deck_entry.pack(fill="x", pady=5)
    
    fields_frame = ttk.Frame(config_frame)
    fields_frame.pack(fill="x", pady=5)
    
    ttk.Label(fields_frame, text=lang_manager.get("source_field")).grid(row=0, column=0, sticky="w", padx=(0, 10))
    ttk.Entry(fields_frame, textvariable=main_app.source_field_var, width=15).grid(row=0, column=1, sticky="w", padx=(0, 20))
    
    ttk.Label(fields_frame, text=lang_manager.get("audio_field")).grid(row=0, column=2, sticky="w", padx=(0, 10))
    ttk.Entry(fields_frame, textvariable=main_app.audio_field_var, width=15).grid(row=0, column=3, sticky="w")
    
    audio_settings_frame = ttk.LabelFrame(parent_tab, text=lang_manager.get("audio_settings", "Audio Settings"), padding="10")
    audio_settings_frame.pack(fill="x", padx=10, pady=5)
    
    settings_row1 = ttk.Frame(audio_settings_frame)
    settings_row1.pack(fill="x", pady=2)
    
    ttk.Label(settings_row1, text=lang_manager.get("audio_speed")).pack(side="left")
    ttk.Combobox(settings_row1, textvariable=main_app.audio_speed_var, values=["0.5", "0.7", "0.8", "1.0", "1.2"], width=8, state="readonly").pack(side="left", padx=(10, 0))
    
    # Dòng code đã được sửa từ ttk.BooleanVar thành tk.BooleanVar
    main_app.overwrite_audio_var = tk.BooleanVar(value=False)
    ttk.Checkbutton(audio_settings_frame, text=lang_manager.get("overwrite_audio", "Overwrite existing audio"), variable=main_app.overwrite_audio_var).pack(anchor="w", pady=5)
    
    # Progress and Log
    p_frame, main_app.audio_progress_bar, main_app.audio_progress_var = create_progress_bar(parent_tab)
    p_frame.pack(fill="x", padx=10, pady=5)
    
    log_frame, main_app.audio_log_text = create_log_area(parent_tab)
    log_frame.pack(fill="both", expand=True, padx=10, pady=5)
    
    # Buttons
    buttons_frame = ttk.Frame(parent_tab)
    buttons_frame.pack(fill="x", padx=10, pady=10, side="bottom")
    
    main_app.audio_scan_button = ttk.Button(buttons_frame, text="Quét từ thiếu Audio", command=main_app.scan_missing_audio)
    main_app.audio_scan_button.pack(side="left")
    
    main_app.audio_generate_button = ttk.Button(buttons_frame, text="Bắt đầu tạo Audio", command=main_app.start_audio_generation, state="disabled")
    main_app.audio_generate_button.pack(side="left", padx=(10, 0))
    
    main_app.audio_stop_button = ttk.Button(buttons_frame, text="Dừng", command=main_app.stop_processing, state="disabled")
    main_app.audio_stop_button.pack(side="left", padx=(10, 0))