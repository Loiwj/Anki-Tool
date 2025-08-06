# Changelog

All notable changes to AnkiTool will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-08-06

### 🎉 Initial Release

#### ✨ Added
- **AI-Powered Card Creation**: Integration with Google Gemini AI for automatic card generation
- **Phonetic Transcription**: Automatic IPA (International Phonetic Alphabet) generation
- **Text-to-Speech**: High-quality audio generation for pronunciation
- **Anki Integration**: Direct synchronization with Anki via AnkiConnect
- **Multi-language Support**: English and Vietnamese language support
- **Modern GUI**: Tab-based interface with Arc theme
- **Standalone Executable**: No Python installation required

#### 🛠️ Technical Features
- **cx_Freeze Build System**: Reliable executable generation
- **Environment Configuration**: Secure API key management via .env files
- **Error Handling**: Comprehensive error messages and fallbacks
- **Resource Management**: Efficient handling of audio and image assets

#### 📦 Distribution
- **Windows Executable**: Ready-to-run .exe file
- **Package Management**: Automated zip packaging for distribution
- **Documentation**: Comprehensive README and user guides
- **Build Scripts**: Automated build and packaging workflows

### 🎯 Features by Tab

#### Tab 1: AI-Generated Cards
- Definition generation
- Example sentences
- Multiple choice questions
- Synonym suggestions

#### Tab 2: Phonetic Cards  
- IPA transcription
- Audio pronunciation
- Voice selection
- Speed control

#### Tab 3: Audio Cards
- Text-to-speech conversion
- Audio quality options
- Custom voice settings
- Batch processing

### 🔧 Technical Specifications
- **Python Version**: 3.10+
- **Build Tool**: cx_Freeze 6.15.0
- **AI Service**: Google Gemini
- **TTS Service**: Google Text-to-Speech
- **UI Framework**: Tkinter with ttkthemes
- **Platform**: Windows 10/11 (64-bit)

### 📊 Metrics
- **Package Size**: ~62MB (compressed)
- **Executable Size**: ~100MB (with dependencies)
- **Startup Time**: <3 seconds
- **Memory Usage**: ~80MB average

---

## [Upcoming] - v2.0.0

### 🗺️ Planned Features
- **Batch Processing**: Multiple cards at once
- **Custom Templates**: User-defined card templates  
- **Learning Analytics**: Progress tracking and statistics
- **Offline Mode**: Limited functionality without internet
- **Plugin System**: Extensible architecture
- **Web Interface**: Browser-based alternative
- **Mobile Companion**: Android/iOS app
- **Cloud Sync**: Cross-device synchronization

### 🔄 Improvements
- **Performance**: Faster AI response times
- **UI/UX**: Enhanced user interface
- **Localization**: Additional language support
- **Accessibility**: Screen reader compatibility
- **API**: RESTful API for third-party integration

---

## Development Notes

### Build Process
1. **Development**: Python source code development
2. **Testing**: Manual testing on Windows 10/11
3. **Packaging**: cx_Freeze executable generation
4. **Distribution**: ZIP package creation
5. **Documentation**: README and user guide updates

### Known Issues
- Large executable size due to AI dependencies
- Internet connection required for full functionality
- Windows-only support (cross-platform planned for v2.0)

### Dependencies
- `google-generativeai`: AI integration
- `requests`: HTTP client
- `ttkthemes`: Modern UI themes  
- `python-dotenv`: Environment configuration
- `cx_Freeze`: Executable building

---

*For detailed technical information, see the repository documentation.*
