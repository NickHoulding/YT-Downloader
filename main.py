# ABOUT *****************************************
# Title:        Youtube Video Downloader
# Developer:    Nicholas Ian Houlding
# Version:      1.1

# IMPORTS ***************************************
from pytube import Playlist
from pytube import YouTube
from gui    import initGUI
import threading
import sys
import os

# GLOBALS ***************************************
LOCK        = threading.Lock()
FILE_FMT    = "AUD+VID"
FILE_RES    = "1080p"
FILE_TYP    = "mp4"
LINKS       = []

# IMPLEMENTATION ********************************
def main():
    initGUI()

def startDL():
    print("Download Started...")

# Start
if __name__ == "__main__":
    main()