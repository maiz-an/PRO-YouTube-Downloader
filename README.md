
# PRO YouTube Downloader 🎥➡️💾

<div align="center">

![YouTube Downloader](https://img.shields.io/badge/PRO-YouTube%20Downloader-red?style=for-the-badge&logo=youtube)
![Multi-Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Android%20%7C%20iOS-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6%2B-green?style=for-the-badge&logo=python)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-orange?style=for-the-badge&logo=ffmpeg)

**The Ultimate Cross-Platform YouTube Downloader with Smart Auto-Setup**

*Download videos, playlists, and audio from YouTube with one click!*

</div>

## ✨ Features

### 🎯 Download Options

- **🎬 Video Download** - Highest quality MP4
- **🎵 Audio Extraction** - MP3 320kbps
- **📚 Playlist Support** - Entire playlists automatically
- **🔧 Manual Selection** - Choose specific formats
- **⏳ Background Downloads** - Keep working while downloading

### 🤖 Smart Automation

- **🚀 One-Click Setup** - Automatic dependency installation
- **🛡️ Self-Healing** - Auto-retry and crash recovery
- **📦 Dependency Management** - Handles Python, FFmpeg, yt-dlp
- **🎯 Platform Detection** - Optimized for Windows, Android, iOS

### 💻 User Experience

- **🎨 Beautiful Interface** - Professional console UI with emojis
- **📊 Real-time Progress** - Animated spinner and progress bars
- **📝 Download History** - Track all your downloads
- **⚙️ Customizable Settings** - Multiple configuration options

## 🚀 Quick Start

### Choose Your Platform

| Platform | Launcher File | Requirements |
|----------|---------------|--------------|
| **🖥️ Windows** | `Run.bat` | Windows 10/11 |
| **📱 Android** | `RunAndroid.py` | Termux app |
| **📱 iOS** | `RunIOS.py` | Carnets app |

### Windows (Recommended)

1. **Download** the project folder
2. **Double-click** `Run.bat`
3. **Watch the magic** - everything installs automatically!
4. **Start downloading** - follow the intuitive menu

### Android

```bash
# In Termux:
python RunAndroid.py
```

### iOS

```bash
# In Carnets:
Run RunIOS.py
```

## 📁 Project Structure

```
PRO-YouTube-Downloader/
├── 🚀 Run.bat                 # Windows Launcher
├── 🚀 Run.py                  # MACOS/ Linux Launcher
├── 📱 RunAndroid.py           # Android Launcher
├── 📱 RunIOS.py               # iOS Launcher
├── 📖 README.md               # This file
├── 📁 Downloads/              # Downloaded files
└── 📁 Source/
    ├── 🐍 Downloader.py       # Main application
    └── ⚙️ refresh_env.bat     # Windows environment helper
```

## 🎮 How to Use

### Basic Usage

1. **Run the appropriate launcher** for your platform
2. **Select download type** from the menu:
   - `1` - Video (Best Quality)
   - `2` - Audio (MP3 320kbps)
   - `3` - Manual Format Selection
   - `4` - Settings
   - `5` - Download History
   - `6` - Exit

3. **Paste YouTube URL** when prompted
4. **Wait for completion** - watch the progress spinner
5. **Find your files** in the `Downloads` folder

### Advanced Features

- **📚 Playlists**: Paste playlist URL to download all videos
- **⚙️ Settings**: Change download folder, enable auto-retry
- **📊 History**: View your download history and status
- **🔄 Retry**: Automatic retry on failed downloads

## 🛠️ Technical Details

### Dependencies (Auto-Managed)

- **Python 3.6+** - Runtime environment
- **FFmpeg** - Audio/video processing  
- **yt-dlp** - Enhanced YouTube downloading
- **Required packages** - All automatically handled

### Supported Platforms

- **✅ Windows** (10, 11) - Full feature support
- **✅ Android** (Termux) - Full feature support
- **✅ iOS** (Carnets) - Full feature support
- **✅ macOS** - Basic functionality
- **✅ Linux** - Basic functionality

### Download Formats

- **Video**: MP4, WebM, MKV (best available)
- **Audio**: MP3 320kbps, M4A, Opus
- **Quality**: 144p to 4K (as available)
- **Codecs**: H.264, VP9, AV1

## 🤖 BOT Assistant

### 🎯 Automatic Setup

- **FFmpeg Setup** - Multiple installation options
- **Dependency Management** - Installs all required packages
- **Environment Configuration** - Sets up PATH and variables

### 🛡️ Smart Recovery

- **3 Retry Attempts** for failed installations
- **Crash Protection** - Auto-restarts on errors
- **Clear Error Messages** - Step-by-step guidance
- **Fallback Options** - Manual setup instructions

### 📊 System Verification

```
[1/4] 🔍 Checking Python installation...
[2/4] 🔧 Checking pip package manager... 
[3/4] 🎬 Checking FFmpeg installation...
[4/4] 📚 Installing Python dependencies...
```

## ❗ Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **"FFmpeg missing"** | Choose automatic installation |
| **"Download failed"** | Auto-retry 3 times |
| **"URL not working"** | Check YouTube URL validity |
| **"Storage full"** | Clear space or change download folder |

### Manual Recovery

```bash
# Manual installation if needed:
pip install yt-dlp
python Source/Downloader.py
```

## 🔒 Privacy & Safety

### ✅ Safe & Secure

- **No Telemetry** - Doesn't send your data anywhere
- **No Ads** - Completely ad-free experience
- **Open Source** - Transparent code you can inspect
- **Local Processing** - Everything runs on your device

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

### Download Speeds

- **Video**: Depends on your internet connection
- **Audio**: Typically faster than video
- **Playlists**: Parallel processing for multiple videos
- **Resumable**: Continues interrupted downloads

### Resource Usage

- **CPU**: Low to moderate during processing
- **RAM**: Minimal footprint
- **Storage**: Efficient temporary file handling

## 🆘 Support

### Getting Help

1. **Check the platform-specific README** files
2. **Verify your internet connection**
3. **Ensure sufficient storage space**
4. **Try restarting the application**

### Common Solutions

- **Restart the app** - Fixes most temporary issues
- **Check updates** - Ensure you have latest version
- **Verify URLs** - Make sure YouTube links are valid
- **Storage permissions** - Especially on mobile devices

## 🔄 Updates

### Keeping Updated

- **Application**: Download latest version
- **Dependencies**: Launchers auto-update packages
- **FFmpeg**: Manual update may be needed occasionally

### Version Info

- **Current Version**: 2.0
- **Last Updated**: ${new Date().toLocaleDateString()}
- **yt-dlp Version**: Auto-updated to latest

## 📄 License

This project is provided for educational and personal use. Please use responsibly and respect all applicable laws and terms of service.

---

<div align="center">

## **🎉 Ready to Download?**

**Choose your platform and start downloading!**

*Windows users: Double-click `Run.bat`*  
*MACOS/Linux users: Run `python Run.py` in terminal*  
*Android users: Run `python RunAndroid.py` in Termux*  
*iOS users: Run `RunIOS.py` in Carnets*

[Report Issue](https://github.com/maiz-an/PRO-YouTube-Downloader/issues) • [Request Feature](https://github.com/maiz-an/PRO-YouTube-Downloader/issues/new?template=feature_request.md) • [View Source](https://github.com/maiz-an/PRO-YouTube-Downloader)

</div>
