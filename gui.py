# ABOUT *****************************************
# Title:        Youtube Video Downloader
# Developer:    Nicholas Ian Houlding
# Version:      1.1

# IMPORTS ***************************************
from customtkinter import *

from tkinter import OptionMenu
from tkinter import PhotoImage
from tkinter import Button
from tkinter import Image
from tkinter import Label
from tkinter import Entry
from tkinter import Text
from tkinter import Tk

from PIL import ImageTk
from PIL import Image

import threading
import tkinter

# GLOBALS ***************************************
NAME        = "YT Downloader"
VERS        = "v1.1"
WIDTH       = 800
HEIGHT      = 400
CONTROLS    = []
ENTRY       = []
DL_BTN      = []
LOCK        = threading.Lock()
LINK        = [None]
FORMAT      = [None]
RESOLUTION  = [None]
FILETYPE    = [None]

# FONT ******************************************
FONT_REG    = "Roboto"
FONT_LGT    = "Roboto Light"
FONT_BOLD   = "Roboto Bold"
TITLE_SZ    = 32
HEAD_SZ     = 18
SUBH_SZ     = 14
BODY_SZ     = 12
SMALL_SZ    = 10

# COLORS ****************************************
OFF_WHT     = "#D9D9D9"
LGT_GRY     = "#272727"
GRY         = "#0F0F0F"
WHT         = "#FFFFFF"
RED         = "#FF0000"

# INITIALIZATION ********************************
def initGUI():
    # Root
    root = CTk()
    Root(root)

    # Frames
    main_frame = tkinter.Frame(root)
    mainFrame(main_frame)

    # Heading
    head_frame = tkinter.Frame(main_frame)
    headFrame(head_frame)
    # Logo
    logo_img = Image.open("YTDL_Logo.png")
    logo = CTkImage(light_image=logo_img, dark_image=logo_img)
    Logo(head_frame, logo)
    head = Label(head_frame, text=NAME)
    Head(head)
    sub_head = Label(head_frame, text=VERS)
    subHead(sub_head)

    # Controls
    ctrl_frame = tkinter.Frame(main_frame)
    ctrlFrame(ctrl_frame)
    entry = CTkEntry(ctrl_frame)
    entryBox(entry)
    dd_frame = tkinter.Frame(ctrl_frame)
    dropdownFrame(dd_frame)
    ftype_label = CTkComboBox(master=dd_frame, values=["mp4", "webm", "3pg"])
    fileTypeDropdown(ftype_label)
    res_label = CTkComboBox(master=dd_frame, values=["1080p", "720p", "480p", "360p"])
    resolutionDropdown(res_label)
    fform_label = CTkComboBox(master=dd_frame, values=["Both", "Audio", "Video"])
    fileFormatDropdown(fform_label, res_label)
    dl_btn = CTkButton(dd_frame, text="Download")
    downloadButton(dl_btn, entry)

    # Disclaimer
    disc_frame = tkinter.Frame(main_frame)
    discFrame(disc_frame)
    disc_title = Label(disc_frame, text="DISCLAIMER:")
    discHead(disc_title)
    disc_body = Label(disc_frame, text="The developer of this software is not responsible for any acquisitions of copyrighted or personal material. Use at your own risk.")
    discBody(disc_body)

    # Append Controls
    LOCK.acquire()
    CONTROLS.append(ftype_label)
    CONTROLS.append(res_label)
    CONTROLS.append(fform_label)
    ENTRY.append(entry)
    DL_BTN.append(dl_btn)
    LOCK.release()

    # Run
    root.mainloop()

# GUI SAFEGUARDING ******************************
def disableUI():
    LOCK.acquire()
    for ctrl in CONTROLS:
        ctrl.configure(state="disabled")

    LINK[0] = ENTRY[0].get()
    FORMAT[0] = CONTROLS[2].get()
    RESOLUTION[0] = CONTROLS[1].get()
    FILETYPE[0] = CONTROLS[0].get()
    
    ENTRY[0].delete(0, "end")
    ENTRY[0].configure(state="disabled")

    DL_BTN[0].configure(text="Downloading...")
    DL_BTN[0].configure(state="disabled")
    LOCK.release()

def enableUI():
    LOCK.acquire()
    for ctrl in CONTROLS:
        ctrl.configure(state="readonly")
    
    ENTRY[0].configure(state="normal")
    
    DL_BTN[0].configure(text="Download")
    DL_BTN[0].configure(state="normal")
    LOCK.release()

# GETTER METHODS ********************************
def getEntry():
    return LINK[0]

def getFileType():
    return FILETYPE[0]

def getResolution():
    return RESOLUTION[0]

def getFileFormat():
    return FORMAT[0]

# CUSTOMIZATION *********************************
def Root(root):
    root.iconbitmap("YTDL_Icon.ico")
    root.title("YT Downloader")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.resizable(False, False)

def mainFrame(main_frame):
    main_frame.configure(background=GRY)
    main_frame.pack(fill="both", expand=True, ipadx=25, ipady=25)

def headFrame(head_frame):
    head_frame.configure(height=200)
    head_frame.configure(background=GRY)
    head_frame.configure(borderwidth=0, highlightthickness=0)
    head_frame.pack(side="top", fill="x")

def Logo(head_frame, logo):
    logo.configure(size=(50, 50))
    logo_label = CTkLabel(head_frame, image=logo, text=None, height=50)
    logo_label.pack(side="top", fill="x", expand=True, anchor="center", pady=(35, 0))

def Head(head):
    head.configure(font=(FONT_BOLD, TITLE_SZ))
    head.configure(fg=WHT, bg=GRY)
    head.configure(borderwidth=0, highlightthickness=0)
    head.pack(fill="x", side="top")

def subHead(sub_head):
    sub_head.configure(font=(FONT_REG, SUBH_SZ))
    sub_head.configure(fg=WHT, bg=GRY)
    sub_head.configure(borderwidth=0, highlightthickness=0)
    sub_head.pack(fill="x", side="bottom")

def ctrlFrame(ctrl_frame):
    ctrl_frame.configure(background=GRY)
    ctrl_frame.configure(borderwidth=0, highlightthickness=0)
    ctrl_frame.pack(fill="x", expand=True)

def entryBox(entry):
    entry.configure(font=(FONT_BOLD, TITLE_SZ))
    entry.configure(fg_color=LGT_GRY, text_color=WHT, border_color=LGT_GRY)
    entry.configure(corner_radius=7)
    entry.pack(fill="x", expand=True, padx=40, pady=(20, 15), anchor="center")

def dropdownFrame(dd_frame):
    dd_frame.configure(background=GRY)
    dd_frame.configure(borderwidth=0, highlightthickness=0)
    dd_frame.pack(fill="both", expand=True, padx=40, pady=20, anchor="center")

def fileTypeDropdown(ftype_label):
    ftype_label.configure(font=(FONT_BOLD, HEAD_SZ))
    ftype_label.configure(dropdown_font=(FONT_BOLD, SUBH_SZ))
    ftype_label.configure(fg_color=GRY, border_color=LGT_GRY, dropdown_fg_color=GRY, button_color=LGT_GRY, button_hover_color=GRY, dropdown_hover_color=LGT_GRY, text_color=WHT)
    ftype_label.configure(border_width=3, justify="center")
    ftype_label.configure(state="readonly")
    ftype_label.pack(side="left", fill="x", expand=True, padx=(0, 25), anchor="center")

def resolutionDropdown(res_label):
    res_label.configure(font=(FONT_BOLD, HEAD_SZ))
    res_label.configure(dropdown_font=(FONT_BOLD, SUBH_SZ))
    res_label.configure(fg_color=GRY, border_color=LGT_GRY, dropdown_fg_color=GRY, button_color=LGT_GRY, button_hover_color=GRY, dropdown_hover_color=LGT_GRY, text_color=WHT)
    res_label.configure(border_width=3, justify="center")
    res_label.configure(state="readonly")
    res_label.pack(side="left", fill="x", expand=True, padx=25, anchor="center")

def fileFormatDropdown(fform_label, res_label):
    fform_label.configure(font=(FONT_BOLD, HEAD_SZ))
    fform_label.configure(dropdown_font=(FONT_BOLD, SUBH_SZ))
    fform_label.configure(fg_color=GRY, border_color=LGT_GRY, dropdown_fg_color=GRY, button_color=LGT_GRY, button_hover_color=GRY, dropdown_hover_color=LGT_GRY, text_color=WHT)
    fform_label.configure(border_width=3, justify="center")
    fform_label.configure(state="readonly")

    state = res_label.get()
    def checkState(choice):
        nonlocal state
        
        if fform_label.get() == "Audio":
            if res_label.get() != "N/A":
                state = res_label.get()
            
            res_label.set("N/A")
            res_label.configure(state="disabled")
        else:
            res_label.configure(state="normal")
            
            if res_label.get() == "N/A":
                res_label.set(state)
            
            res_label.configure(state="readonly")

    fform_label.configure(command=checkState)
    fform_label.pack(side="left", fill="x", expand=True, padx=25, anchor="center")

def downloadButton(dl_btn, entryBox):
    dl_btn.configure(font=(FONT_BOLD, HEAD_SZ))
    dl_btn.configure(fg_color=WHT, hover_color=OFF_WHT, text_color=GRY)
    from main import startDL
    dl_btn.configure(command=startDL)
    dl_btn.configure(state="normal")
    dl_btn.pack(side="left", padx=(25, 0), expand=True, anchor="center")

def discFrame(disc_frame):
    disc_frame.configure(height=200)
    disc_frame.configure(background=GRY)
    disc_frame.configure(borderwidth=0, highlightthickness=0)
    disc_frame.pack(side="bottom", fill="x")

def discHead(disc_title):
    disc_title.configure(font=(FONT_REG, SMALL_SZ))
    disc_title.configure(fg=OFF_WHT, bg=GRY)
    disc_title.configure(justify="center")
    disc_title.configure(borderwidth=0, highlightthickness=0)
    disc_title.pack(side="top", fill="x")

def discBody(disc_body):
    disc_body.configure(font=(FONT_LGT, SMALL_SZ))
    disc_body.configure(fg=OFF_WHT, bg=GRY)
    disc_body.configure(justify="center")
    disc_body.configure(borderwidth=0, highlightthickness=0)
    disc_body.pack(pady=(0, 35), side="bottom", fill="x")