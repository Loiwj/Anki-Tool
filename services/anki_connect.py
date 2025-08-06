import requests
import os

class AnkiConnect:
    """Quản lý tất cả các tương tác với AnkiConnect."""
    
    def invoke(self, action, **params):
        payload = {"action": action, "version": 6, "params": params}
        try:
            response = requests.post('http://localhost:8765', json=payload, timeout=10)
            response.raise_for_status()
            result = response.json()
            if error := result.get('error'):
                raise Exception(f"Lỗi từ Anki: {error}")
            return result.get('result')
        except requests.exceptions.RequestException as e:
            raise Exception(f"Lỗi kết nối AnkiConnect. Bạn đã mở Anki chưa?\n{e}")

    def get_anki_media_path(self):
        try:
            return self.invoke('getMediaDirPath')
        except Exception as e:
            print(f"Không thể lấy đường dẫn media từ AnkiConnect: {e}")
            return None