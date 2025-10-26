#!/usr/bin/env python3
"""
🚀 PRO YouTube Downloader - iOS Launcher
Perfect companion to Run.bat - Same functionality for iOS
"""

import os
import sys
import subprocess
import platform
import time
import requests

# Colors for iOS terminal
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    END = '\033[0m'

def clear_screen():
    """Clear screen for iOS"""
    os.system('clear')

def print_banner():
    """Print iOS-optimized banner matching Windows version"""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════════╗
║                    PRO YouTube Downloader                     ║
║                  iOS Setup Assistant                          ║
╚════════════════════════════════════════════════════════════════╝
{Colors.END}
"""
    print(banner)

def check_ios_environment():
    """Check if we're running on iOS and detect environment"""
    print(f"{Colors.BLUE}🔍 Scanning for required files...{Colors.END}")
    
    # Check for Source/Downloader.py (same structure as Windows)
    possible_paths = [
        'Source/Downloader.py',
        'Downloader.py',
        '../Source/Downloader.py',
        './Source/Downloader.py'
    ]
    
    script_path = None
    for path in possible_paths:
        if os.path.exists(path):
            script_path = path
            print(f"✅ Found: {path}")
            break
    
    if not script_path:
        print(f"{Colors.RED}❌ Error: Downloader.py not found!{Colors.END}")
        print(f"📁 Current location: {os.getcwd()}")
        print(f"\n{Colors.YELLOW}🔧 iOS Setup Assistant: Let me help you fix this!{Colors.END}")
        print(f"\nPossible solutions:")
        print(f"1. Ensure the folder structure is:")
        print(f"   MainFolder/")
        print(f"   ├── RunIOS.py (this file)")
        print(f"   └── Source/")
        print(f"       └── Downloader.py")
        print(f"\n2. Or Downloader.py should be in the same folder as RunIOS.py")
        
        response = input(f"\n{Colors.CYAN}Create the folder structure automatically? (y/n): {Colors.END}").lower().strip()
        if response == 'y':
            print(f"\n{Colors.GREEN}🛠️ Creating folder structure...{Colors.END}")
            os.makedirs('Source', exist_ok=True)
            print(f"📁 Created: Source/")
            print(f"\n{Colors.YELLOW}📝 Please make sure to:")
            print(f"   - Place Downloader.py in the 'Source' folder")
            print(f"   - Then run this script again{Colors.END}")
            return None
        else:
            print(f"\n{Colors.YELLOW}💡 Manual setup required.")
            print(f"Please ensure Downloader.py is in the correct location.{Colors.END}")
            return None
    
    return script_path

def check_python_installation():
    """Check Python installation (iOS usually has Python)"""
    print(f"\n{Colors.BLUE}[1/3] 🔍 Checking Python installation...{Colors.END}")
    
    try:
        result = subprocess.run([sys.executable, '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ {version}")
            return True
    except:
        pass
    
    print(f"{Colors.RED}❌ Python not found!{Colors.END}")
    print(f"\n{Colors.YELLOW}🔧 iOS Setup Assistant: Python is required!{Colors.END}")
    print(f"\nOn iOS, you can:")
    print(f"1. Use {Colors.BOLD}a-Shell{Colors.END} (has Python pre-installed)")
    print(f"2. Use {Colors.BOLD}Pythonista 3{Colors.END} (paid)")
    print(f"3. Use {Colors.BOLD}Carnets{Colors.END} (Jupyter with Python)")
    return False

def check_dependencies():
    """Check and install required dependencies"""
    print(f"\n{Colors.BLUE}[2/3] 📚 Checking Python dependencies...{Colors.END}")
    
    # Check yt-dlp
    try:
        import yt_dlp
        version = yt_dlp.version.__version__
        print(f"✅ yt-dlp: {version}")
        return True
    except ImportError:
        print(f"{Colors.YELLOW}🔄 yt-dlp not found. Installing now...{Colors.END}")
        return install_yt_dlp()

def install_yt_dlp():
    """Install yt-dlp with retry logic"""
    attempts = 3
    for attempt in range(1, attempts + 1):
        print(f"🔄 Attempt {attempt}: Installing yt-dlp...")
        try:
            result = subprocess.run([
                sys.executable, '-m', 'pip', 'install', 'yt-dlp', '--upgrade',
                '--no-warn-script-location', '--user'
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                # Verify installation
                try:
                    import yt_dlp
                    version = yt_dlp.version.__version__
                    print(f"✅ yt-dlp installed successfully: {version}")
                    return True
                except ImportError:
                    continue
                    
        except Exception as e:
            print(f"❌ Installation error: {e}")
    
    print(f"{Colors.RED}❌ Failed to install yt-dlp after {attempts} attempts.{Colors.END}")
    print(f"\n{Colors.YELLOW}⚠️ The application may not work properly without yt-dlp.{Colors.END}")
    return False

def check_ffmpeg():
    """Check FFmpeg availability"""
    print(f"\n{Colors.BLUE}[3/3] 🎬 Checking FFmpeg installation...{Colors.END}")
    
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            for line in result.stdout.split('\n'):
                if 'ffmpeg version' in line:
                    version = line.split('ffmpeg version')[1].split()[0]
                    print(f"✅ FFmpeg: {version}")
                    return True
    except:
        pass
    
    print(f"{Colors.YELLOW}⚠️ FFmpeg not found (optional for basic features){Colors.END}")
    print(f"   Some features like audio extraction may be limited")
    return False

def setup_directories():
    """Create necessary directories"""
    print(f"\n{Colors.BLUE}📁 Setting up directories...{Colors.END}")
    
    directories = ['Downloads', 'Source', 'Config']
    for dir_name in directories:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)
            print(f"✅ Created: {dir_name}/")

def launch_downloader(script_path):
    """Launch the main downloader application"""
    clear_screen()
    
    print(f"{Colors.GREEN}{Colors.BOLD}")
    print("════════════════════════════════════════════════════════════════")
    print("✅ All systems ready! Launching PRO YouTube Downloader...")
    print(f"📁 Downloads will be saved in: {os.path.abspath('Downloads')}")
    print(f"📍 Running from: {os.getcwd()}")
    print("════════════════════════════════════════════════════════════════")
    print(Colors.END)
    
    time.sleep(2)
    clear_screen()
    
    print(f"{Colors.GREEN}🚀 Launching PRO YouTube Downloader...{Colors.END}\n")
    
    try:
        # Run the main application
        result = subprocess.run([sys.executable, script_path])
        return result.returncode
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⏹️ Downloader stopped by user{Colors.END}")
        return 0
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error running downloader: {e}{Colors.END}")
        return 1

def main():
    """Main iOS launcher - mirrors Windows .bat functionality"""
    clear_screen()
    print_banner()
    
    # Check file structure
    script_path = check_ios_environment()
    if not script_path:
        input(f"\n{Colors.YELLOW}Press Enter to exit...{Colors.END}")
        return
    
    # System checks
    if not check_python_installation():
        input(f"\n{Colors.YELLOW}Press Enter to exit...{Colors.END}")
        return
    
    if not check_dependencies():
        print(f"\n{Colors.YELLOW}Continuing with limited functionality...{Colors.END}")
    
    check_ffmpeg()
    setup_directories()
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}✅ Setup completed successfully!{Colors.END}")
    
    # Launch the application
    exit_code = launch_downloader(script_path)
    
    # Handle application exit
    if exit_code != 0:
        print(f"\n{Colors.RED}❌ Application exited with error code: {exit_code}{Colors.END}")
        response = input(f"\n{Colors.CYAN}Restart the application? (y/n): {Colors.END}").lower().strip()
        if response == 'y':
            print(f"\n{Colors.GREEN}🔄 Restarting application...{Colors.END}")
            time.sleep(2)
            launch_downloader(script_path)
    
    print(f"\n{Colors.CYAN}{Colors.BOLD}👋 Thank you for using PRO YouTube Downloader!")
    print(f"📂 Your downloaded files are in: {os.path.abspath('Downloads')}{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}👋 Goodbye!{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Unexpected error: {e}{Colors.END}")
        input(f"\nPress Enter to exit...")