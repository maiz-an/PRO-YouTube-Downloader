#!/usr/bin/env python3
"""
PRO YouTube Downloader - Android Launcher
For running in Termux and other Android Python environments
"""

import os
import sys
import subprocess
import time
import platform

def clear_screen():
    """Clear screen for Android compatibility"""
    if platform.system() == "Linux" and "android" in str(os.uname()):
        os.system("clear")
    else:
        print("\n" * 50)

def print_banner():
    """Print setup banner"""
    banner = """
╔════════════════════════════════════════════════════════════════╗
║                    PRO YouTube Downloader                     ║
║                  Android Setup Assistant                      ║
╚════════════════════════════════════════════════════════════════╝
"""
    print(banner)

def check_android_environment():
    """Check if running on Android"""
    print("📱 Checking Android environment...")
    try:
        # Check for Termux or Android-specific paths
        if "com.termux" in os.getcwd() or "ANDROID_ROOT" in os.environ:
            print("✅ Running on Android (Termux)")
            return True
        elif "android" in str(os.uname()).lower():
            print("✅ Running on Android")
            return True
        else:
            print("⚠️  Not detected as Android environment")
            return False
    except:
        return False

def check_python():
    """Check Python installation"""
    print("[1/4] 🔍 Checking Python installation...")
    python_version = sys.version.split()[0]
    print(f"✅ Python {python_version}")
    return True

def check_termux_packages():
    """Check and install Termux packages if needed"""
    print("[2/4] 📦 Checking system packages...")
    
    # Check if we're in Termux
    if not os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
        print("ℹ️  Not in Termux, skipping package checks")
        return True
    
    required_packages = ["ffmpeg", "python"]
    missing_packages = []
    
    for pkg in required_packages:
        try:
            result = subprocess.run(["pkg", "list-installed"], capture_output=True, text=True)
            if pkg not in result.stdout:
                missing_packages.append(pkg)
        except:
            missing_packages.append(pkg)
    
    if missing_packages:
        print(f"🔄 Installing missing packages: {', '.join(missing_packages)}")
        try:
            subprocess.run(["pkg", "install", "-y"] + missing_packages, check=True)
            print("✅ Packages installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install packages: {e}")
            print("💡 Run manually: pkg install ffmpeg python")
            return False
    
    return True

def check_dependencies():
    """Check and install Python dependencies"""
    print("[3/4] 📚 Checking Python dependencies...")
    
    # Check yt-dlp
    try:
        import yt_dlp
        version = yt_dlp.version.__version__
        print(f"✅ yt-dlp: {version}")
        return True
    except ImportError:
        print("🔄 yt-dlp not found. Installing now...")
        
        attempts = 3
        for attempt in range(1, attempts + 1):
            print(f"🔄 Attempt {attempt}: Installing yt-dlp...")
            try:
                # Use pip with --user flag for Android compatibility
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", 
                    "yt-dlp", "--upgrade", "--user", "--quiet"
                ])
                import yt_dlp
                version = yt_dlp.version.__version__
                print(f"✅ yt-dlp installed successfully: {version}")
                return True
            except Exception as e:
                print(f"❌ Attempt {attempt} failed: {e}")
                if attempt < attempts:
                    time.sleep(2)
        
        print("❌ Failed to install yt-dlp after 3 attempts.")
        print("💡 Try manually: pip install yt-dlp --user")
        return False

def check_ffmpeg():
    """Check FFmpeg installation"""
    print("[4/4] 🎬 Checking FFmpeg installation...")
    try:
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
        if result.returncode == 0:
            # Extract version from output
            for line in result.stdout.split('\n'):
                if 'ffmpeg version' in line:
                    version = line.split('ffmpeg version')[-1].split()[0]
                    print(f"✅ FFmpeg: {version}")
                    return True
        print("❌ FFmpeg not found or not working")
        print("💡 Install with: pkg install ffmpeg (Termux)")
        return False
    except Exception as e:
        print("❌ FFmpeg not found in PATH")
        print("💡 Install with: pkg install ffmpeg (Termux)")
        return False

def setup_directories():
    """Create necessary directories with Android-friendly paths"""
    print("📁 Setting up directories...")
    
    # Get current directory
    current_dir = os.getcwd()
    
    # For Android, use current directory or create in Downloads if accessible
    if "Android" in current_dir or "/sdcard" in current_dir:
        # We're in Android storage area
        downloads_dir = os.path.join(current_dir, "PRO_Youtube_Downloads")
    else:
        # In Termux home or other location
        downloads_dir = os.path.join(current_dir, "Downloads")
    
    config_dir = os.path.join(current_dir, "Config")
    
    try:
        os.makedirs(downloads_dir, exist_ok=True)
        print(f"✅ Created: {downloads_dir}")
    except Exception as e:
        print(f"❌ Failed to create downloads directory: {e}")
        # Fallback to current directory
        downloads_dir = current_dir
        print(f"📁 Using current directory: {downloads_dir}")
    
    try:
        os.makedirs(config_dir, exist_ok=True)
        print("✅ Created: Config/")
    except Exception:
        pass  # Config directory is optional
    
    return downloads_dir, current_dir

def get_storage_permission():
    """Guide user for storage permissions on Android"""
    print("\n🔐 Android Storage Permissions Guide:")
    print("═" * 50)
    print("For Termux users:")
    print("1. Run: termux-setup-storage")
    print("2. Allow storage permission when prompted")
    print("3. This gives access to: /sdcard/Download/")
    print()
    print("For other Android Python apps:")
    print("• Check app settings for storage permissions")
    print("• Downloads will be in app's internal storage")
    print("═" * 50)
    
    if os.path.exists("/data/data/com.termux/files/usr/bin/termux-setup-storage"):
        choice = input("Run termux-setup-storage now? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            try:
                subprocess.run(["termux-setup-storage"], check=True)
                print("✅ Storage setup completed!")
                time.sleep(2)
            except Exception as e:
                print(f"❌ Storage setup failed: {e}")

def main():
    """Main setup and launcher function"""
    clear_screen()
    print_banner()
    
    # Check Android environment
    is_android = check_android_environment()
    
    if is_android:
        get_storage_permission()
    
    # Check for required files
    print("\n🔍 Scanning for required files...")
    
    # Look for Downloader.py in various locations
    possible_paths = [
        "Source/Downloader.py",
        "Downloader.py",
        "./Source/Downloader.py",
        "./Downloader.py"
    ]
    
    downloader_path = None
    for path in possible_paths:
        if os.path.exists(path):
            downloader_path = path
            print(f"✅ Found: {path}")
            break
    
    if not downloader_path:
        print("❌ Error: Downloader.py not found!")
        print("\n📁 Current location:", os.getcwd())
        print("\n🔧 Please ensure the file structure is:")
        print("   MainFolder/")
        print("   ├── RunAndroid.py (this file)")
        print("   └── Source/")
        print("       └── Downloader.py")
        print("\n💡 Or place Downloader.py in the same folder as RunAndroid.py")
        input("\nPress Enter to exit...")
        return
    
    # Perform system checks
    check_python()
    
    if is_android:
        check_termux_packages()
    
    deps_ok = check_dependencies()
    ffmpeg_ok = check_ffmpeg()
    
    # Setup directories
    downloads_dir, current_dir = setup_directories()
    
    print("\n" + "═" * 64)
    print("✅ All systems ready! Launching PRO YouTube Downloader...")
    print(f"📁 Downloads will be saved in: {downloads_dir}")
    print(f"📍 Running from: {current_dir}")
    
    if is_android:
        print("📱 Running on: Android")
    print("═" * 64)
    
    # Wait a moment
    time.sleep(2)
    
    # Launch the main application
    while True:
        try:
            clear_screen()
            print("🚀 Launching PRO YouTube Downloader...")
            print()
            
            # Change to the directory containing Downloader.py
            script_dir = os.path.dirname(os.path.abspath(downloader_path))
            os.chdir(script_dir)
            
            # Run the main application
            subprocess.run([sys.executable, os.path.basename(downloader_path)])
            
        except Exception as e:
            print(f"❌ Error launching application: {e}")
        
        # Ask if user wants to restart
        try:
            restart = input("\n🔁 Restart the application? (y/n): ").strip().lower()
            if restart not in ['y', 'yes']:
                break
            print("🔄 Restarting...")
            time.sleep(2)
        except (KeyboardInterrupt, EOFError):
            break
    
    print("\n👋 Thank you for using PRO YouTube Downloader!")
    print(f"📂 Your downloaded files are in: {downloads_dir}")
    
    if is_android and "/sdcard" in downloads_dir:
        print("\n💡 Android Tip: Use your file manager to access downloaded files")
        print("   Location: Internal Storage/PRO_Youtube_Downloads/")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️ Setup interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        input("Press Enter to exit...")