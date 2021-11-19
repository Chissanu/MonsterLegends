from Classes.Monster import Monster
from Classes.Player import Player
from tkinter import *
from PIL import ImageTk, Image  

def close_win(root):
    root.destroy()

def attack(Char,Mon,monHp,gameText,playerHp,gameCanvas):
    if Mon.getCurrentHp() > 0:
        turn = Char.attack(Mon)
        monHpText = "HP: " + str(Mon.getCurrentHp()) + "/" + str(Mon.getHp())
        playerHpText = "HP:" + str(Char.getCurrentHp()) + "/" + str(Char.getHp())
        if turn == True:
            if Mon.getCurrentHp() <= 0:
                text = "You defeat " + str(Mon.getName()) + " !"
                gameCanvas.itemconfig(gameText, text=text)
            else:
                text = "You did " + str(Char.getDmgDone()) + " Damage!"
                gameCanvas.itemconfig(gameText, text=text)
            
        else:
            text = "You took " + str(Char.getDmgTaken()) + " Damage!"
            gameCanvas.itemconfig(gameText, text=text)
            
        gameCanvas.itemconfig(monHp, text=monHpText)
        gameCanvas.itemconfig(playerHp, text=playerHpText)
        
        # print("Mon HP is ", Mon.getCurrentHp())
        # print("Player HP is ", Char.getCurrentHp())
        # print("================")
    else:
        text = "You defeat " + str(Mon.getName()) + " !"
        
        gameCanvas.itemconfig(gameText, text=text)
        # print("Monster is dead")

def genMon(Char,gameCanvas):
    global photo
    Mon = Monster(Char)
    print(Mon.getPlayerStats())
    photo = PhotoImage(file = Mon.genMonName())
    gameCanvas.create_image(950, 480, image=photo)
    return Mon

def genChar():
    Char = Player()
    return Char

def init_game(root):
    gameCanvas = Canvas(root,bg="#b1d0f2")
    Char = genChar()
    Mon = genMon(Char,gameCanvas)
    textBox = gameCanvas.create_rectangle(5, 800, 1195, 1075, fill="#ffffff",width=5, outline='blue')
    ActionBox = gameCanvas.create_rectangle(1200, 800, 1915, 1075, fill="#000000",width=5, outline='red')

    # Render enemy's health
    monHpBox = gameCanvas.create_rectangle(5, 5, 500, 200, fill="#ffffff",width=5, outline='blue')

    # Generate Mon Stats
    monHpText = "HP: " + str(Mon.getCurrentHp()) + "/" + str(Mon.getHp())
    monAtkText = "ATK: " + str(Mon.getAtk())
    monDefText = "Def: " + str(Mon.getArmor())
    monSpdText = "Spd: " + str(Mon.getSpd())

    monName = gameCanvas.create_text(250,50,text=(Mon.getName()),font=("Helvetica", 30))
    monHp = gameCanvas.create_text(64,100,text=monHpText,font=("Helvetica", 20),anchor='w')
    monAtk = gameCanvas.create_text(64,150,text=monAtkText,font=("Helvetica", 20),anchor='w')
    monDef = gameCanvas.create_text(280,100,text=monDefText,font=("Helvetica", 20),anchor='w')
    monSpd = gameCanvas.create_text(280,150,text=monSpdText,font=("Helvetica", 20),anchor='w')


    # Render Character's health
    playerHpBox = gameCanvas.create_rectangle(1400, 600, 1915, 795, fill="#ffffff",width=5, outline='blue')

    # Generate Player stats
    playerHpText = "HP:" + str(Char.getCurrentHp()) + "/" + str(Char.getHp())
    playerAtkText = "ATK:" + str(Char.getAtk())
    playerDefText = "Def:" + str(Char.getArmor())
    playerSpdText = "Spd:" + str(Char.getSpd())

    playerName = gameCanvas.create_text(1650,640,text=(Char.getName()),font=("Helvetica", 30))
    playerHp = gameCanvas.create_text(1500,680,text=playerHpText,font=("Helvetica", 20))
    playerAtk = gameCanvas.create_text(1750,680,text=playerAtkText,font=("Helvetica", 20))
    playerDef = gameCanvas.create_text(1460,730,text=playerDefText,font=("Helvetica", 20))
    playerSpd = gameCanvas.create_text(1755,730,text=playerSpdText,font=("Helvetica", 20))


    # Render Game Message
    text = "You found " + Mon.getName()
    gameText = gameCanvas.create_text(560,930,text=text,font=("Helvetica", 30))


    atkButton = Button(gameCanvas, text="ATK",command=lambda:attack(Char,Mon,monHp,gameText,playerHp,gameCanvas),width=10,border=5,font=("Helvetica", 20)).place(relx=0.65, rely=0.8)
    skillButton = Button(gameCanvas, text="SKILL",width=10,border=5,font=("Helvetica", 20)).place(relx=0.65, rely=0.9)
    BagButton = Button(gameCanvas, text="BAG",width=10,border=5,font=("Helvetica", 20)).place(relx=0.768, rely=0.8)
    RunButton = Button(gameCanvas, text="RUN",width=10,border=5,font=("Helvetica", 20)).place(relx=0.768, rely=0.9)
    AllInButton = Button(gameCanvas, text="All In",width=10,height=4,border=5,font=("Helvetica", 20)).place(relx=0.89, rely=0.805)

    gameCanvas.pack(fill="both", expand=1)
        
    root.bind('<Escape>', lambda e: close_win(root))