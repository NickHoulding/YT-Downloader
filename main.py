################## ABOUT ############################
# Title:           Youtube Video Downloader
# Creator:         Nicholas Ian Houlding
# Version:         1.1


################## IMPORTS ##########################
from pytube import Playlist
from pytube import YouTube
from gui    import initGUI
import threading
import sys
import os


################## GLOBALS ##########################
T_LOCK      = threading.Lock()
FILE_FRMT   = "AUD+VID"
FILE_RES    = "1080p"
FILE_TYPE   = "mp4"
LINKS       = []


################## IMPLEMENTATION ###################
def main():
    initGUI()

def startDL():
    print("Download Started...")

# Start
if __name__ == "__main__":
    main()