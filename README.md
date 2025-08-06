# 🎓 AnkiTool - AI-Powered Anki Learning Assistant

<div align="center">

![AnkiTool Logo](assets/icon.ico)

**Công cụ học tập thông minh với sự hỗ trợ của AI Gemini**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://microsoft.com/windows)
[![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)](https://ai.google.dev)

[🚀 Tải về](#-tải-về-và-cài-đặt) • [📖 Hướng dẫn](#-hướng-dẫn-sử-dụng) • [🎯 Tính năng](#-tính-năng-chính) • [🛠️ Phát triển](#-phát-triển)

</div>

---

## 🌟 Giới thiệu

**AnkiTool** là ứng dụng desktop mạnh mẽ giúp bạn tạo và quản lý thẻ học Anki một cách thông minh với sự hỗ trợ của AI Google Gemini. Ứng dụng tự động hóa quá trình tạo thẻ, tạo phiên âm IPA, và tạo file audio, giúp bạn học hiệu quả hơn.

### ✨ Tại sao chọn AnkiTool?

- 🤖 **AI-Powered**: Sử dụng Google Gemini để tự động tạo định nghĩa, ví dụ, và câu hỏi
- 🔊 **Text-to-Speech**: Tạo file audio phát âm chất lượng cao
- 📚 **Phiên âm IPA**: Tự động tạo ký hiệu phiên âm quốc tế
- 🔗 **Tích hợp Anki**: Đồng bộ trực tiếp với Anki thông qua AnkiConnect
- 🎨 **Giao diện thân thiện**: Thiết kế hiện đại, dễ sử dụng
- 🚀 **Standalone**: Chạy độc lập, không cần cài đặt Python

---

## 🎯 Tính năng chính

### 🤖 Thẻ AI-Generated
- Tự động tạo định nghĩa từ vựng
- Tạo ví dụ minh họa context
- Tạo câu hỏi trắc nghiệm
- Hỗ trợ tiếng Anh và tiếng Việt

### 🔊 Thẻ Phonetic & Audio
- Tạo ký hiệu IPA (International Phonetic Alphabet)
- Tạo file audio phát âm tự động
- Hỗ trợ nhiều giọng đọc khác nhau
- Tùy chỉnh tốc độ đọc

### 📱 Giao diện hiện đại
- Tab-based interface
- Theme hỗ trợ
- Responsive design
- Progress indicators

---

## 🚀 Tải về và Cài đặt

### 📋 Yêu cầu hệ thống

- **OS**: Windows 10/11 (64-bit)
- **RAM**: Tối thiểu 4GB
- **Internet**: Cần kết nối để sử dụng AI và TTS
- **Anki**: Phiên bản 2.1.x trở lên
- **AnkiConnect**: Add-on code `2055492159`

### 📦 Cài đặt nhanh

1. **Tải về AnkiTool**
   ```
   📁 AnkiTool-v1.0.zip
   ```

2. **Giải nén** vào thư mục bất kỳ

3. **Cài đặt Anki & AnkiConnect**
   - Tải Anki từ [ankiweb.net](https://apps.ankiweb.net/)
   - Cài AnkiConnect: Tools → Add-ons → Get Add-ons → `2055492159`

4. **Cấu hình API Keys**
   - Sao chép `.env.example` thành `.env`
   - Lấy Gemini API key từ [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Thêm vào file `.env`:
     ```env
     GEMINI_API_KEYS="your_api_key_here"
     ```

5. **Chạy ứng dụng**
   - Double-click `AnkiTool.exe`
   - Đảm bảo Anki đang chạy

---

## 📖 Hướng dẫn sử dụng

### 🎯 Tab "Thẻ với AI"

<details>
<summary>🔽 Chi tiết sử dụng</summary>

1. **Nhập từ/cụm từ** cần học
2. **Chọn loại thẻ**:
   - 📝 Định nghĩa
   - 💡 Ví dụ
   - ❓ Câu hỏi
   - 🔄 Đồng nghĩa
3. **Chọn ngôn ngữ**: Tiếng Anh/Việt
4. **Tạo thẻ**: AI sẽ tự động sinh nội dung
5. **Review & Save**: Kiểm tra và lưu vào Anki

</details>

### 🔊 Tab "Thẻ Phonetic"

<details>
<summary>🔽 Chi tiết sử dụng</summary>

1. **Nhập từ tiếng Anh**
2. **Tạo phiên âm**: Hệ thống tự động tạo IPA
3. **Tạo audio**: Chọn giọng và tốc độ đọc
4. **Preview**: Nghe thử audio
5. **Lưu thẻ**: Bao gồm từ + IPA + audio

</details>

### 🎵 Tab "Thẻ Audio"

<details>
<summary>🔽 Chi tiết sử dụng</summary>

1. **Nhập văn bản**: Câu hoặc đoạn văn
2. **Cấu hình**:
   - 👨‍🎤 Giọng nam/nữ
   - ⚡ Tốc độ đọc
   - 🎚️ Chất lượng audio
3. **Tạo audio**: Chuyển text thành speech
4. **Lưu thẻ**: Thẻ audio cho luyện nghe

</details>

---

## 🛠️ Cấu hình nâng cao

### 🔑 API Keys Management

```env
# File .env
GEMINI_API_KEYS="key1,key2,key3"  # Nhiều keys để load balancing
```

### 🎨 Themes & UI

- **Arc Theme**: Theme mặc định hiện đại
- **Fallback**: Tự động chuyển về Tkinter nếu lỗi
- **Responsive**: Tự động điều chỉnh theo screen size

### 📊 Performance Tips

- 🔄 **API Rotation**: Sử dụng nhiều API keys để tránh rate limit
- 💾 **Caching**: Kết quả được cache để tăng tốc
- 🌐 **Offline Mode**: Một số tính năng hoạt động offline

---

## 🐛 Xử lý lỗi thường gặp

<details>
<summary>❌ "Không tìm thấy file .env"</summary>

**Nguyên nhân**: Chưa tạo file cấu hình API  
**Giải pháp**: 
1. Sao chép `.env.example` thành `.env`
2. Thêm API keys vào file `.env`

</details>

<details>
<summary>❌ "Không kết nối được Anki"</summary>

**Nguyên nhân**: Anki không chạy hoặc thiếu AnkiConnect  
**Giải pháp**: 
1. Mở Anki trước khi chạy AnkiTool
2. Cài AnkiConnect addon (code: `2055492159`)
3. Restart Anki sau khi cài addon

</details>

<details>
<summary>❌ "API key không hợp lệ"</summary>

**Nguyên nhân**: API key sai hoặc hết hạn  
**Giải pháp**: 
1. Kiểm tra API key tại [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Tạo API key mới nếu cần
3. Cập nhật file `.env`

</details>

---

## 🔧 Phát triển

### 🏗️ Build từ Source Code

```bash
# Clone repository
git clone https://github.com/your-username/ankitool.git
cd ankitool

# Cài đặt dependencies  
pip install -r requirements.txt

# Chạy development
python main.py

# Build executable
powershell -ExecutionPolicy Bypass -File build.ps1
```

### 📁 Cấu trúc Project

```
ankitool/
├── 📄 main.py              # Entry point
├── 📁 gui/                 # GUI components
│   ├── main_window.py      # Main interface
│   ├── audio_tab.py        # Audio features
│   └── phonetic_tab.py     # Phonetic features
├── 📁 services/            # Business logic
│   ├── anki_connect.py     # Anki integration
│   ├── gemini_client.py    # AI client
│   └── google_tts.py       # Text-to-speech
├── 📁 assets/              # Resources
└── 📄 requirements.txt     # Dependencies
```

### 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📊 Thống kê & Roadmap

### 📈 Tính năng hiện tại
- ✅ AI-powered card generation
- ✅ IPA phonetic transcription  
- ✅ Text-to-speech audio
- ✅ Anki integration
- ✅ Multi-language support

### 🗺️ Roadmap v2.0
- 🔄 Batch processing
- 📱 Mobile companion app
- 🌐 Web interface
- 🎯 Advanced AI models
- 📊 Learning analytics

---

## 📞 Liên hệ & Hỗ trợ

<div align="center">

📧 **Email**: support@ankitool.app  
🐛 **Bug Reports**: [GitHub Issues](https://github.com/your-username/ankitool/issues)  
💬 **Discussions**: [GitHub Discussions](https://github.com/your-username/ankitool/discussions)  
📖 **Wiki**: [Documentation](https://github.com/your-username/ankitool/wiki)

</div>

---

## 📄 License

Dự án được phát hành dưới [MIT License](LICENSE) - xem file LICENSE để biết chi tiết.

---

<div align="center">

**⭐ Nếu ứng dụng hữu ích, hãy cho chúng tôi một star trên GitHub! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/your-username/ankitool.svg?style=social&label=Star)](https://github.com/your-username/ankitool)

---

**Made with ❤️ by AnkiTool Team**  
*Empowering learning through AI technology*

</div>
