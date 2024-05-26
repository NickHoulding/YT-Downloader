# ABOUT *****************************************
# Title:        Youtube Video Downloader
# Developer:    Nicholas Ian Houlding
# Version:      1.1

# IMPORTS ***************************************
from pytube import Playlist
from pytube import YouTube
from gui import getFileFormat
from gui import getResolution
from gui import getFileType
from gui import getEntry
from gui import disableUI
from gui import enableUI
from gui import initGUI
import datetime
import threading
import sys
import os

# GLOBALS ***************************************
LOCK        = threading.Lock()
MAX_THREADS = 25
FILE_FMT    = [None]
FILE_RES    = [None]
FILE_TYP    = [None]
LINKS       = []

# IMPLEMENTATION ********************************
def main():
    initGUI()

def startDL():
    disableUI()

    lnk = getEntry()
    typ = getFileType()
    fmt = getFileFormat()

    if fmt == "Audio":
        res = None
    else:
        res = getResolution()

    valid = validateLink(lnk)
    if valid:
        LOCK.acquire()
        FILE_RES[0] = res
        FILE_TYP[0] = typ
        FILE_FMT[0] = fmt
        LOCK.release()

        os.chdir(os.path.expanduser("~") + "/Downloads")
        dirName = "YTDL_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        WORKING_DIR = os.path.join(os.getcwd(), dirName)
        os.mkdir(WORKING_DIR)
        os.chdir(WORKING_DIR)

        launchThreads()

    enableUI()

def validateLink(lnk):
    result = True
    
    # Video
    if lnk.startswith("https://www.youtube.com/watch?v=") or lnk.startswith("https://youtu.be/"):
        try:
            yt = YouTube(lnk)
            if yt.streams == []:
                result = False
            else:
                LOCK.acquire()
                LINKS.append(lnk)
                LOCK.release()
        except:
            result = False

    # Playlist
    elif lnk.startswith("https://www.youtube.com/playlist?list=") or lnk.startswith("https://youtube.com/playlist?list="):
        try:
            pl = Playlist(lnk)
            if pl.video_urls == []:
                result = False
            else:
                LOCK.acquire()
                for link in pl.video_urls:
                    LINKS.append(link)
                LOCK.release()
        except:
            result = False
    
    # Neither
    else:
        result = False

    return result

def launchThreads():
    while len(LINKS) > 0:
        threads = []
        numLinks = len(LINKS)

        if numLinks > MAX_THREADS:
            numLinks = MAX_THREADS

        LOCK.acquire()

        for i in range(numLinks):
            t = threading.Thread(target=download, args=(LINKS[i], FILE_FMT[0], FILE_RES[0], FILE_TYP[0]))
            threads.append(t)
            t.start()

        LOCK.release()

        for t in threads:
            t.join()

def download(link, fmt, res, typ):
    LOCK.acquire()
    LINKS.remove(link)

    yt = YouTube(link)

    if fmt == "Audio":
        stream = yt.streams.filter(only_audio=True).first()
    elif fmt == "Video":
        stream = yt.streams.filter(only_video=True).first()
    else:
        stream = yt.streams.filter(file_extension=typ).first()
    
    stream.download()

    LOCK.release()

# Start
if __name__ == "__main__":
    main()