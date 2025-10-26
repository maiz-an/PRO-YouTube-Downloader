# PRO YouTube Downloader 🎥➡️💾

A BOT-powered YouTube downloader with an intuitive console interface that automatically handles all dependencies and setup requirements.

![YouTube Downloader](https://img.shields.io/badge/YouTube-Downloader-red) ![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-green) ![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey)

## ✨ Features

- **🎯 Smart Auto-Setup**: BOT-powered dependency installation
- **📥 Multiple Download Modes (also playlist)**:
  - 🎬 **Video**: Best quality MP4 download
  - 🎵 **Audio**: High-quality MP3 (320kbps)
  - 🔧 **Manual**: Custom format selection
- **⏳ Real-time Progress**: Beautiful spinner animation
- **🛡️ Error Recovery**: Automatic retry and crash protection
- **📁 Organized Structure**: Clean separation of source and downloads
- **🎨 Professional UI**: Beautiful console interface with emojis

## 📁 Project Structure

```
PRO YouTube Downloader/
├── 📄 Run.bat                    # Main launcher (BOT Assistant)
├── 📁 Downloads/                 # Downloaded files folder
└── 📁 Source/
    ├── 🐍 Downloader.py          # Main Python application
    └── ⚙️ refresh_env.bat        # Environment helper
```

## 🚀 Quick Start

### Method 1: One-Click Setup (Recommended)

1. **Download** the entire `Mainfolder` to your computer
2. **Double-click** `Run.bat`
3. **Follow the BOT Assistant** - it will handle everything automatically!

### Method 2: Manual Setup

```bash
# 1. Install Python 3.6+ from python.org
# 2. Install FFmpeg and add to PATH
# 3. Run manually:
cd Mainfolder/Source
pip install yt-dlp
python Downloader.py
```

## 🔧 System Requirements

- **Windows** 10 or later
- **Python** 3.6 or higher (auto-installed)
- **FFmpeg** (auto-installed if missing)
- **Internet connection** for downloads and setup

## 🤖 BOT Assistant Features

The `Run.bat` acts as your personal BOT assistant:

### 🎯 Smart Dependency Management

- **Python Detection**: Automatically checks for Python installation
- **Auto-Install**: Downloads and installs Python if missing
- **PATH Management**: Handles environment variables automatically

### 🛠️ FFmpeg Setup

- **Multiple Options**:
  - ✅ Automatic portable installation
  - 📥 Download with instructions
  - ℹ️ Manual installation guide

### 🔄 Intelligent Error Handling

- **Retry Logic**: 3 automatic retries for failed installations
- **Crash Recovery**: Auto-restarts on application crashes
- **Clear Guidance**: Step-by-step instructions for manual setup

### 📦 Dependency Verification

- **Pip Management**: Upgrades pip to latest version
- **Package Installation**: Installs and verifies yt-dlp
- **Environment Setup**: Ensures all components work together

## 🎮 How to Use

### Starting the Application

1. **Double-click** `Run.bat` in the Mainfolder
2. **Watch the BOT Assistant** set up everything automatically:

   ```
   [1/4] 🔍 Checking Python installation...
   [2/4] 🔧 Checking pip package manager...
   [3/4] 🎬 Checking FFmpeg installation...
   [4/4] 📚 Installing Python dependencies...
   ```

3. **Application launches** automatically when ready

### Using the Downloader

```
╔══════════════════════════════════════════════╗
║            🚀 PRO YT Downloader 🚀          ║
║           Premium YouTube Downloader         ║
╚══════════════════════════════════════════════╝

✨ Welcome to PRO YouTube Downloader ✨
📁 Download location: F:\MVs

═══════════════════════════════════════════════════════
            🎯 DOWNLOAD OPTIONS
═══════════════════════════════════════════════════════
1. 📹 Download Video (Best Quality)
2. 🎵 Download Audio MP3 (320kbps)
3. 🔧 Manual Select Format
4. ⚙️  Settings
5. 📊 Download History
6. ❌ Exit
═══════════════════════════════════════════════════════
📁 Current Download Folder: F:\MVs
═══════════════════════════════════════════════════════
Select an option (1-6):

```

### Download Process

1. **Select mode** (1, 2, . . . 6)
2. **Paste YouTube URL** when prompted
3. **Watch progress spinner**: `⏳ Downloading... |/-\`
4. **Get completion message**: `✅ Download Completed Successfully`
5. **Find your file** in the `Downloads` folder

## 📂 Output Structure

After downloading, your files will be organized as:

```
PRO YouTube Downloader/
├── Run.bat
├── Downloads/
│   ├── Your_Video_Title.mp4
│   ├── Your_Audio_Title.mp3
│   └── ...
└── Source/
    ├── Downloader.py
    └── refresh_env.bat
```

## 🛠️ Technical Details

### Dependencies (Auto-Managed)

- **yt-dlp**: Enhanced YouTube downloader
- **FFmpeg**: Audio/video processing
- **Python 3.6+**: Runtime environment

### Key Features Preserved

- ✅ **All original download options**
- ✅ **Progress spinner animations**
- ✅ **Error handling and retry logic**
- ✅ **Beautiful console interface**
- ✅ **Multiple format support**

## ❗ Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Python not found"** | BOT Assistant will auto-install it |
| **"FFmpeg missing"** | Choose automatic portable installation |
| **"Download failed"** | Application auto-retries 3 times |
| **"Script not found"** | Ensure folder structure is intact |
| **"Permission denied"** | Run as Administrator if needed |

### Manual Recovery Steps

If the BOT Assistant fails:

1. **Install Python manually** from [python.org](https://python.org)
2. **Install FFmpeg** from [ffmpeg.org](https://ffmpeg.org)
3. **Run manually**:

   ```cmd
   cd Mainfolder\Source
   pip install yt-dlp
   python Downloader.py
   ```

## 🔄 Updates & Maintenance

### Keeping Dependencies Updated

The BOT Assistant automatically checks for updates, but you can manually update:

```cmd
pip install --upgrade yt-dlp
```

### Application Updates

- Replace entire `Mainfolder` with new version
- Your `Downloads` folder and files remain safe
- All settings and preferences preserved

## ⚠️ Legal & Ethical Usage

This tool is designed for:

- ✅ Personal use and education
- ✅ Downloading content you own
- ✅ Fair use purposes

Please respect:

- 📜 YouTube's Terms of Service
- ©️ Copyright laws
- 👨‍💻 Content creators' rights

## 🆘 Support

### Quick Fixes

1. **Restart the application** - BOT Assistant will re-check everything
2. **Check internet connection** - Required for downloads and setup
3. **Verify folder structure** - Ensure all files are in correct locations

### Getting Help

If issues persist:

1. Check that all files are in the correct folder structure
2. Ensure Windows is updated
3. Try running as Administrator
4. Check antivirus isn't blocking the application

## 🎉 Success Message

When everything works perfectly, you'll see:

```
✅ All systems ready! Starting PRO YouTube Downloader...
📁 Downloads will be saved in: G:\Mainfolder\Downloads
```

---

**Enjoy seamless, BOT-powered YouTube downloads!** 🚀

*Last updated: ${new Date().toLocaleDateString()}*
