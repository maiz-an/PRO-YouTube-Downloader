#!/usr/bin/env python3
"""
🚀 PRO YouTube Downloader - Mobile Launcher
Compatible with: a-Shell (iOS), Termux (Android), Pydroid (Android)
"""

import os
import sys
import subprocess
import platform
import time

# Colors for mobile terminals that support them
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def clear_screen():
    """Clear screen for mobile terminals"""
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    """Print mobile-optimized banner"""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════╗
║            🚀 PRO YT Downloader 🚀           ║
║           Mobile Edition v1.0               ║
╚══════════════════════════════════════════════╝
{Colors.END}
"""
    print(banner)

def check_platform():
    """Check if we're running on a supported mobile platform"""
    system = platform.system().lower()
    
    # Detect mobile environments
    mobile_indicators = [
        'ANDROID_ROOT' in os.environ,
        'TERMUX_VERSION' in os.environ,
        'PYTHONISTA' in os.environ,
        'a-Shell' in sys.executable if sys.executable else False,
        'ios' in system,
        'android' in system
    ]
    
    is_mobile = any(mobile_indicators)
    
    print(f"{Colors.BLUE}📱 Platform Detection:{Colors.END}")
    print(f"  System: {platform.system()} {platform.release()}")
    print(f"  Python: {platform.python_version()}")
    print(f"  Mobile Environment: {'Yes' if is_mobile else 'No'}")
    print()
    
    return is_mobile

def check_dependencies():
    """Check and install required dependencies"""
    print(f"{Colors.BLUE}📦 Dependency Check:{Colors.END}")
    
    dependencies = ['yt-dlp']
    missing_deps = []
    
    for dep in dependencies:
        try:
            if dep == 'yt-dlp':
                import yt_dlp
                version = yt_dlp.version.__version__
                print(f"  ✅ {dep}: {version}")
            else:
                __import__(dep)
                print(f"  ✅ {dep}: Installed")
        except ImportError:
            print(f"  ❌ {dep}: Missing")
            missing_deps.append(dep)
    
    return missing_deps

def install_dependencies(dependencies):
    """Install missing dependencies"""
    if not dependencies:
        return True
        
    print(f"\n{Colors.YELLOW}🔧 Installing missing dependencies...{Colors.END}")
    
    for dep in dependencies:
        print(f"  📥 Installing {dep}...")
        try:
            # Use pip to install the package
            result = subprocess.run([
                sys.executable, '-m', 'pip', 'install', dep, '--upgrade',
                '--no-warn-script-location'
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"  ✅ {dep}: Installed successfully")
            else:
                print(f"  ❌ {dep}: Installation failed")
                print(f"     Error: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"  ❌ {dep}: Installation error: {e}")
            return False
    
    return True

def setup_directories():
    """Create necessary directories for mobile"""
    print(f"{Colors.BLUE}📁 Setting up directories:{Colors.END}")
    
    directories = [
        'Downloads',
        'Source',
        'Config'
    ]
    
    for dir_name in directories:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)
            print(f"  ✅ Created: {dir_name}/")
        else:
            print(f"  📁 Found: {dir_name}/")

def find_downloader_script():
    """Find the main downloader script"""
    possible_paths = [
        'Source/Downloader.py',
        'Downloader.py',
        '../Source/Downloader.py',
        './Source/Downloader.py'
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            print(f"  ✅ Found main script: {path}")
            return path
    
    # If not found, create a basic one or guide user
    print(f"  ❌ Main script not found in common locations")
    return None

def check_ffmpeg():
    """Check if FFmpeg is available (optional for mobile)"""
    print(f"{Colors.BLUE}🎬 Checking FFmpeg:{Colors.END}")
    
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            # Extract version from output
            for line in result.stdout.split('\n'):
                if 'ffmpeg version' in line:
                    version = line.split('ffmpeg version')[1].split()[0]
                    print(f"  ✅ FFmpeg: {version}")
                    return True
    except (subprocess.SubprocessError, FileNotFoundError):
        print(f"  ⚠️  FFmpeg: Not found (optional for basic features)")
        print(f"     Some features like audio extraction may be limited")
        return False

def run_downloader(script_path):
    """Run the main downloader script"""
    if not script_path or not os.path.exists(script_path):
        print(f"\n{Colors.RED}❌ Error: Cannot find main downloader script{Colors.END}")
        print(f"Please ensure 'Downloader.py' exists in the Source folder")
        return False
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}🚀 Launching PRO YouTube Downloader...{Colors.END}")
    print(f"📁 Script: {script_path}")
    print(f"💾 Downloads: {os.path.abspath('Downloads')}")
    print(f"\n{Colors.YELLOW}Press Ctrl+C to exit at any time{Colors.END}")
    print("-" * 50)
    
    try:
        # Run the main script
        result = subprocess.run([sys.executable, script_path])
        return result.returncode == 0
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⏹️  Downloader stopped by user{Colors.END}")
        return True
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error running downloader: {e}{Colors.END}")
        return False

def show_mobile_tips():
    """Show mobile-specific usage tips"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}📱 Mobile Usage Tips:{Colors.END}")
    print(f"  • Use {Colors.BOLD}Wi-Fi{Colors.END} for large downloads")
    print(f"  • {Colors.BOLD}MP3 downloads{Colors.END} use less data")
    print(f"  • Keep screen on for progress updates")
    print(f"  • Check {Colors.BOLD}storage space{Colors.END} before large playlists")
    print(f"  • Use {Colors.BOLD}Option 4 (Quiet Mode){Colors.END} for faster downloads")

def main():
    """Main mobile launcher function"""
    clear_screen()
    print_banner()
    
    # Check if we're on a mobile platform
    is_mobile = check_platform()
    
    if not is_mobile:
        print(f"{Colors.YELLOW}⚠️  This launcher is optimized for mobile devices{Colors.END}")
        print(f"   For desktop, use the provided .bat file instead")
        print()
    
    # Setup phase
    setup_directories()
    print()
    
    # Dependency check
    missing_deps = check_dependencies()
    print()
    
    # Install dependencies if needed
    if missing_deps:
        if not install_dependencies(missing_deps):
            print(f"\n{Colors.RED}❌ Failed to install required dependencies{Colors.END}")
            print(f"Please install manually: pip install {' '.join(missing_deps)}")
            input("\nPress Enter to exit...")
            return
    
    # Check FFmpeg (optional)
    check_ffmpeg()
    print()
    
    # Find main script
    script_path = find_downloader_script()
    print()
    
    if not script_path:
        print(f"{Colors.RED}❌ Cannot proceed without main downloader script{Colors.END}")
        print(f"Please ensure the file structure is:")
        print(f"  MainFolder/")
        print(f"  ├── RunMoby.py (this file)")
        print(f"  ├── Run.bat")
        print(f"  └── Source/")
        print(f"      └── Downloader.py (main script)")
        input("\nPress Enter to exit...")
        return
    
    # Show mobile tips
    show_mobile_tips()
    
    # Ask user if they want to proceed
    print(f"\n{Colors.GREEN}{Colors.BOLD}Ready to launch!{Colors.END}")
    try:
        input("\nPress Enter to start the downloader...")
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}👋 Goodbye!{Colors.END}")
        return
    
    # Clear screen and run
    clear_screen()
    
    # Run the downloader in a loop so users can restart easily
    while True:
        success = run_downloader(script_path)
        
        if success:
            print(f"\n{Colors.GREEN}✅ Downloader completed successfully{Colors.END}")
        else:
            print(f"\n{Colors.RED}❌ Downloader encountered an error{Colors.END}")
        
        # Ask if user wants to restart
        print(f"\n{Colors.CYAN}What would you like to do?{Colors.END}")
        print(f"  1. Restart Downloader")
        print(f"  2. Exit")
        
        try:
            choice = input(f"\nEnter choice (1-2): ").strip()
            if choice == '2':
                break
            elif choice == '1':
                clear_screen()
                print_banner()
                print(f"{Colors.GREEN}🔄 Restarting downloader...{Colors.END}\n")
                continue
            else:
                print(f"{Colors.YELLOW}⚠️  Invalid choice, restarting...{Colors.END}")
                time.sleep(2)
                clear_screen()
                print_banner()
                continue
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}👋 Goodbye!{Colors.END}")
            break
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}✨ Thank you for using PRO YouTube Downloader!{Colors.END}")
    print(f"📂 Your files are in: {os.path.abspath('Downloads')}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}👋 Goodbye!{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Unexpected error: {e}{Colors.END}")
        print(f"Please report this issue.")
        input("\nPress Enter to exit...")