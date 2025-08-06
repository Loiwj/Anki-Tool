import os
import sys
from dotenv import load_dotenv
from ttkthemes import ThemedTk
import tkinter as tk
from gui.main_window import MainWindow

def main():
    # Print startup info
    print("=" * 60)
    print("🚀 AnkiTool - Multi-language Anki Card Creator")
    print("   by Dương Quốc Lợi")
    print("=" * 60)
    print("📱 Running in Development Mode")
    print("🌍 Supports: Korean, Japanese, Vietnamese, English")
    print("🎯 Features: AI Cards, Phonetics, Audio Generation")
    print("=" * 60)
    
    # Tải biến môi trường từ file .env
    env_file = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_file):
        load_dotenv(env_file)
    else:
        load_dotenv()
    
    api_keys_str = os.getenv("GEMINI_API_KEYS")
    
    # Debug: Print what we found
    print(f"🔍 Looking for .env file at: {env_file}")
    print(f"🔍 File exists: {os.path.exists(env_file)}")
    if os.path.exists(env_file):
        with open(env_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"🔍 .env content: {content[:50]}...")
    print(f"🔍 API keys found: {'Yes' if api_keys_str else 'No'}")
    
    if not api_keys_str:
        print("❌ ERROR: GEMINI_API_KEYS not found in .env file.")
        print("📝 Please create .env file and add: GEMINI_API_KEYS=\"key1,key2,...\"")
        print("\n🔧 How to get API keys:")
        print("   1. Visit: https://aistudio.google.com/app/apikey")
        print("   2. Create new API key")
        print("   3. Add to .env file")
        print("\n📋 Example .env file:")
        print("   GEMINI_API_KEYS=\"your-api-key-here\"")
        print("=" * 60)
        input("Press Enter to exit...")
        return

    print("✅ API keys loaded successfully")
    print("🎨 Starting GUI...")
    print("=" * 60)

    # Khởi tạo giao diện
    try:
        root = ThemedTk(theme="arc")
        print("✅ Arc theme loaded")
    except tk.TclError:
        root = tk.Tk()
        print("⚠️  Using default theme (Arc theme not available)")
        
    # Set icon if available
    icon_path = os.path.join(os.path.dirname(__file__), "assets", "icon.ico")
    if os.path.exists(icon_path):
        try:
            root.iconbitmap(icon_path)
            print("✅ Application icon loaded")
        except:
            print("⚠️  Could not load application icon")
    
    # Set window properties
    root.geometry("900x700")
    root.minsize(800, 600)
    
    print("🎯 Initializing AnkiTool...")
    app = MainWindow(root, api_keys_str)
    
    print("🚀 AnkiTool is ready!")
    print("📖 Usage Instructions:")
    print("   • Select Interface Language: Vietnamese/English")
    print("   • Select Processing Language: Korean/Japanese/Vietnamese/English") 
    print("   • Make sure Anki is running with AnkiConnect addon")
    print("   • Test connection via Help menu")
    print("=" * 60)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\n👋 AnkiTool closed by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()