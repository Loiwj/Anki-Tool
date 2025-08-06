import tkinter as tk
from tkinter import ttk, scrolledtext

def create_log_area(parent, title="Nhật ký"):
    """Tạo một khu vực log có thể cuộn."""
    log_frame = ttk.LabelFrame(parent, text=title, padding="10")
    log_text = scrolledtext.ScrolledText(log_frame, height=8, wrap=tk.WORD)
    log_text.pack(fill="both", expand=True)
    log_text.config(state='disabled') # Chỉ đọc
    return log_frame, log_text

def create_progress_bar(parent, title="Tiến độ"):
    """Tạo một thanh tiến trình với nhãn."""
    progress_frame = ttk.LabelFrame(parent, text=title, padding="10")
    progress_var = tk.StringVar(value="Sẵn sàng")
    
    ttk.Label(progress_frame, textvariable=progress_var).pack(anchor="w")
    progress_bar = ttk.Progressbar(progress_frame, length=400, mode='determinate')
    progress_bar.pack(fill="x", pady=5)

    return progress_frame, progress_bar, progress_var