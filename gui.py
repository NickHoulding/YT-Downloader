## Title:           Youtube Video Downloader
## Creator:         Nicholas Ian Houlding
## Version:         1.0

## IMPORTS
from tkinter import Text
from tkinter import Tk

## GLOBALS
W_HIG       = 800
W_WID       = 400
FONT        = "Roboto"

## COLORS
LGT_GRY     = "#272727"
GRY         = "#0F0F0F"
WHT         = "#FFFFFF"
RED         = "#FF0000"

## IMPLEMENTATION
def initGUI():
    root = Tk()
    root.title("YT Video Downloader")
    root.geometry(f"{W_HIG}x{W_WID}")
    root.configure(bg=LGT_GRY)

    text = Text(root, height=1, width=int(W_WID / 2), bg=LGT_GRY, fg=WHT, font=(FONT, 12))
    text.tag_configure("center", justify="center")
    text.pack()

    root.mainloop()