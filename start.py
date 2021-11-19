import Menu as menu
import Game as game
from tkinter import *

running = True

root = Tk()
root.title("Text Adventure")
root.geometry("1920x1080")
root.configure(bg="#000000")
root.attributes('-fullscreen',True)

if running:
    #menu.init_menu(root)
    game.init_game(root)
    root.mainloop()

