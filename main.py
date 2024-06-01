# ABOUT *****************************************
# Title:        Youtube Video Downloader
# Developer:    Nicholas Ian Houlding
# Version:      1.1

# IMPORTS ***************************************
from pytube import Playlist
from pytube import YouTube
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
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
import re

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

    LOCK.acquire()
    lnk = getEntry()
    FILE_TYP[0] = getFileType()
    FILE_FMT[0] = getFileFormat()
    FILE_RES[0] = getResolution()
    LOCK.release()

    valid = validateLink(lnk)

    if valid:
        # desktop
        os.chdir(os.path.expanduser("~") + "/Desktop")
        dirName = "YTDL_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        WORKING_DIR = os.path.join(os.getcwd(), dirName)
        os.mkdir(WORKING_DIR)
        os.chdir(WORKING_DIR)

        launchThreads()

    enableUI()


def validateLink(lnk):
    result = True
    
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
    else:
        result = False

    return result


def launchThreads():
    numLinks = len(LINKS)

    while numLinks > 0:
        threads = []

        if numLinks > MAX_THREADS:
            numLinks = MAX_THREADS

        LOCK.acquire()
        for i in range(numLinks):
            t = threading.Thread(target=download, args=(LINKS[i], FILE_FMT[0], FILE_RES[0], FILE_TYP[0]))
            threads.append(t)
            t.start()
            numLinks -= 1
        LOCK.release()

        for t in threads:
            t.join()


def download(lnk, fmt, res, typ):
    LOCK.acquire()
    LINKS.remove(lnk)
    LOCK.release()

    yt = YouTube(lnk)

    if fmt == "Audio":
        audio_codec = set_audio_codec(typ)
        audio_stream = yt.streams.filter(file_extension=typ, only_audio=True).first()
        audio_path = audio_stream.download()
        audio = AudioFileClip(audio_path)
        filename = sanitize_filename(yt.title) + "." + typ
        audio.write_audiofile(filename=filename, codec=audio_codec)
        os.remove(audio_path)

    elif fmt == "Video":
        video_codec = set_video_codec(typ)
        video_stream = yt.streams.filter(file_extension=typ, only_video=True).first()
        video_path = video_stream.download()
        video = VideoFileClip(video_path)
        filename = sanitize_filename(yt.title) + "." + typ
        video.write_videofile(filename=filename, codec=video_codec)
        os.remove(video_path)

    else:
        video_codec = set_video_codec(typ)
        audio_codec = set_audio_codec(typ)
        video_stream = yt.streams.filter(file_extension=typ, only_video=True).first()
        video_path = video_stream.download()
        video = VideoFileClip(video_path)
        audio_stream = yt.streams.filter(file_extension=typ, only_audio=True).first()
        audio_path = audio_stream.download()
        audio = AudioFileClip(audio_path)
        final = video.set_audio(audio)
        filename = sanitize_filename(yt.title) + "." + typ
        final.write_videofile(filename=filename, codec=video_codec, audio_codec=audio_codec)
        os.remove(video_path)
        os.remove(audio_path)


def set_audio_codec(typ):
    if typ == "mp4":
        return "aac"
    elif typ == "webm":
        return "opus"
    elif typ == "3gp":
        return "amr_nb"

    
def set_video_codec(typ):
    if typ == "mp4":
        return "libx264"
    elif typ == "webm":
        return "libvpx"
    elif typ == "3gp":
        return "libx264"


def sanitize_filename(filename):
    return re.sub(r'[^\w\s-]', '', filename).strip()


if __name__ == "__main__":
    main()