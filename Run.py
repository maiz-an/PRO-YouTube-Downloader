#!/usr/bin/env python3
"""
PRO YouTube Downloader - Universal Launcher
This file launches the main application from the Source folder
"""

import os
import sys
from pathlib import Path

def main():
    # Add Source directory to Python path
    source_dir = Path(__file__).parent / "Source"
    sys.path.insert(0, str(source_dir))
    
    try:
        from launcher import main as launcher_main
        launcher_main()
    except ImportError as e:
        print(f"❌ Error: Could not import from Source folder: {e}")
        print("📁 Please ensure all files are in the Source directory")
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()