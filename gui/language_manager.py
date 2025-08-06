# Language Manager for AnkiTool
# Quản lý đa ngôn ngữ cho AnkiTool

import json
import os

class LanguageManager:
    def __init__(self):
        self.current_ui_language = "vi"  # Default to Vietnamese
        self.translations = {
            "vi": {
                # Main Window
                "app_title": "Công cụ Anki đa ngôn ngữ by Dương Quốc Lợi",
                "help_menu": "Trợ giúp",
                "test_anki_connection": "Kiểm tra kết nối Anki",
                "select_language": "Chọn ngôn ngữ:",
                "select_ui_language": "Giao diện:",
                "select_processing_language": "Xử lý:",
                
                # Tabs
                "phonetic_tab": "Tạo Phiên Âm",
                "audio_tab": "Tạo Audio",
                "ai_cards_tab": "Tạo Thẻ AI",
                
                # Phonetic Tab
                "input_text": "Nhập văn bản:",
                "deck_name": "Tên Deck:",
                "source_field": "Trường nguồn:",
                "target_field": "Trường đích:",
                "create_cards": "Tạo thẻ",
                "stop": "Dừng",
                
                # Audio Tab
                "audio_field": "Trường Audio:",
                "audio_speed": "Tốc độ:",
                "voice_selection": "Chọn giọng:",
                "create_audio": "Tạo Audio",
                
                # Language options
                "korean": "Tiếng Hàn",
                "japanese": "Tiếng Nhật",
                "vietnamese": "Tiếng Việt",
                "english": "Tiếng Anh",
                
                # Messages
                "anki_connection_success": "Kết nối Anki thành công! Phiên bản AnkiConnect: {}",
                "anki_connection_error": "Lỗi kết nối Anki",
                "language_switched": "Đã chuyển sang chế độ {}.",
                "ui_language_switched": "Giao diện đã chuyển sang {}",
                "success": "Thành công",
                "error": "Lỗi",
                "warning": "Cảnh báo",
                "info": "Thông tin",
                
                # Logs
                "processing": "Đang xử lý...",
                "completed": "Hoàn thành!",
                "stopped": "Đã dừng",
                "connecting_anki": "Đang kết nối Anki...",
                "generating_audio": "Đang tạo audio...",
                "creating_cards": "Đang tạo thẻ...",
                
                # Additional UI elements
                "configuration": "Cấu hình",
                "word_processing_list": "Danh sách từ đang xử lý",
                "deck_name_optional": "Tên Deck (để trống để quét tất cả):",
                "audio_settings": "Cài đặt Audio",
                "overwrite_audio": "Ghi đè audio đã có",
            },
            
            "en": {
                # Main Window
                "app_title": "Multi-language Anki Tool by Dương Quốc Lợi",
                "help_menu": "Help",
                "test_anki_connection": "Test Anki Connection",
                "select_language": "Select Language:",
                "select_ui_language": "Interface:",
                "select_processing_language": "Processing:",
                
                # Tabs
                "phonetic_tab": "Create Phonetics",
                "audio_tab": "Create Audio",
                "ai_cards_tab": "AI Cards",
                
                # Phonetic Tab
                "input_text": "Input text:",
                "deck_name": "Deck Name:",
                "source_field": "Source Field:",
                "target_field": "Target Field:",
                "create_cards": "Create Cards",
                "stop": "Stop",
                
                # Audio Tab
                "audio_field": "Audio Field:",
                "audio_speed": "Speed:",
                "voice_selection": "Voice Selection:",
                "create_audio": "Create Audio",
                
                # Language options
                "korean": "Korean",
                "japanese": "Japanese",
                "vietnamese": "Vietnamese",
                "english": "English",
                
                # Messages
                "anki_connection_success": "Anki connection successful! AnkiConnect version: {}",
                "anki_connection_error": "Anki connection error",
                "language_switched": "Switched to {} mode.",
                "ui_language_switched": "Interface switched to {}",
                "success": "Success",
                "error": "Error",
                "warning": "Warning",
                "info": "Information",
                
                # Logs
                "processing": "Processing...",
                "completed": "Completed!",
                "stopped": "Stopped",
                "connecting_anki": "Connecting to Anki...",
                "generating_audio": "Generating audio...",
                "creating_cards": "Creating cards...",
                
                # Additional UI elements
                "configuration": "Configuration",
                "word_processing_list": "Word Processing List",
                "deck_name_optional": "Deck Name (leave empty to scan all):",
                "audio_settings": "Audio Settings",
                "overwrite_audio": "Overwrite existing audio",
            }
        }
    
    def set_ui_language(self, lang_code):
        """Set the UI language"""
        if lang_code in self.translations:
            self.current_ui_language = lang_code
            return True
        return False
    
    def get(self, key, *args):
        """Get translated text for current UI language"""
        try:
            text = self.translations[self.current_ui_language].get(key, key)
            if args:
                return text.format(*args)
            return text
        except:
            return key
    
    def get_available_ui_languages(self):
        """Get list of available UI languages"""
        return [
            ("vi", "Tiếng Việt"),
            ("en", "English")
        ]
    
    def get_processing_languages(self):
        """Get list of available processing languages"""
        return [
            ("korean", self.get("korean")),
            ("japanese", self.get("japanese")),
            ("vietnamese", self.get("vietnamese")),
            ("english", self.get("english"))
        ]

# Global language manager instance
lang_manager = LanguageManager()
