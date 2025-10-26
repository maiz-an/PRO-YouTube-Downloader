import os
import sys
import threading
import time
import json
from datetime import datetime
from yt_dlp import YoutubeDL

# Set DOWNLOAD_DIR to the Mainfolder/Downloads directory
DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Configuration file path
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloader_config.json")

spinner_running = False
spinner_thread = None

# Default configuration
DEFAULT_CONFIG = {
    "download_dir": DOWNLOAD_DIR,
    "max_downloads": 5,
    "enable_logging": True,
    "auto_retry": True,
    "max_retries": 3
}

def load_config():
    """Load configuration from file or create default"""
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return {**DEFAULT_CONFIG, **json.load(f)}
    except Exception:
        pass
    return DEFAULT_CONFIG.copy()

def save_config(config):
    """Save configuration to file"""
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
    except Exception:
        pass

def spinner():
    """Enhanced spinner with progress indication"""
    phases = ["⏳ Downloading... \\", "⏳ Downloading... |", "⏳ Downloading... /", "⏳ Downloading... -"]
    idx = 0
    while spinner_running:
        sys.stdout.write(f"\r{phases[idx]}")
        sys.stdout.flush()
        time.sleep(0.15)
        idx = (idx + 1) % len(phases)

def start_spinner():
    global spinner_running, spinner_thread
    spinner_running = True
    spinner_thread = threading.Thread(target=spinner)
    spinner_thread.daemon = True
    spinner_thread.start()

def stop_spinner():
    global spinner_running
    spinner_running = False
    time.sleep(0.2)
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print application banner"""
    banner = """
╔══════════════════════════════════════════════╗
║            🚀 PRO YT Downloader 🚀           ║
║           Premium YouTube Downloader         ║
╚══════════════════════════════════════════════╝
    """
    print(banner)

def print_menu():
    """Print main menu with enhanced visual design"""
    print("\n" + "═" * 55)
    print("            🎯 DOWNLOAD OPTIONS")
    print("═" * 55)
    print("1. 📹 Download Video (Best Quality)")
    print("2. 🎵 Download Audio MP3 (320kbps)")
    print("3. 🔧 Manual Select Format")
    print("4. ⚙️  Settings")
    print("5. 📊 Download History")
    print("6. ❌ Exit")
    print("═" * 55)
    print(f"📁 Current Download Folder: {DOWNLOAD_DIR}")
    print("═" * 55)

def print_settings_menu():
    """Print settings menu"""
    print("\n" + "═" * 55)
    print("            ⚙️  SETTINGS")
    print("═" * 55)
    print("1. 📂 Change Download Folder")
    print("2. 🔄 Auto-retry Failed Downloads")
    print("3. 📝 Enable/Disable Logging")
    print("4. 🧹 Clear Download History")
    print("5. ↩️  Back to Main Menu")
    print("═" * 55)

def mode_text(mode):
    modes = {
        "1": "Video", 
        "2": "MP3", 
        "3": "Custom Format"
    }
    return modes.get(mode, "Unknown")

def log_download(url, filename, mode, status="Success"):
    """Log download activity"""
    try:
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": url,
            "filename": filename,
            "mode": mode_text(mode),
            "status": status
        }
        
        log_file = os.path.join(os.path.dirname(CONFIG_FILE), "download_history.json")
        history = []
        
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                try:
                    history = json.load(f)
                except:
                    history = []
        
        history.append(log_entry)
        
        # Keep only last 50 entries
        if len(history) > 50:
            history = history[-50:]
        
        with open(log_file, 'w') as f:
            json.dump(history, f, indent=2)
    except Exception:
        pass

def show_download_history():
    """Display download history"""
    log_file = os.path.join(os.path.dirname(CONFIG_FILE), "download_history.json")
    
    if not os.path.exists(log_file):
        print("\n❌ No download history found.")
        return
    
    try:
        with open(log_file, 'r') as f:
            history = json.load(f)
        
        if not history:
            print("\n❌ No download history found.")
            return
        
        print("\n" + "═" * 80)
        print("                            📊 DOWNLOAD HISTORY")
        print("═" * 80)
        print(f"{'Date/Time':<20} {'Type':<12} {'Status':<10} {'Filename'}")
        print("-" * 80)
        
        for entry in reversed(history[-10:]):  # Show last 10 entries
            filename = entry.get('filename', 'Unknown')
            if len(filename) > 35:
                filename = filename[:32] + "..."
            print(f"{entry['timestamp']:<20} {entry['mode']:<12} {entry['status']:<10} {filename}")
        
        print("═" * 80)
        input("\nPress Enter to continue...")
        
    except Exception as e:
        print(f"\n❌ Error loading history: {e}")

def get_video_info(url):
    """Get video information without downloading"""
    try:
        with YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                'title': info.get('title', 'Unknown'),
                'duration': info.get('duration', 0),
                'uploader': info.get('uploader', 'Unknown'),
                'view_count': info.get('view_count', 0),
                'upload_date': info.get('upload_date', 'Unknown')
            }
    except Exception:
        return None

def format_duration(seconds):
    """Format duration from seconds to MM:SS or HH:MM:SS"""
    if not seconds:
        return "Unknown"
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes:02d}:{seconds:02d}"

def progress_hook(info):
    """Enhanced progress hook with detailed information"""
    if info["status"] == "downloading":
        # Show download progress if available
        if '_percent_str' in info:
            percent = info['_percent_str'].strip()
            speed = info.get('_speed_str', 'N/A').strip()
            eta = info.get('_eta_str', 'N/A').strip()
            sys.stdout.write(f"\r⏳ Downloading... {percent} | Speed: {speed} | ETA: {eta}")
            sys.stdout.flush()
    
    elif info["status"] == "finished":
        stop_spinner()
        filepath = info.get("filepath", "Unknown")
        
        if filepath != "Unknown":
            filepath = os.path.abspath(filepath)
            filename = os.path.basename(filepath)
            file_size = os.path.getsize(filepath) if os.path.exists(filepath) else 0
            size_mb = file_size / (1024 * 1024)
            
            print("\n" + "═" * 55)
            print("            ✅ DOWNLOAD COMPLETED")
            print("═" * 55)
            print(f"📄 File name: {filename}")
            print(f"📂 Location: {os.path.dirname(filepath)}")
            print(f"💾 File size: {size_mb:.2f} MB")
            print(f"⏰ Completed at: {datetime.now().strftime('%H:%M:%S')}")
            print("═" * 55 + "\n")
        else:
            print("\n✅ Download Completed Successfully")
            print("📂 File saved: Unknown (check download folder)\n")

def download(url, mode, config, retry_count=0):
    """Enhanced download function with retry logic"""
    ydl_opts = {
        "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
        "progress_hooks": [progress_hook],
        "noplaylist": True,
        "quiet": True,
        "no_warnings": False,
    }

    if mode == "1":
        ydl_opts.update({
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
        })
    elif mode == "2":
        ydl_opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }]
        })
    elif mode == "3":
        try:
            print("\n📋 Fetching available formats...")
            with YoutubeDL({"listformats": True, "quiet": True}) as ydl:
                ydl.download([url])
            print("\n" + "─" * 50)
            fmt = input("🎯 Enter format ID: ").strip()
            if not fmt:
                print("❌ No format ID entered")
                return
            ydl_opts.update({"format": fmt})
        except Exception as e:
            print(f"❌ Failed to fetch formats: {e}")
            return

    try:
        # Show video info before downloading
        print("\n🔍 Fetching video information...")
        video_info = get_video_info(url)
        if video_info:
            print("\n" + "─" * 50)
            print("📹 VIDEO INFORMATION")
            print("─" * 50)
            print(f"📺 Title: {video_info['title']}")
            print(f"👤 Channel: {video_info['uploader']}")
            print(f"⏱️ Duration: {format_duration(video_info['duration'])}")
            print(f"👀 Views: {video_info['view_count']:,}")
            print(f"📅 Upload date: {video_info['upload_date']}")
            print("─" * 50)
        
        start_spinner()
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            # Log successful download
            log_download(url, os.path.basename(filename), mode, "Success")
            
    except Exception as e:
        stop_spinner()
        error_msg = str(e)
        print(f"\n❌ Download Error: {error_msg}")
        
        # Log failed download
        log_download(url, "Unknown", mode, f"Failed: {error_msg}")
        
        if config.get('auto_retry', True) and retry_count < config.get('max_retries', 3):
            retry_count += 1
            print(f"🔄 Retrying... Attempt {retry_count} of {config.get('max_retries', 3)}")
            time.sleep(2)
            download(url, mode, config, retry_count)
        else:
            retry = input("\n🔄 Retry download? (y/n): ").lower().strip()
            if retry == 'y':
                download(url, mode, config)

def change_download_folder():
    """Change the download folder"""
    global DOWNLOAD_DIR
    print(f"\n📁 Current download folder: {DOWNLOAD_DIR}")
    new_folder = input("Enter new download folder path: ").strip()
    
    if new_folder:
        try:
            # Expand user directory if ~ is used
            new_folder = os.path.expanduser(new_folder)
            os.makedirs(new_folder, exist_ok=True)
            
            # Test if directory is writable
            test_file = os.path.join(new_folder, 'test_write.tmp')
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            
            DOWNLOAD_DIR = new_folder
            print(f"✅ Download folder changed to: {DOWNLOAD_DIR}")
            
            # Update config
            config = load_config()
            config['download_dir'] = DOWNLOAD_DIR
            save_config(config)
            
        except Exception as e:
            print(f"❌ Error: Cannot write to directory. {e}")
    else:
        print("❌ No path provided.")

def settings_menu(config):
    """Handle settings menu"""
    while True:
        clear_screen()
        print_banner()
        print_settings_menu()
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            change_download_folder()
        elif choice == "2":
            auto_retry = not config.get('auto_retry', True)
            config['auto_retry'] = auto_retry
            save_config(config)
            status = "enabled" if auto_retry else "disabled"
            print(f"✅ Auto-retry {status}")
        elif choice == "3":
            logging_enabled = not config.get('enable_logging', True)
            config['enable_logging'] = logging_enabled
            save_config(config)
            status = "enabled" if logging_enabled else "disabled"
            print(f"✅ Logging {status}")
        elif choice == "4":
            confirm = input("🧹 Are you sure you want to clear download history? (y/n): ").lower()
            if confirm == 'y':
                log_file = os.path.join(os.path.dirname(CONFIG_FILE), "download_history.json")
                try:
                    if os.path.exists(log_file):
                        os.remove(log_file)
                    print("✅ Download history cleared.")
                except Exception as e:
                    print(f"❌ Error clearing history: {e}")
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice. Please select 1-5.")
        
        input("\nPress Enter to continue...")

def main():
    """Main application function"""
    config = load_config()
    global DOWNLOAD_DIR
    DOWNLOAD_DIR = config.get('download_dir', DOWNLOAD_DIR)
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    clear_screen()
    print_banner()
    print(f"✨ Welcome to PRO YouTube Downloader ✨")
    print(f"📁 Download location: {DOWNLOAD_DIR}")
    
    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1" or choice == "2" or choice == "3":
            # Download modes
            while True:
                prompt = f"\n🎯 Enter YouTube link to download {mode_text(choice)} (or '0' to change mode): "
                url = input(prompt).strip()
                
                if url == "0":
                    break
                    
                if not url:
                    print("❌ Please enter a valid URL")
                    continue
                    
                if "youtube.com" not in url and "youtu.be" not in url:
                    print("❌ Please enter a valid YouTube URL")
                    continue
                    
                download(url, choice, config)
                
                again = input("\n📥 Download another file? (y/n): ").lower().strip()
                if again != "y":
                    break
        
        elif choice == "4":
            # Settings
            settings_menu(config)
            clear_screen()
            print_banner()
            
        elif choice == "5":
            # Download History
            clear_screen()
            print_banner()
            show_download_history()
            clear_screen()
            print_banner()
            
        elif choice == "6":
            # Exit
            print("\n👋 Thanks for using PRO Downloader. Goodbye!")
            print(f"📂 Your files are saved in: {DOWNLOAD_DIR}")
            break
            
        else:
            print("❌ Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Downloader stopped by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        input("Press Enter to exit...")