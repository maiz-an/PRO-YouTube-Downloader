#!/bin/bash
cd "$(dirname "$0")"

echo "════════════════════════════════════════════════════════════════"
echo "                   PRO YouTube Downloader"
echo "════════════════════════════════════════════════════════════════"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found! Please install Python from:"
    echo "   https://python.org"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo "🚀 Starting PRO YouTube Downloader..."
echo ""
python3 "Source/launcher.py"

# If application exits, pause to show any messages
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Application exited with an error"
    read -p "Press Enter to exit..."
fi