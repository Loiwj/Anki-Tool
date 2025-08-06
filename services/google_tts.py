import requests

def generate_audio(text, language_code, speed=0.8):
    """Tạo audio từ Google Translate TTS."""
    try:
        params = {'ie': 'UTF-8', 'q': text, 'tl': language_code, 'client': 'tw-ob', 'ttsspeed': speed}
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get("https://translate.google.com/translate_tts", params=params, headers=headers, timeout=15)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"Lỗi tạo audio cho '{text}': {e}")
        return None

def sanitize_filename(filename):
    """Làm sạch tên file để tránh các ký tự không hợp lệ."""
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-. '
    return "".join(c for c in filename if c in allowed_chars).rstrip()[:50]