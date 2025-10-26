# PRO YouTube Downloader 📱🎥➡️💾

A powerful YouTube downloader optimized for iOS with the same great features as the Windows version.

![YouTube Downloader](https://img.shields.io/badge/YouTube-Downloader-red) ![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![iOS](https://img.shields.io/badge/Platform-iOS-lightgrey)

## ✨ Features

- **📱 iOS Optimized**: Works perfectly on iPhone/iPad
- **🎯 Same Great Features** as Windows version:
  - 🎬 **Video**: Best quality MP4 download
  - 🎵 **Audio**: High-quality MP3 (320kbps)
  - 📂 **Playlist Support**: Download entire playlists
- **⏳ Real-time Progress**: Beautiful spinner animation
- **🛡️ Error Recovery**: Automatic retry and crash protection
- **🎨 Professional UI**: Beautiful interface with emojis

## 📁 Project Structure

```
PRO YouTube Downloader/
├── 📄 RunIOS.py                 # iOS launcher
├── 📄 RunAND.py                 # iOS launcher
├── 📄 Run.bat                   # Windows launcher
├── 📁 Downloads/                # Downloaded files folder
└── 📁 Source/
    ├── 🐍 Downloader.py          # Main Python application
    └── ⚙️ refresh_env.bat        # Environment helper
```

## 🚀 Quick Start for iOS

### Method 1: a-Shell (Free - Recommended)

1. **Install a-Shell** from App Store (free)
2. **Open a-Shell** and navigate to your folder:

   ```bash
   cd "/path/to/PRO YouTube Downloader"
   ```

3. **Run the iOS launcher**:

   ```bash
   python RunIOS.py
   ```

4. **Follow the setup** - it handles everything automatically!

### Method 2: Carnets (Free - Jupyter)

1. **Install Carnets** from App Store (free)
2. **Open Carnets** and create new notebook
3. **Install yt-dlp** in first cell:

   ```python
   !pip install yt-dlp
   ```

4. **Run the downloader** in next cells

## 📱 iOS Setup Guide

### Step 1: Get Your Files on iPhone

**Option A - Cloud Transfer:**

- Upload folder to iCloud Drive
- Save to "PRO YouTube Downloader" folder

**Option B - Direct Download:**

```bash
# In a-Shell, download directly:
curl -O https://your-url/RunIOS.py
curl -O https://your-url/Source/Downloader.py
```

### Step 2: Run the Application

**In a-Shell:**

```bash
# Navigate to your folder
cd "PRO YouTube Downloader"

# Run the iOS launcher
python RunIOS.py
```

### Step 3: Start Downloading

The app will:

1. ✅ **Auto-setup** dependencies
2. ✅ **Create folders** if needed
3. ✅ **Launch downloader** automatically

## 🎮 How to Use

### Starting the Application

1. **Run** `python RunIOS.py` in a-Shell
2. **Watch the setup** complete automatically:

   ```
   [1/3] 🔍 Checking Python installation...
   [2/3] 📚 Checking Python dependencies...
   [3/3] 🎬 Checking FFmpeg installation...
   ```

3. **Application launches** when ready

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
2. **Paste YouTube URL** - video OR playlist
3. **Watch progress spinner**: `⏳ Downloading... |/-\`
4. **Get completion message**: `✅ Download Completed Successfully`
5. **Find your file** in the `Downloads` folder

## 📂 File Locations

**Downloads are saved in:**

- a-Shell: App's Documents folder
- Carnets: Notebook directory

**To access downloaded files:**

- Use **Share** button in a-Shell
- Save to Photos or Files app

## 🛠️ iOS-Specific Tips

### Best Practices

- **Use Wi-Fi** for large downloads
- **Keep app open** during downloads
- **MP3 files** are smaller - perfect for mobile
- **Check storage** before large playlists

### a-Shell Commands

```bash
# List files
ls

# Check storage space
df -h

# Navigate to downloads
cd Downloads
ls -la
```

## ❗ Troubleshooting

### Common iOS Issues

| Issue | Solution |
|-------|----------|
| **"Module not found"** | Run `pip install yt-dlp` |
| **"Permission denied"** | Use `python RunIOS.py` |
| **Download stops** | Keep a-Shell app open |
| **Storage full** | Delete old files, use MP3 |

### Quick Fixes

1. **Restart a-Shell** app
2. **Reinstall yt-dlp**: `pip install yt-dlp --upgrade`
3. **Check internet connection**
4. **Ensure enough storage space**

## 🔄 Cross-Platform Compatibility

**Same features as Windows version:**

- ✅ Identical download options
- ✅ Same folder structure
- ✅ Identical user interface
- ✅ Same error handling
- ✅ Playlist support

**Files work between platforms:**

- Download on iOS → Transfer to Windows
- Same project structure on both platforms

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

### Getting Help

1. **Check folder structure** is correct
2. **Ensure a-Shell** is updated
3. **Try different YouTube URL**
4. **Use Wi-Fi connection**

### Success Message

When everything works, you'll see:

```
✅ All systems ready! Launching PRO YouTube Downloader...
📁 Downloads will be saved in: /Downloads
```

---

**Enjoy YouTube downloads on your iPhone!** 🚀

*Perfect companion to the Windows version*
