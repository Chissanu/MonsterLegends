from tkinter import *
from tkinter import font
import Setup as char
import Game as game
import os,pyglet
from pathlib import Path
from winsound import *
from PIL import Image, ImageTk

def click():
    global play
    print("Clicked")
    path = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\sound\\"
    clickSound = path + "click.wav"
    PlaySound(clickSound,SND_ASYNC)

def init_menu(root):
    global bg,startImg
    fontPath = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\Font\\alagard.ttf"
    pyglet.font.add_file(fontPath)
    start = Frame(root,bg="grey")
    load = Frame(root,bg="grey")   
    root.bind('<Escape>', lambda x:exit(root))
    
    path = Path(os.path.dirname(os.path.abspath(__file__)))
    
    # Loading image
    bg = PhotoImage(file = (str(path) + "\Assets\\background\Menu\main.png"))
    
    
    startCanvas = Canvas(root)
    
    
    # Background
    startBg = Label(startCanvas,image=bg, borderwidth=0).place(x=0,y=0)



    startBtd = Button(startCanvas,text="Start",font=("alagard", 40),command=lambda:change_to_start(root,startCanvas))
    startBtd.place(relx=0.5, rely=0.3, anchor="center")
    
    conBtd = Button(startCanvas,text="Continue",font=("alagard", 40),command=lambda:change_to_load(root,startCanvas))
    conBtd.place(relx=0.5, rely=0.5, anchor="center")
    
    exitBtd = Button(startCanvas,text="Exit",font=("alagard", 40),command=lambda:exit(root))
    exitBtd.place(relx=0.5, rely=0.7, anchor="center")
    
    font2 = font.Font(family='alagard', size='40')
    
    continueLabel = Label(load, text="WIP Please Wait", foreground="blue", font=font2)
    continueLabel.pack(pady=20)
    startCanvas.pack(fill="both", expand=1)
    
def change_to_start(root,startCanvas):
    click()
    startCanvas.pack_forget()
    char.init_Char(root)
    
def change_to_load(root,startCanvas):
    click()
    startCanvas.pack_forget()
    try:
        game.init_game(root)
    except:
        char.init_Char(root)
    
def exit(root):
    click()
    root.destroy()

    

