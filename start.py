import Menu as menu
import Game as game
from tkinter import *
from pathlib import Path
from winsound import *
from PIL import ImageTk, Image
import os,pyglet

running = True

root = Tk()
root.title("Monster Legends")
root.geometry("1920x1080")
root.configure(bg="#000000")
root.attributes('-fullscreen',True)

# Music
# path = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\sound\\"
# bgSound = path + "menu.wav"
# PlaySound(bgSound,SND_ASYNC | SND_NOSTOP)

mainicon = PhotoImage(file = 'logo.png')
root.iconphoto(True, mainicon)

if running:
    menu.init_menu(root)
    #game.init_game(root)
    root.mainloop()

