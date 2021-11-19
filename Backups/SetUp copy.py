from tkinter import *
from typing import Sized
   
def createChar(root):
    x1, y1, x2, y2 = 130,150,270,180

    create = Frame(root,bg="#000000")
    label1 = Label(create, text="Create Character",foreground="cyan",bg="#318beb",font=("Helvetica", 40))
    label1.pack(pady=20)
    
    # Create Canvas for character creation
    charCreateMenu = Canvas(create, bg="#b1d0f2",height=600,width=400)
    charCreateMenu.create_window(200,100)
    charCreateName = Entry(root,width=12,font=("Calibri 41"), justify='center')
    charCreateMenu.create_window(200, 80, window=charCreateName)
    
    #charCreateMenu.create_rectangle(150, 170, 268, 151,width=50, fill="white")
    charCreateMenu.create_rectangle(x1, y1, x2, y2,width=30, fill="#000000")
    
    charCreateMenu.pack()
    create.pack(fill="both", expand=1)


    
        