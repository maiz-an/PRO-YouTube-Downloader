import os
import sys
import subprocess
import platform
import shutil
import time
from pathlib import Path

def clear_screen():
    """Clear terminal screen cross-platform"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print setup banner"""
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                   PRO YouTube Downloader                      ║
║                  Universal Setup Assistant                    ║
╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python():
    """Check if Python is available"""
    try:
        result = subprocess.run([sys.executable, '--version'], 
                              capture_output=True, text=True, check=True)
        version = result.stdout.strip()
        print(f"✅ Python detected: {version}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Python not found or not in PATH")
        return False

def check_yt_dlp():
    """Check if yt-dlp is already installed"""
    try:
        result = subprocess.run([
            sys.executable, '-c', 'import yt_dlp; print(yt_dlp.version.__version__)'
        ], capture_output=True, text=True, check=True)
        version = result.stdout.strip()
        print(f"✅ yt-dlp already installed: version {version}")
        return True
    except subprocess.CalledProcessError:
        return False

def install_dependencies():
    """Install required Python packages only if needed"""
    if check_yt_dlp():
        print("📦 yt-dlp is already installed, skipping installation")
        return True
        
    packages = ['yt-dlp']
    
    print("📦 Installing Python dependencies...")
    for package in packages:
        try:
            print(f"🔧 Installing {package}...")
            subprocess.run([
                sys.executable, '-m', 'pip', 'install', 
                package, '--upgrade', '--quiet'
            ], check=True)
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {package}: {e}")
            return False
    return True

def download_ffmpeg_macos():
    """Download FFmpeg for macOS"""
    ffmpeg_dir = Path(__file__).parent / "FFmpeg" / "macos"
    ffmpeg_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg_path = ffmpeg_dir / "ffmpeg"
    
    print("📥 Downloading FFmpeg for macOS...")
    
    try:
        # Try to download from official source
        subprocess.run([
            'curl', '-L', '-o', str(ffmpeg_path),
            'https://evermeet.cx/ffmpeg/ffmpeg-7.0.1.zip'
        ], check=True, capture_output=True)
        
        # Extract if it's a zip file
        if ffmpeg_path.suffix == '.zip':
            import zipfile
            with zipfile.ZipFile(ffmpeg_path, 'r') as zip_ref:
                zip_ref.extractall(ffmpeg_dir)
            # Find the actual ffmpeg binary
            for file in ffmpeg_dir.iterdir():
                if file.name.startswith('ffmpeg') and not file.suffix == '.zip':
                    file.rename(ffmpeg_path)
                    break
        
        # Make executable
        ffmpeg_path.chmod(0o755)
        print(f"✅ FFmpeg downloaded for macOS: {ffmpeg_path}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to download FFmpeg for macOS: {e}")
        print("💡 Please download manually from: https://evermeet.cx/ffmpeg/")
        return False

def download_ffmpeg_linux():
    """Download FFmpeg for Linux"""
    ffmpeg_dir = Path(__file__).parent / "FFmpeg" / "linux"
    ffmpeg_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg_path = ffmpeg_dir / "ffmpeg"
    
    print("📥 Downloading FFmpeg for Linux...")
    
    try:
        # Download static build
        temp_dir = ffmpeg_dir / "temp"
        temp_dir.mkdir(exist_ok=True)
        
        # Download the static build
        download_path = temp_dir / "ffmpeg.tar.xz"
        subprocess.run([
            'wget', '-O', str(download_path),
            'https://johnvansickle.com/ffmpeg/releases/ffmpeg-git-amd64-static.tar.xz'
        ], check=True, capture_output=True)
        
        # Extract
        subprocess.run([
            'tar', '-xf', str(download_path), '-C', str(temp_dir)
        ], check=True, capture_output=True)
        
        # Find and copy the ffmpeg binary
        for item in temp_dir.iterdir():
            if item.is_dir() and 'ffmpeg-git' in item.name:
                ffmpeg_binary = item / "ffmpeg"
                if ffmpeg_binary.exists():
                    shutil.copy2(ffmpeg_binary, ffmpeg_path)
                    break
        
        # Cleanup
        shutil.rmtree(temp_dir)
        
        # Make executable
        ffmpeg_path.chmod(0o755)
        print(f"✅ FFmpeg downloaded for Linux: {ffmpeg_path}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to download FFmpeg for Linux: {e}")
        print("💡 Please download manually from: https://johnvansickle.com/ffmpeg/")
        return False

def setup_ffmpeg():
    """Setup FFmpeg paths - using bundled FFmpeg or download if missing"""
    system = platform.system().lower()
    
    # FFmpeg directory structure
    ffmpeg_base = Path(__file__).parent / "FFmpeg"
    
    if system == "windows":
        ffmpeg_path = ffmpeg_base / "ffmpeg-8.0.1" / "bin"
        ffmpeg_exe = ffmpeg_path / "ffmpeg.exe"
    elif system == "darwin":  # macOS
        ffmpeg_path = ffmpeg_base / "macos"
        ffmpeg_exe = ffmpeg_path / "ffmpeg"
        
        # Download if not exists
        if not ffmpeg_exe.exists():
            if download_ffmpeg_macos():
                ffmpeg_exe = ffmpeg_path / "ffmpeg"
            else:
                print("⚠️  FFmpeg download failed for macOS")
                
    elif system == "linux":
        ffmpeg_path = ffmpeg_base / "linux"
        ffmpeg_exe = ffmpeg_path / "ffmpeg"
        
        # Download if not exists
        if not ffmpeg_exe.exists():
            if download_ffmpeg_linux():
                ffmpeg_exe = ffmpeg_path / "ffmpeg"
            else:
                print("⚠️  FFmpeg download failed for Linux")
    else:
        ffmpeg_path = ffmpeg_base / "other"
        ffmpeg_exe = ffmpeg_path / "ffmpeg"
    
    # Check if FFmpeg exists in project
    if ffmpeg_exe.exists():
        print(f"✅ FFmpeg found: {ffmpeg_exe}")
        
        # Add to PATH for current process
        os.environ['PATH'] = str(ffmpeg_path) + os.pathsep + os.environ.get('PATH', '')
        
        # Verify FFmpeg works
        try:
            result = subprocess.run([str(ffmpeg_exe), '-version'], 
                                  capture_output=True, text=True, check=True)
            version_line = result.stdout.split('\n')[0]
            print(f"✅ {version_line}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("⚠️  FFmpeg found but not executable")
    else:
        print("⚠️  Bundled FFmpeg not found, checking system FFmpeg...")
        
        # Check system FFmpeg
        system_ffmpeg = shutil.which('ffmpeg')
        if system_ffmpeg:
            print(f"✅ Using system FFmpeg: {system_ffmpeg}")
            return True
        else:
            print("❌ No FFmpeg found. Some features may not work.")
    
    return False

def create_downloads_folder():
    """Create Downloads folder"""
    downloads_path = Path(__file__).parent.parent / "Downloads"
    downloads_path.mkdir(exist_ok=True)
    print(f"✅ Downloads folder: {downloads_path}")
    return downloads_path

def run_main_application():
    """Run the main Downloader application"""
    downloader_script = Path(__file__).parent / "Downloader.py"
    
    if not downloader_script.exists():
        print("❌ Error: Downloader.py not found!")
        return False
    
    print("🚀 Launching PRO YouTube Downloader...")
    print("═" * 60)
    
    try:
        # Run the main application directly in the same process
        import importlib.util
        spec = importlib.util.spec_from_file_location("downloader", downloader_script)
        downloader_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(downloader_module)
        
        # Call the main function
        downloader_module.main()
        return True
        
    except Exception as e:
        print(f"❌ Application error: {e}")
        return False

def check_system_readiness():
    """Check if system is ready without installing anything"""
    print("🔍 Checking system readiness...")
    
    # Check Python
    if not check_python():
        return False
    
    # Check yt-dlp
    if not check_yt_dlp():
        print("📦 yt-dlp needs to be installed")
        return False
    
    # Check FFmpeg
    system_ffmpeg = shutil.which('ffmpeg')
    ffmpeg_base = Path(__file__).parent / "FFmpeg"
    current_system = platform.system().lower()
    
    if current_system == "windows":
        ffmpeg_exe = ffmpeg_base / "ffmpeg-8.0.1" / "bin" / "ffmpeg.exe"
    else:
        ffmpeg_exe = ffmpeg_base / "ffmpeg"
    
    if not ffmpeg_exe.exists() and not system_ffmpeg:
        print("⚠️  FFmpeg not found")
        return False
    
    print("✅ System is ready!")
    return True

def main():
    """Main setup function"""
    clear_screen()
    print_banner()
    
    # Check if system is already ready
    if check_system_readiness():
        print("\n" + "═" * 60)
        print("✅ System is already set up! Launching application...")
        print("═" * 60)
        time.sleep(2)  # Brief pause to show the message
        clear_screen()
    else:
        print("\n🔍 Performing system setup...")
        print("═" * 60)
        
        # Step 1: Check Python
        print("\n[1/4] 🔍 Checking Python installation...")
        if not check_python():
            print("\n❌ Python is required. Please install Python 3.6+ from https://python.org")
            print("   Make sure to check 'Add Python to PATH' during installation.")
            input("\nPress Enter to exit...")
            return
        
        # Step 2: Install dependencies
        print("\n[2/4] 📦 Installing dependencies...")
        if not install_dependencies():
            print("\n❌ Failed to install dependencies")
            input("\nPress Enter to exit...")
            return
        
        # Step 3: Verify yt-dlp
        print("\n[3/4] 🔧 Verifying installation...")
        if not check_yt_dlp():
            print("\n❌ yt-dlp installation failed")
            input("\nPress Enter to exit...")
            return
        
        # Step 4: Setup FFmpeg
        print("\n[4/4] 🎬 Setting up FFmpeg...")
        setup_ffmpeg()
        
        print("\n" + "═" * 60)
        print("✅ Setup completed successfully!")
        print("═" * 60)
        time.sleep(2)  # Brief pause to show completion message
    
    # Create downloads folder
    print("\n📁 Setting up folders...")
    downloads_path = create_downloads_folder()
    
    print("\n" + "═" * 60)
    print("🚀 Launching PRO YouTube Downloader...")
    print(f"📁 Downloads will be saved in: {downloads_path}")
    print("═" * 60)
    
    # Automatic countdown instead of requiring Enter
    print("\n🕐 Launching PRO YouTube Downloader 🚀")
    time.sleep(0.1)
    clear_screen()
    
    # Run main application
    success = run_main_application()
    
    if success:
        print("\n" + "═" * 60)
        print("👋 Thank you for using PRO YouTube Downloader!")
        print(f"📂 Your downloaded files are in: {downloads_path}")
        print("═" * 60)
    else:
        print("\n❌ Application failed to run properly")
    
    # Only ask for Enter if there was an error
    if not success:
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Setup cancelled by user")
        input("\nPress Enter to exit...")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        input("\nPress Enter to exit...")