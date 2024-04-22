## Title:           Youtube Video Downloader
## Creator:         Nicholas Ian Houlding
## Version:         1.0

## IMPORTS
from tkinter import Label
from tkinter import Text
from tkinter import Tk
import tkinter

## GLOBALS
W_HIG       = 1000
W_WID       = 500
FONT_REG    = "Roboto"
FONT_LGT    = "Roboto Light"
FONT_BOLD   = "Roboto Bold"
HEADING_SZ  = 24
SUBHEAD_SZ  = 14
BODY_SZ     = 10

## COLORS
LGT_GRY     = "#272727"
GRY         = "#0F0F0F"
WHT         = "#FFFFFF"
RED         = "#FF0000"

## IMPLEMENTATION
def initGUI():
    root = Tk()
    root.title("YT Downloader")
    root.geometry(f"{W_HIG}x{W_WID}")
    root.resizable(False, False)
    root.configure(bg=GRY)

    ## Frame
    frame = tkinter.Frame(root, background=GRY, width=W_WID, height=W_HIG)
    frame.pack(fill="both", expand=True, padx=25, pady=25)

    ## Heading
    heading = Label(frame, text="YT Downloader", font=(FONT_BOLD, HEADING_SZ), fg=WHT, bg=GRY, foreground=WHT)
    heading.pack()

    ## Subheading
    subheading = Label(frame, text="Version 1.0", font=(FONT_LGT, SUBHEAD_SZ), fg=WHT, bg=GRY)
    subheading.pack(padx=10)

    ## Input
    txtbox = Text(frame, font=(FONT_REG, BODY_SZ), fg=WHT, bg=LGT_GRY, width=50, height=1, highlightcolor=GRY)
    txtbox.pack(padx=20, pady=20)
    txtbox.place(relx=0.5, rely=0.3, anchor="center")

    ## Disclaimer
    body = Label(frame, text="DISCLAIMER: The developer of this software is not responsible for any acquisitions of copyrighted or personal material. Use at your own risk.", font=(FONT_LGT, BODY_SZ), fg=WHT, bg=GRY, width=W_WID, height=6, justify="center")
    body.pack(padx=10, pady=20)
    body.place(relx=0.5, rely=0.95, anchor="center")

    root.mainloop()