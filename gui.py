# ABOUT *****************************************
# Title:        Youtube Video Downloader
# Developer:    Nicholas Ian Houlding
# Version:      1.1

# IMPORTS ***************************************
from tkinter import OptionMenu
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import Text
from tkinter import Tk
import tkinter

# GLOBALS ***************************************
NAME        = "YT Downloader"
VERS        = "v1.1"
WIDTH       = 800
HEIGHT      = 400

# FONT ******************************************
FONT_REG    = "Roboto"
FONT_LGT    = "Roboto Light"
FONT_BOLD   = "Roboto Bold"
HEADING_SZ  = 32
SUBHEAD_SZ  = 16
BODY_SZ     = 10

# COLORS ****************************************
OFF_WHT     = "#AAAAAA"
LGT_GRY     = "#272727"
GRY         = "#0F0F0F"
WHT         = "#FFFFFF"
RED         = "#FF0000"

# CUSTOM WIDGETS ********************************
class OptionMenuPlaceholder(tkinter.OptionMenu):
    from tkinter import StringVar as Tk
    def __init__(self, master, placeholder, *options):
        self.var = tkinter.StringVar(master)
        self.var.set(placeholder)
        super().__init__(master, self.var, *options)

# INITIALIZATION ********************************
# Initializes the GUI and all its components.
def initGUI():
    # Root
    root = Tk()
    Root(root)

    # Frames
    main_frame = tkinter.Frame(root)
    mainFrame(main_frame)

    # Heading
    head_frame = tkinter.Frame(main_frame)
    headFrame(head_frame)
    head = Label(head_frame, text=NAME)
    Head(head)
    sub_head = Label(head_frame, text=VERS)
    subHead(sub_head)

    # Controls
    ctrl_frame = tkinter.Frame(main_frame)
    ctrlFrame(ctrl_frame)
    entry = Entry(ctrl_frame)
    entryBox(entry)
    dd_frame = tkinter.Frame(ctrl_frame)
    dropdownFrame(dd_frame)
    ftype_label = OptionMenuPlaceholder(dd_frame, "File Type", "mp4", "webm", "3pg")
    fileTypeDropdown(ftype_label)
    fform_label = OptionMenuPlaceholder(dd_frame, "File Format", "Audio", "Video", "Both")
    fileFormatDropdown(fform_label)
    res_label = OptionMenuPlaceholder(dd_frame, "Resolution", "1080p", "720p", "480p")
    resolutionDropdown(res_label)
    dl_btn = Button(dd_frame, text="Download")
    downloadButton(dl_btn)

    # Disclaimer
    disc_frame = tkinter.Frame(main_frame)
    discFrame(disc_frame)
    disc_title = Label(disc_frame, text="DISCLAIMER:")
    discHead(disc_title)
    disc_body = Label(disc_frame, text="The developer of this software is not responsible for any acquisitions of copyrighted or personal material. Use at your own risk.")
    discBody(disc_body)

    # Run
    root.mainloop()


# CUSTOMIZATION *********************************
# These customize their respective GUI parts.
def Root(root):
    root.title("YT Downloader")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.resizable(False, False)
    root.configure(bg=GRY)

def mainFrame(main_frame):
    main_frame.configure(background=GRY)
    main_frame.pack(fill="both", expand=True, padx=25, pady=25)

def headFrame(head_frame):
    head_frame.configure(height=200)
    head_frame.configure(background=RED)
    head_frame.configure(borderwidth=0, highlightthickness=0)
    head_frame.pack(side="top", fill="x")

def Head(head):
    head.configure(font=(FONT_BOLD, HEADING_SZ))
    head.configure(fg=WHT, bg=GRY)
    head.configure(borderwidth=0, highlightthickness=0)
    head.pack(fill="x", side="top")

def subHead(sub_head):
    sub_head.configure(font=(FONT_LGT, SUBHEAD_SZ))
    sub_head.configure(fg=WHT, bg=GRY)
    sub_head.configure(borderwidth=0, highlightthickness=0)
    sub_head.pack(fill="x", side="bottom")

def ctrlFrame(ctrl_frame):
    ctrl_frame.configure(background=GRY)
    ctrl_frame.configure(borderwidth=0, highlightthickness=0)
    ctrl_frame.pack(fill="x", expand=True)

def entryBox(entry):
    entry.configure(font=(FONT_REG, SUBHEAD_SZ))
    entry.configure(fg=WHT, bg=LGT_GRY, insertbackground=OFF_WHT)
    entry.configure(borderwidth=0, highlightthickness=0)
    entry.pack(fill="x", expand=True, padx=25, pady=20, anchor="center")

def dropdownFrame(dd_frame):
    dd_frame.configure(background=GRY)
    dd_frame.configure(borderwidth=0, highlightthickness=0)
    dd_frame.pack(fill="both", expand=True, padx=25, pady=20, anchor="center")

def fileTypeDropdown(ftype_label):
    ftype_label.configure(font=(FONT_REG, BODY_SZ))
    ftype_label.configure(fg=WHT, bg=LGT_GRY, activebackground=OFF_WHT, activeforeground=GRY)
    ftype_label.configure(width=10, borderwidth=0, highlightthickness=0)
    ftype_label.pack(side="left", expand=True, anchor="center")

def fileFormatDropdown(fform_label):
    fform_label.configure(font=(FONT_REG, BODY_SZ))
    fform_label.configure(fg=WHT, bg=LGT_GRY, activebackground=OFF_WHT, activeforeground=GRY)
    fform_label.configure(width=10, borderwidth=0, highlightthickness=0)
    fform_label.pack(side="left", expand=True, anchor="center")

def resolutionDropdown(res_label):
    res_label.configure(font=(FONT_REG, BODY_SZ))
    res_label.configure(fg=WHT, bg=LGT_GRY, activebackground=OFF_WHT, activeforeground=GRY)
    res_label.configure(width=10, borderwidth=0, highlightthickness=0)
    res_label.pack(side="left", expand=True, anchor="center")

def downloadButton(dl_btn):
    dl_btn.configure(font=(FONT_REG, BODY_SZ))
    dl_btn.configure(fg=WHT, bg=LGT_GRY, activebackground=OFF_WHT, activeforeground=GRY)
    dl_btn.configure(width=10, height=1, borderwidth=0, highlightthickness=0)
    dl_btn.pack(side="right", expand=True, anchor="center")
    
    # Button actions
    dl_btn.bind("<Enter>", lambda e: dl_btn.configure(bg=OFF_WHT, fg=GRY))
    dl_btn.bind("<Leave>", lambda e: dl_btn.configure(bg=LGT_GRY, fg=WHT))
    from main import startDL
    dl_btn.bind("<Button-1>", lambda e: startDL())

def discFrame(disc_frame):
    disc_frame.configure(height=200)
    disc_frame.configure(background=RED)
    disc_frame.configure(borderwidth=0, highlightthickness=0)
    disc_frame.pack(side="bottom", fill="x")

def discHead(disc_title):
    disc_title.configure(font=(FONT_BOLD, BODY_SZ))
    disc_title.configure(fg=OFF_WHT, bg=GRY)
    disc_title.configure(justify="center")
    disc_title.configure(borderwidth=0, highlightthickness=0)
    disc_title.pack(side="top", fill="x")

def discBody(disc_body):
    disc_body.configure(font=(FONT_LGT, BODY_SZ))
    disc_body.configure(fg=OFF_WHT, bg=GRY)
    disc_body.configure(justify="center")
    disc_body.configure(borderwidth=0, highlightthickness=0)
    disc_body.pack(side="bottom", fill="x")