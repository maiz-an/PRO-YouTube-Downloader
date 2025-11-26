# PRO YouTube Downloader 🎥➡️💾

<div align="center">

![YouTube Downloader](https://img.shields.io/badge/PRO-YouTube%20Downloader-red?style=for-the-badge&logo=youtube)
![Multi-Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6%2B-green?style=for-the-badge&logo=python)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Bundled-orange?style=for-the-badge&logo=ffmpeg)

**The Ultimate Cross-Platform YouTube Downloader with Smart Auto-Setup**

*Download videos, playlists, and audio from YouTube with one click!*

</div>

## ✨ Features

### 🎯 Download Options

- **🎬 Video Download** - Highest quality MP4
- **🎵 Audio Extraction** - MP3 320kbps
- **📚 Playlist Support** - Entire playlists automatically
- **🔧 Manual Selection** - Choose specific formats
- **⏳ Real-time Progress** - Live download progress with speed and ETA

### 🤖 Smart Automation

- **🚀 One-Click Setup** - Automatic dependency installation
- **🛡️ Self-Healing** - Auto-retry and crash recovery
- **📦 Dependency Management** - Handles Python, FFmpeg, yt-dlp automatically
- **🎯 Platform Detection** - Optimized for Windows, macOS, Linux
- **🔧 Auto FFmpeg** - Automatically downloads FFmpeg for macOS/Linux

### 💻 User Experience

- **🎨 Beautiful Interface** - Professional console UI with emojis
- **📊 Real-time Progress** - Live percentage, speed, and ETA display
- **📝 Download History** - Track all your downloads
- **⚙️ Customizable Settings** - Multiple configuration options
- **🔕 Clean Output** - No technical warnings or clutter

## 🚀 Quick Start

### Choose Your Platform (Easiest Method)

| Platform | Launcher File | How to Run |
|----------|---------------|------------|
| **🖥️ Windows** | `Run.bat` | **Double-click** the file |
| **🍎 macOS** | `Run.command` | **Double-click** the file |
| **🐧 Linux** | `Run.sh` | **Double-click** or run `./Run.sh` |

### Alternative: Universal Launcher

```bash
# All platforms (if Python is in PATH):
python Source/launcher.py
```

### First-Time Setup (macOS/Linux Only)

After downloading, open Terminal and run:

```bash
# Navigate to the downloaded folder
cd "PRO YouTube Downloader"

# Make launchers executable (one-time setup)
chmod +x Run.command Run.sh
```

**Windows users:** Just double-click `Run.bat` - no setup needed!

## 📁 Project Structure

```
PRO-YouTube-Downloader/
├── 🚀 Run.bat                 # Windows Launcher (Double-click)
├── 🚀 Run.command             # macOS Launcher (Double-click)  
├── 🚀 Run.sh                  # Linux Launcher (Double-click)
├── 📖 README.md               # This file
├── 📁 Downloads/              # Downloaded files
└── 📁 Source/                 # All application files
    ├── 🐍 launcher.py         # Main setup launcher
    ├── 🐍 Downloader.py       # Main application
    ├── 🎬 FFmpeg/             # Bundled FFmpeg binaries
    │   ├── windows/           # Windows FFmpeg
    │   ├── macos/             # macOS FFmpeg (auto-downloaded)
    │   └── linux/             # Linux FFmpeg (auto-downloaded)
    └── ⚙️ *.json             # Configuration files
```

## 🎮 How to Use

### Basic Usage

1. **Double-click the launcher** for your platform (`Run.bat`, `Run.command`, or `Run.sh`)
2. **Watch the magic** - everything installs automatically!
3. **Select download type** from the menu:
   - `1` - Video (Best Quality)
   - `2` - Audio (MP3 320kbps)
   - `3` - Manual Format Selection
   - `4` - Settings
   - `5` - Download History
   - `6` - Exit

4. **Paste YouTube URL** when prompted
5. **Watch real-time progress** with percentage, speed, and ETA
6. **Find your files** in the `Downloads` folder

### Advanced Features

- **📚 Playlists**: Paste playlist URL to download all videos
- **⚙️ Settings**: Change download folder, enable auto-retry, toggle quiet mode
- **📊 History**: View your download history and status
- **🔄 Retry**: Automatic retry on failed downloads
- **🔕 Clean Mode**: No technical warnings or clutter

## 🛠️ Technical Details

### Dependencies (Auto-Managed)

- **Python 3.6+** - Runtime environment (auto-detected)
- **FFmpeg** - Audio/video processing (bundled/auto-downloaded)
- **yt-dlp** - Enhanced YouTube downloading (auto-installed)
- **All packages** - Automatically handled by the launcher

### Supported Platforms

- **✅ Windows** (10, 11) - Full feature support with bundled FFmpeg
- **✅ macOS** (10.14+) - Full feature support with auto-downloaded FFmpeg
- **✅ Linux** (Ubuntu, Fedora, etc.) - Full feature support with auto-downloaded FFmpeg

### Download Formats

- **Video**: MP4, WebM, MKV (best available)
- **Audio**: MP3 320kbps, M4A, Opus
- **Quality**: 144p to 4K (as available)
- **Codecs**: H.264, VP9, AV1

## 🔧 Smart Features

### Automatic Setup Process

```
🔍 Checking system readiness...
✅ Python detected: Python 3.13.2
✅ yt-dlp already installed: version 2025.11.12
✅ System is ready!

🚀 Launching PRO YouTube Downloader...
```

### FFmpeg Auto-Download

- **Windows**: Uses pre-bundled FFmpeg
- **macOS**: Automatically downloads from evermeet.cx
- **Linux**: Automatically downloads static builds from johnvansickle.com

### Clean User Experience

- No technical warnings or debug messages
- Real-time progress with percentage and speed
- Professional completion messages
- Automatic error recovery

## ❗ Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **"Python not found"** | Install Python from python.org (check "Add to PATH") |
| **"Permission denied" (macOS/Linux)** | Run `chmod +x Run.command Run.sh` |
| **"Download failed"** | Auto-retry 3 times automatically |
| **"URL not working"** | Check YouTube URL validity |
| **"Storage full"** | Clear space or change download folder in settings |

### Manual Recovery

```bash
# Manual installation if needed:
pip install yt-dlp
python Source/launcher.py
```

## 🔒 Privacy & Safety

### ✅ Safe & Secure

- **No Telemetry** - Doesn't send your data anywhere
- **No Ads** - Completely ad-free experience
- **Open Source** - Transparent code you can inspect
- **Local Processing** - Everything runs on your device
- **No Tracking** - No analytics or user tracking

### ⚠️ Legal Notice

This tool is designed for:

- Personal use and education
- Downloading content you own or have rights to
- Fair use purposes

Please respect:

- YouTube's Terms of Service
- Copyright laws  
- Content creators' rights

## 📈 Performance

### Download Features

- **Real-time Progress**: Live percentage, speed, and ETA display
- **Background Downloads**: Keep working while downloading
- **Playlist Support**: Batch download entire playlists
- **Resumable**: Continues interrupted downloads
- **Fast Processing**: Optimized audio/video conversion

### Resource Usage

- **CPU**: Low to moderate during processing
- **RAM**: Minimal footprint
- **Storage**: Efficient temporary file handling

## 🆘 Support

### Getting Help

1. **Double-check the setup instructions** above
2. **Verify your internet connection**
3. **Ensure sufficient storage space**
4. **Try restarting the application**

### Common Solutions

- **Restart the app** - Fixes most temporary issues
- **Check Python installation** - Ensure it's in PATH
- **Verify URLs** - Make sure YouTube links are valid
- **Storage permissions** - Ensure write access to download folder

## 🔄 Updates

### Keeping Updated

- **Application**: Download latest version from GitHub
- **Dependencies**: Launcher auto-updates packages
- **FFmpeg**: Automatically managed by the launcher

### Version Info

- **Current Version**: 3.0 (Universal Launcher)
- **Last Updated**: December 2024
- **yt-dlp Version**: Auto-updated to latest
- **FFmpeg**: Bundled (Windows) / Auto-downloaded (macOS/Linux)

## 📄 License

This project is provided for educational and personal use. Please use responsibly and respect all applicable laws and terms of service.

---

<div align="center">

## **🎉 Ready to Download?**

**Choose your platform and start downloading!**

*Windows users: Double-click `Run.bat`*  
*macOS users: Double-click `Run.command`*  
*Linux users: Double-click `Run.sh`*  

**All platforms:** Automatic setup • No technical knowledge required • One-click operation

[Report Issue](https://github.com/maiz-an/PRO-YouTube-Downloader/issues) • [Request Feature](https://github.com/maiz-an/PRO-YouTube-Downloader/issues/new?template=feature_request.md) • [View Source](https://github.com/maiz-an/PRO-YouTube-Downloader)

**✨ The easiest way to download YouTube videos - just double-click and go! ✨**

</div>
