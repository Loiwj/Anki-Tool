import google.generativeai as genai

class GeminiClient:
    """Quản lý việc gọi API của Gemini và xử lý key."""
    
    def __init__(self, api_keys_str):
        self.api_keys = [key.strip() for key in api_keys_str.split(',') if key.strip()]
        if not self.api_keys:
            raise ValueError("Không tìm thấy API key của Gemini trong file .env hoặc key không hợp lệ.")
        self.current_api_key_index = 0

    def _get_next_key(self):
        self.current_api_key_index = (self.current_api_key_index + 1) % len(self.api_keys)
        return self.api_keys[self.current_api_key_index]

    def get_phonetic(self, text_to_convert, language):
        if not self.api_keys:
            return None, "Không có API key"

        initial_key_index = self.current_api_key_index
        
        while True:
            try:
                current_key = self.api_keys[self.current_api_key_index]
                genai.configure(api_key=current_key)
                model = genai.GenerativeModel('gemini-1.5-flash-latest')

                if language == "Tiếng Hàn":
                    prompt = f"Chuyển từ tiếng Hàn sau thành phiên âm tiếng Việt, dùng dấu gạch ngang nối âm tiết (ví dụ: 안녕하세요 -> an-nyông-ha-sê-yo). Chỉ trả về phiên âm. Từ: \"{text_to_convert}\""
                elif language == "Tiếng Nhật":
                    prompt = f"Chuyển cụm từ tiếng Nhật sau thành Romaji (ví dụ: 今日は -> kyō wa). Chỉ trả về Romaji. Cụm từ: \"{text_to_convert}\""
                else:
                    return None, f"Ngôn ngữ '{language}' không được hỗ trợ."

                response = model.generate_content(prompt)
                return response.text.strip(), None

            except Exception as e:
                error_str = str(e).lower()
                if "api key not valid" in error_str or ("429" in error_str and "quota" in error_str):
                    self.current_api_key_index = (self.current_api_key_index + 1) % len(self.api_keys)
                    if self.current_api_key_index == initial_key_index:
                        return None, "Tất cả API key đều đã hết hạn ngạch hoặc không hợp lệ."
                else:
                    return None, f"Lỗi không xác định từ Gemini: {e}"