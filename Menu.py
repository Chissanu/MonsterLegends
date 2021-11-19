from tkinter import *
from tkinter import font
import Setup as char
import os
from pathlib import Path
from PIL import Image, ImageTk


def init_menu(root):
    global bg,startImg
    start = Frame(root,bg="grey")
    load = Frame(root,bg="grey")   
    root.bind('<Escape>', lambda x:exit(root))
    
    path = Path(os.path.dirname(os.path.abspath(__file__)))
    
    # Loading image
    bg = PhotoImage(file = (str(path) + "\Assets\\background\main.png"))
    
    
    startCanvas = Canvas(root)
    
    
    # Background
    startBg = Label(startCanvas,image=bg, borderwidth=0).place(x=0,y=0)



    startBtd = Button(startCanvas,text="Start",font=("Helvetica", 40),command=lambda:change_to_start(root,startCanvas))
    startBtd.place(relx=0.5, rely=0.3, anchor="center")
    
    conBtd = Button(startCanvas,text="Continue",font=("Helvetica", 40),command=change_to_load)
    conBtd.place(relx=0.5, rely=0.5, anchor="center")
    
    exitBtd = Button(startCanvas,text="Exit",font=("Helvetica", 40),command=lambda:exit(root))
    exitBtd.place(relx=0.5, rely=0.7, anchor="center")
    
    font2 = font.Font(family='Helvetica', size='40')
    
    continueLabel = Label(load, text="WIP Please Wait", foreground="blue", font=font2)
    continueLabel.pack(pady=20)
    startCanvas.pack(fill="both", expand=1)
    
def change_to_start(root,startCanvas):
    startCanvas.pack_forget()
    char.init_Char(root)
    
def change_to_load():
    pass
    # load.pack(fill='both', expand=1)
    # start.pack_forget()
    
def exit(root):
    root.destroy()

    

