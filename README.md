# 🎓 AnkiTool - AI-Powered Anki Learning Assistant

<div align="center">

![AnkiTool Logo](assets/icon.ico)

**Smart learning tool powered by AI Gemini | Công cụ học tập thông minh với sự hỗ trợ của AI Gemini**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://microsoft.com/windows)
[![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)](https://ai.google.dev)
[![Languages](https://img.shields.io/badge/Languages-4-purple.svg)](README.md)
[![Version](https://img.shields.io/badge/Version-1.1.0-brightgreen.svg)](CHANGELOG.md)

[🚀 Download](#-download--installation) • [📖 User Guide](#-user-guide) • [🎯 Features](#-key-features) • [🛠️ Development](#-development) | [🚀 Tải về](#-tải-về-và-cài-đặt) • [📖 Hướng dẫn](#-hướng-dẫn-sử-dụng) • [🎯 Tính năng](#-tính-năng-chính) • [🛠️ Phát triển](#-phát-triển)

</div>

---

# 🇺🇸 ENGLISH VERSION

## 🌟 Introduction

**AnkiTool** is an intelligent learning tool that uses AI Gemini to automatically create Anki cards. Version 1.1 features **multilingual interface** and supports **4 different processing languages**!

### 🌍 **Complete multilingual support:**
- **UI Interface**: Vietnamese 🇻🇳 & English 🇺🇸  
- **Content Processing**: Korean 🇰🇷, Japanese 🇯🇵, Vietnamese 🇻🇳, English 🇺🇸

### 🚀 **Two usage modes:**
1. **Standalone Application** - Run `.exe` file (no Python installation required)
2. **Development Mode** - Run `python main.py` (requires Python 3.10+)

### ✨ Why choose AnkiTool?

- 🤖 **AI-Powered**: Uses Google Gemini to automatically generate definitions, examples, and questions
- 🔊 **Text-to-Speech**: Creates high-quality pronunciation audio files
- 📚 **IPA Phonetics**: Automatically generates International Phonetic Alphabet symbols
- 🔗 **Anki Integration**: Direct synchronization with Anki via AnkiConnect
- 🎨 **User-Friendly Interface**: Modern design, easy to use
- 🚀 **Standalone**: Runs independently, no Python installation needed

---

## 🎯 Key Features

### 🌍 **Multilingual Support**
- **Interface**: Vietnamese & English - instant switching
- **Processing**: Korean, Japanese, Vietnamese, English - automatic mapping
- **Smart**: Automatically adjusts fields based on selected language

### 🤖 **AI-Generated Cards**
- Automatically generates vocabulary definitions with AI Gemini
- Creates rich contextual examples
- Generates smart multiple-choice questions
- Supports multilingual processing

### 🔊 **Phonetic & Audio Cards**
- Generates IPA (International Phonetic Alphabet) symbols
- Creates high-quality automatic pronunciation audio files
- Supports multiple voice options
- Customizable reading speed from 0.5x to 1.2x

### 📱 **Modern Interface**
- Multilingual interface with language switcher
- Tab-based interface with Arc theme
- Optimized responsive design
- Progress indicators and real-time feedback

---

## 🚀 Download & Installation

### 📋 System Requirements

- **OS**: Windows 10/11 (64-bit)  
- **RAM**: Minimum 4GB
- **Internet**: Required for AI and TTS services
- **Anki**: Version 2.1.x or higher with AnkiConnect
- **Python**: 3.10+ (only for development mode)

### 🎯 Two Usage Methods

#### 🚀 **Executable Mode** (Recommended)
```bash
# Download AnkiTool-v1.1.zip (62MB)  
# Extract and run AnkiTool.exe
# No Python installation needed!
```

#### 🛠️ **Development Mode**
```bash
# Clone repository
git clone https://github.com/Loiwj/Anki-Tool.git
cd ankitool

# Install dependencies  
pip install -r requirements.txt

# Run directly
python main.py
```

### 📝 Setup Steps

1. **Download AnkiTool**
   ```
   📁 AnkiTool-v1.1.zip
   ```

2. **Extract** to any folder

3. **Install Anki & AnkiConnect**
   - Download Anki from [ankiweb.net](https://apps.ankiweb.net/)
   - Install AnkiConnect: Tools → Add-ons → Get Add-ons → `2055492159`

4. **Configure API Keys**
   - Copy `.env.example` to `.env`
   - Get Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Add to `.env` file:
     ```env
     GEMINI_API_KEYS="your_api_key_here"
     ```

5. **Run Application**
   - Double-click `AnkiTool.exe`
   - Ensure Anki is running

---

## 📖 User Guide

### 🎯 "AI Cards" Tab

<details>
<summary>🔽 Detailed Usage</summary>

1. **Enter word/phrase** to learn
2. **Select card type**:
   - 📝 Definition
   - 💡 Example
   - ❓ Question
   - 🔄 Synonym
3. **Choose language**: English/Vietnamese/Korean/Japanese
4. **Generate card**: AI will automatically create content
5. **Review & Save**: Check and save to Anki

</details>

### 🔊 "Phonetic Cards" Tab

<details>
<summary>🔽 Detailed Usage</summary>

1. **Enter English word**
2. **Generate phonetics**: System automatically creates IPA
3. **Create audio**: Choose voice and reading speed
4. **Preview**: Listen to audio
5. **Save card**: Includes word + IPA + audio

</details>

### 🎵 "Audio Cards" Tab

<details>
<summary>🔽 Detailed Usage</summary>

1. **Enter text**: Sentence or paragraph
2. **Configure**:
   - 👨‍🎤 Male/female voice
   - ⚡ Reading speed
   - 🎚️ Audio quality
3. **Generate audio**: Convert text to speech
4. **Save card**: Audio card for listening practice

</details>

---

## 🛠️ Advanced Configuration

### 🔑 API Keys Management

```env
# .env file
GEMINI_API_KEYS="key1,key2,key3"  # Multiple keys for load balancing
```

### 🎨 Themes & UI

- **Arc Theme**: Modern default theme
- **Fallback**: Automatically switches to Tkinter if error occurs
- **Responsive**: Auto-adjusts to screen size

### 📊 Performance Tips

- 🔄 **API Rotation**: Use multiple API keys to avoid rate limits
- 💾 **Caching**: Results are cached for faster performance
- 🌐 **Offline Mode**: Some features work offline

---

## 🐛 Troubleshooting

<details>
<summary>❌ ".env file not found"</summary>

**Cause**: API configuration file not created  
**Solution**: 
1. Copy `.env.example` to `.env`
2. Add API keys to `.env` file

</details>

<details>
<summary>❌ "Cannot connect to Anki"</summary>

**Cause**: Anki not running or missing AnkiConnect  
**Solution**: 
1. Open Anki before running AnkiTool
2. Install AnkiConnect addon (code: `2055492159`)
3. Restart Anki after installing addon

</details>

<details>
<summary>❌ "Invalid API key"</summary>

**Cause**: Incorrect or expired API key  
**Solution**: 
1. Check API key at [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create new API key if needed
3. Update `.env` file

</details>

---

## 🔧 Development

### 🏗️ Build from Source

```bash
# Clone repository
git clone https://github.com/Loiwj/Anki-Tool.git
cd ankitool

# Install dependencies  
pip install -r requirements.txt

# Run development
python main.py

# Build executable
python setup.py build
```

### 📁 Project Structure

```
ankitool/
├── 📄 main.py              # Entry point
├── 📁 gui/                 # GUI components
│   ├── main_window.py      # Main interface
│   ├── language_manager.py # Language management
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

## 📊 Statistics & Roadmap

### 📈 Current Features
- ✅ AI-powered card generation
- ✅ IPA phonetic transcription  
- ✅ Text-to-speech audio
- ✅ Anki integration
- ✅ Multi-language support
- ✅ Standalone executable

### 🗺️ Roadmap v2.0
- 🔄 Batch processing
- 📱 Mobile companion app
- 🌐 Web interface
- 🎯 Advanced AI models
- 📊 Learning analytics

---

## 📞 Contact & Support

<div align="center">

📧 **Email**: duongquocloi1010@gmail.com  
🌐 **GitHub**: [Loiwj/Anki-Tool](https://github.com/Loiwj/Anki-Tool)

</div>

---

---

# 🇻🇳 PHIÊN BẢN TIẾNG VIỆT

## 🌟 Giới thiệu

**AnkiTool** là công cụ học tập thông minh sử dụng AI Gemini để tạo thẻ Anki tự động. Phiên bản 1.1 mới với **giao diện đa ngôn ngữ** và hỗ trợ **4 ngôn ngữ xử lý** khác nhau!

### 🌍 **Đa ngôn ngữ hoàn toàn:**
- **Giao diện UI**: Tiếng Việt 🇻🇳 & English 🇺🇸  
- **Xử lý nội dung**: Tiếng Hàn 🇰🇷, Nhật 🇯🇵, Việt 🇻🇳, Anh 🇺🇸

### 🚀 **Hai cách sử dụng:**
1. **Ứng dụng độc lập** - Chạy file `.exe` (không cần cài Python)
2. **Chế độ phát triển** - Chạy `python main.py` (cần Python 3.10+)

### ✨ Tại sao chọn AnkiTool?

- 🤖 **AI-Powered**: Sử dụng Google Gemini để tự động tạo định nghĩa, ví dụ, và câu hỏi
- 🔊 **Text-to-Speech**: Tạo file audio phát âm chất lượng cao
- 📚 **Phiên âm IPA**: Tự động tạo ký hiệu phiên âm quốc tế
- 🔗 **Tích hợp Anki**: Đồng bộ trực tiếp với Anki thông qua AnkiConnect
- 🎨 **Giao diện thân thiện**: Thiết kế hiện đại, dễ sử dụng
- 🚀 **Standalone**: Chạy độc lập, không cần cài đặt Python

---

## 🎯 Tính năng chính

### 🌍 **Hỗ trợ đa ngôn ngữ**
- **Giao diện**: Tiếng Việt & English - chuyển đổi tức thì
- **Xử lý**: Hàn Quốc, Nhật Bản, Việt Nam, Anh - mapping tự động
- **Thông minh**: Tự động điều chỉnh field dựa trên ngôn ngữ chọn

### 🤖 **Thẻ AI-Generated**
- Tự động tạo định nghĩa từ vựng với AI Gemini
- Tạo ví dụ minh họa context phong phú
- Tạo câu hỏi trắc nghiệm thông minh
- Hỗ trợ đa ngôn ngữ trong xử lý

### 🔊 **Thẻ Phonetic & Audio**
- Tạo ký hiệu IPA (International Phonetic Alphabet)
- Tạo file audio phát âm tự động chất lượng cao
- Hỗ trợ nhiều giọng đọc khác nhau
- Tùy chỉnh tốc độ đọc từ 0.5x đến 1.2x

### 📱 **Giao diện hiện đại**
- Interface đa ngôn ngữ với language switcher
- Tab-based interface với Arc theme
- Responsive design tối ưu
- Progress indicators và real-time feedback

---

## 🚀 Tải về và Cài đặt

### 📋 Yêu cầu hệ thống

- **OS**: Windows 10/11 (64-bit)  
- **RAM**: Tối thiểu 4GB
- **Internet**: Cần kết nối để sử dụng AI và TTS
- **Anki**: Phiên bản 2.1.x trở lên với AnkiConnect
- **Python**: 3.10+ (chỉ cho development mode)

### 🎯 Hai cách sử dụng

#### 🚀 **Executable Mode** (Khuyến nghị)
```bash
# Tải file AnkiTool-v1.1.zip (62MB)  
# Giải nén và chạy AnkiTool.exe
# Không cần cài Python!
```

#### 🛠️ **Development Mode**
```bash
# Clone repository
git clone https://github.com/Loiwj/Anki-Tool.git
cd ankitool

# Cài đặt dependencies  
pip install -r requirements.txt

# Chạy trực tiếp
python main.py
```

### 📝 Các bước thiết lập

1. **Tải về AnkiTool**
   ```
   📁 AnkiTool-v1.1.zip
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
3. **Chọn ngôn ngữ**: Tiếng Anh/Việt/Hàn/Nhật
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

### 🔑 Quản lý API Keys

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
git clone https://github.com/Loiwj/Anki-Tool.git
cd ankitool

# Cài đặt dependencies  
pip install -r requirements.txt

# Chạy development
python main.py

# Build executable
python setup.py build
```

### 📁 Cấu trúc Project

```
ankitool/
├── 📄 main.py              # Entry point
├── 📁 gui/                 # GUI components
│   ├── main_window.py      # Main interface
│   ├── language_manager.py # Quản lý ngôn ngữ
│   ├── audio_tab.py        # Audio features
│   └── phonetic_tab.py     # Phonetic features
├── 📁 services/            # Business logic
│   ├── anki_connect.py     # Anki integration
│   ├── gemini_client.py    # AI client
│   └── google_tts.py       # Text-to-speech
├── 📁 assets/              # Resources
└── 📄 requirements.txt     # Dependencies
```

### 🤝 Đóng góp

1. Fork repository
2. Tạo feature branch (`git checkout -b feature/amazing-feature`)
3. Commit thay đổi (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Tạo Pull Request

---

## 📊 Thống kê & Roadmap

### 📈 Tính năng hiện tại
- ✅ AI-powered card generation
- ✅ IPA phonetic transcription  
- ✅ Text-to-speech audio
- ✅ Anki integration
- ✅ Multi-language support
- ✅ Standalone executable

### 🗺️ Roadmap v2.0
- 🔄 Batch processing
- 📱 Mobile companion app
- 🌐 Web interface
- 🎯 Advanced AI models
- 📊 Learning analytics

---

## 📞 Liên hệ & Hỗ trợ

<div align="center">

📧 **Email**: duongquocloi1010@gmail.com  
🌐 **GitHub**: [Loiwj/Anki-Tool](https://github.com/Loiwj/Anki-Tool)

</div>

---

## 📄 License

Dự án được phát hành dưới [MIT License](LICENSE) - xem file LICENSE để biết chi tiết.

---

<div align="center">

**⭐ If the app is helpful, please give us a star on GitHub! | Nếu ứng dụng hữu ích, hãy cho chúng tôi một star trên GitHub! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/Loiwj/Anki-Tool.svg?style=social&label=Star)](https://github.com/Loiwj/Anki-Tool)

---

**Made with ❤️ by Duong Quoc Loi**  
*Empowering learning through AI technology | Trao quyền học tập thông qua công nghệ AI*

</div>
