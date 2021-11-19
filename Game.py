from Classes.Monster import Monster
from Classes.Player import Player
from Classes.Item import Item
from tkinter import *
from PIL import ImageTk, Image
import Setup as char
from functools import partial
import json,os


"""
===============================================================
                       Key Binds
===============================================================
"""
def close_win(root):
    root.destroy()

def goToGame(frame,root):
    save()
    frame.pack_forget()
    gameFrame.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda e: close_win(root))

"""
===============================================================
                      Skill Frame
===============================================================
"""
def useSkill(skill,count,root):
    Char.useScroll(skill,count,Mon)
    update(root)
    text = "You did " + str(Char.getDmgDone()) + " Damage!"
    printSlow(text)
    playerAtkText = "ATK:" + str(Char.getAtk())
    if "Thunder Bolt" in skill:
        if "Common" in skill:
            text = "Your Attack has increased by "+ str(10)
            printSlow(text)
        elif "Normal" in skill:
            text = "Your Attack has increased by " + str(20)
            printSlow(text)
        elif "Rare" in skill:
            text = "Your Attack has increased by "+ str(30)
            printSlow(text)
    save()
    
            

def skill(root,previousFrame):
    gameFrame.pack_forget()
    skillList = {}
    useRedBtn = []
    useBlueBtn = []
    useGreenBtn = []
    itemID = 1
    x,y = 860 , 160 # Item Sprite cords
    x2,y2 = 960, 165 # Item name cords
    x3,y3 = 1050, 165
    x4,y4 = 0.58,0.136
    y5 = 160
    y6 = 0.15
    
    skillFrame = Frame(root)
    skillCanvas = Canvas(skillFrame,bg="#b1d0f2")
    skillText = skillCanvas.create_text(960,50,text="Scroll List",font=("Helvetica", 40),anchor='center')
    skillBox = skillCanvas.create_rectangle(300, 100, 1620, 800, fill="white",width=5, outline='black')
    
    # Render Scrolls Name
    redText = skillCanvas.create_text(370,130,text="Red Scrolls",font=("Helvetica", 20),anchor='w')  
    blueText = skillCanvas.create_text(900,130,text="Blue Scrolls",font=("Helvetica", 20),anchor='w')
    greenText = skillCanvas.create_text(1320,130,text="Blue Scrolls",font=("Helvetica", 20),anchor='w')   
    
    # Red Scrolls
    for key,value in Char.getRedSkill().items():
        text = skillCanvas.create_text(320,y5,text=key,font=("Helvetica", 15),anchor='w')
        countText = skillCanvas.create_text(600,y5,text=value,font=("Helvetica", 15),anchor='w')
        useRedBtn.append(Button(skillCanvas, text="USE",command=lambda key = key:useSkill(key,value,root),font=("Helvetica", 10)).place(x=630, y=y5-15))
        y5 += 30
    
    # Blue Scrolls
    y5 = 160
    for key,value in Char.getBlueSkill().items():
        text = skillCanvas.create_text(850,y5,text=key,font=("Helvetica", 15),anchor='w')
        countText = skillCanvas.create_text(1100,y5,text=value,font=("Helvetica", 15),anchor='w')
        useBlueBtn.append(Button(skillCanvas, text="USE",command=lambda key = key:useSkill(key,value,root),font=("Helvetica", 10)).place(x=1130, y=y5-15))
        y5 += 30
    
    # Green Scrolls
    y5 = 160   
    for key,value in Char.getGreenSkill().items():
        text = skillCanvas.create_text(1250,y5,text=key,font=("Helvetica", 15),anchor='w')
        countText = skillCanvas.create_text(1500,y5,text=value,font=("Helvetica", 15),anchor='w')
        useGreenBtn.append(Button(skillCanvas, text="USE",command=lambda key = key:useSkill(key,value,root),font=("Helvetica", 10)).place(x=1530, y=y5-15))
        y5 += 30
    
    backBtn = Button(skillCanvas,text=" Back ",font=("Helvetica", 15), command= lambda: back(skillFrame,previousFrame,root)).place(x=1530,y=735)
    
    skillFrame.pack(fill="both", expand=1)
    skillCanvas.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda x: back(skillFrame,previousFrame,root))

"""
===============================================================
                      End Frame
===============================================================
"""
def newGame(root,difficulty,endFrame):
    Char.setDifficulty(difficulty)
    genCanvas(root)
    new(root)
    endFrame.pack_forget()
    
def goToShop(root,endFrame):
    endFrame.pack_forget()
    shop(root,endFrame)
    
    
def endFrame(root):
    gameFrame.pack_forget()
    endFrame = Frame(root)
    endCanvas = Canvas(endFrame,bg="#b1d0f2")
    
    endText = "You defeated the monster " + str(Mon.getName()) + "!"
    
    endTextBox = endCanvas.create_text(960,200,text=endText,font=("Helvetica", 40),anchor='center')
    diffText = endCanvas.create_text(960,350,text="Choose difficultly!",font=("Helvetica", 40),anchor='center')

    easyBtn = Button(endCanvas, text="Easy",command=lambda:newGame(root,1,endFrame),width=30,font=("Helvetica", 15)).place(x=180, y=500)
    medBtn = Button(endCanvas, text="Medium",command=lambda:newGame(root,2,endFrame),width=30,font=("Helvetica", 15)).place(x=800, y=500)
    hardBtn = Button(endCanvas, text="Hard",command=lambda:newGame(root,3,endFrame),width=30,font=("Helvetica", 15)).place(x=1440, y=500)
    bossBtn = Button(endCanvas, text="BOSS",command=lambda:newGame(root,4,endFrame),width=30,font=("Helvetica", 15)).place(x=800, y=700)

    shopBtn = Button(endCanvas, text="SHOP",command=lambda:goToShop(root,endFrame),width=30,font=("Helvetica", 15)).place(x=180, y=700)
    saveBtn = Button(endCanvas, text="SAVE",command=lambda:save(),width=30,font=("Helvetica", 15)).place(x=800, y=900)
    statBtn = Button(endCanvas, text="STATS",command="",width=30,font=("Helvetica", 15)).place(x=1440, y=700)


    endFrame.pack(fill="both", expand=1)
    endCanvas.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda e: close_win(root))
    


"""
===============================================================
                      Bag Frame
===============================================================
"""
def useItem(itemName,playerHp,count,bagCanvas):
    if itemName == "Red Scroll":
        pass
    else:
        Char.useItem(itemName)
        
    playerHpText = "HP:" + str(Char.getCurrentHp()) + "/" + str(Char.getHp())
    gameCanvas.itemconfig(playerHp, text=playerHpText)
    bagCanvas.itemconfig(count, text=Char.getBag(itemName))
    save()
    

def bag(root,playerHp):
    global imgList
    gameFrame.pack_forget()
    item = Item()
    imgList = {}
    itemID = 1
    x,y = 860 , 160 # Item Sprite cords
    x2,y2 = 960, 165 # Item name cords
    x3,y3 = 1050, 165
    x4,y4 = 0.58,0.136

    bagFrame = Frame(root)
    bagCanvas = Canvas(bagFrame,bg="#b1d0f2")
    bagText = bagCanvas.create_text(960,50,text="Inventory",font=("Helvetica", 40),anchor='center')
    statBox = bagCanvas.create_rectangle(500, 100, 800, 800, fill="white",width=5, outline='black')
    bagBox = bagCanvas.create_rectangle(800, 100, 1360, 800, fill="white",width=5, outline='black')

    # Render item list
    for imgs in item.getItemList():
            img = PhotoImage(file = item.getItemPath(imgs)).subsample(4)
            imgList[img] = itemID
            bagCanvas.create_image(x, y, image=img)
            bagCanvas.create_text(x2,y2,text=item.getName(imgs),font=("Helvetica", 20))
            y += 80
            y2 += 80
            itemID += 1
    
    # Render item counts
    hpCount = bagCanvas.create_text(x3,y3,text=Char.getBag("Hp Potion"),font=("Helvetica", 20),anchor='center')
    mpCount = bagCanvas.create_text(x3,y3 + 80,text=Char.getBag("Mp Potion"),font=("Helvetica", 20),anchor='center')
    
    # Render Use Buttons
    hpUseBtn = Button(bagCanvas, text="USE",command=lambda:useItem("Hp Potion",playerHp,hpCount,bagCanvas),font=("Helvetica", 15)).place(relx=x4, rely=y4)
    mpUseBtn = Button(bagCanvas, text="USE",command=lambda:useItem("Mp Potion",playerHp,mpCount,bagCanvas),font=("Helvetica", 15)).place(relx=x4, rely=y4 + 0.07)
    
    # Render stats box
    statBox = bagCanvas.create_text(650,150,text="Stats",font=("Helvetica", 35),anchor='center')

    nameText = "Name:" + str(Char.getName())
    nameTextBox = bagCanvas.create_text(650,240,text=nameText,font=("Helvetica", 20),anchor='center')

    hpText = "Health: " + str(Char.getHp())
    hpTextBox = bagCanvas.create_text(650,290,text=hpText,font=("Helvetica", 20),anchor='center')

    atkText = "Attack: " + str(Char.getAtk())
    atkTextBox = bagCanvas.create_text(650,340,text=atkText,font=("Helvetica", 20),anchor='center')

    defText = "Armor: " + str(Char.getArmor())
    defTextBox = bagCanvas.create_text(650,390,text=defText,font=("Helvetica", 20),anchor='center')

    spdText = "Speed: " + str(Char.getSpd())
    spdTextBox = bagCanvas.create_text(650,440,text=spdText,font=("Helvetica", 20),anchor='center')
    
    luckText = "Luck: " + str(Char.getLuck())
    spdTextBox = bagCanvas.create_text(650,490,text=luckText,font=("Helvetica", 20),anchor='center')

    moneyText = "Money: " + str(Char.getMoney())
    moneyTextBox = bagCanvas.create_text(650,530,text=moneyText,font=("Helvetica", 20),anchor='center')

    bagFrame.pack(fill="both", expand=1)
    bagCanvas.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda e: goToGame(bagFrame,root))
    

"""
===============================================================
                      Shop Frame
===============================================================
"""
def back(frame,previousFrame,root):
    frame.pack_forget()
    previousFrame.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda e: close_win(root))
    
    
def buy(itemName,item,shopCanvas,moneyTextBox):
    if itemName == "Hp Potion":
        Char.buyItem("Hp Potion",20)
    elif itemName == "Mp Potion":
        Char.buyItem("Mp Potion",20)
    elif itemName == "Red Scroll":
        Char.buyScroll(Char,"Red Scroll",20)
    elif itemName == "Blue Scroll":
        Char.buyScroll(Char,"Blue Scroll",20)
    elif itemName == "Green Scroll":
        Char.buyScroll(Char,"Green Scroll",20)
    
    moneyText = "Money: " + str(Char.getMoney()) + "G"
    shopCanvas.itemconfig(moneyTextBox,text=moneyText)
    save()

def shop(root,previousFrame):
    global imgList, skillList
    item = Item()
    imgList = {}
    skillList = {}
    itemID = 1
    skillID = 1
    x,y = 650 , 160 # Item cords
    x2,y2 = 0.48, 0.135 #  Buy cords
    x3,y3 = 800, 165 # Item name cords
    gameFrame.pack_forget()
    shopFrame = Frame(root)
    shopCanvas = Canvas(shopFrame,bg="#b1d0f2")
    
    # Render Shop GUI
    shopText = shopCanvas.create_text(960,50,text="SHOP",font=("Helvetica", 40),anchor='center')
    shopBox = shopCanvas.create_rectangle(560, 100, 1360, 800, fill="white",width=5, outline='black')
    
    # Render items
    for imgs in item.getItemList():       
        img = PhotoImage(file = item.getItemPath(imgs)).subsample(4)
        imgList[img] = itemID
        shopCanvas.create_image(x, y, image=img)
        shopCanvas.create_text(x3,y3,text=item.getNameTag(imgs),font=("Helvetica", 20))
        y += 80
        y3 += 80
        itemID += 1
    
    for imgs in Char.getSkillList():       
        img = PhotoImage(file = Char.getSkillPath(imgs)).subsample(4)
        skillList[img] = skillID
        shopCanvas.create_image(x, y, image=img)
        shopCanvas.create_text(x3,y3,text = Char.getSkillTag(imgs,20),font=("Helvetica", 20))
        y += 80
        y3 += 80  
        skillID += 1
    
    # Render Money
    moneyText = "Money: " + str(Char.getMoney()) + "G"
    moneyTextBox = shopCanvas.create_text(960,760,text=moneyText,font=("Helvetica", 20))
       
    # Render Buy
    hpBtn = Button(shopCanvas,text=" Buy ",font=("Helvetica", 15), command= lambda: buy("Hp Potion",item,shopCanvas,moneyTextBox)).place(relx=x2, rely=y2)
    mpBtn = Button(shopCanvas,text=" Buy ",font=("Helvetica", 15), command= lambda: buy("Mp Potion",item,shopCanvas,moneyTextBox)).place(relx=x2, rely=y2 + 0.07)
    blueBtn = Button(shopCanvas,text=" Buy ",font=("Helvetica", 15), command= lambda: buy("Blue Scroll",item,shopCanvas,moneyTextBox)).place(relx=x2, rely=y2 + 0.145)
    greenBtn = Button(shopCanvas,text=" Buy ",font=("Helvetica", 15), command= lambda: buy("Green Scroll",item,shopCanvas,moneyTextBox)).place(relx=x2, rely=y2 + 0.22)
    redBtn = Button(shopCanvas,text=" Buy ",font=("Helvetica", 15), command= lambda: buy("Red Scroll",item,shopCanvas,moneyTextBox)).place(relx=x2, rely=y2 + 0.295)
    backBtn = Button(shopCanvas,text=" Back ",font=("Helvetica", 15), command= lambda: back(shopFrame,previousFrame,root)).place(x=1260,y=735)
    
    # Render Frame and Canvas
    shopFrame.pack(fill="both", expand=1)
    shopCanvas.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda x: back(shopFrame,previousFrame,root))

"""
===============================================================
                        Game Mechanics
===============================================================
"""


def update(root):
    monHpText = "HP: " + str(Mon.getCurrentHp()) + "/" + str(Mon.getHp())
    playerHpText = "HP:" + str(Char.getCurrentHp()) + "/" + str(Char.getHp())
    playerAtkText = "ATK:" + str(Char.getAtk())
    playerDefText = "Def:" + str(Char.getArmor())
    playerSpdText = "Spd:" + str(Char.getSpd())
    
    gameCanvas.itemconfig(monHp, text=monHpText)
    gameCanvas.itemconfig(playerHp, text=playerHpText)
    gameCanvas.itemconfig(playerAtk, text=playerAtkText)
    gameCanvas.itemconfig(playerDef, text=playerDefText)
    gameCanvas.itemconfig(playerSpd, text=playerSpdText)
    

def printSlow(myText):
    delta = 50
    delay = 0
    for x in range(len(myText)+1):
        s = myText[:x]
        newText = lambda s=s: gameCanvas.itemconfigure(gameText,text=s)
        gameCanvas.after(delay,newText)
        delay += delta


def attack(playerHp,root):
    if Mon.getCurrentHp() > 0:
        turn = Char.attack(Mon)
        
        # Change HP text
        monHpText = "HP: " + str(Mon.getCurrentHp()) + "/" + str(Mon.getHp())
        playerHpText = "HP:" + str(Char.getCurrentHp()) + "/" + str(Char.getHp())
        if turn == True:
            if Mon.getCurrentHp() <= 0:
                # text = "You defeated a " + str(Mon.getName()) + "!"
                # printSlow(text)
                money = 0
                stat = 0
                if Char.getDifficulty() == 1:
                    money = 20
                    stat = 2   
                elif Char.getDifficulty() == 2:
                    money = 40
                    stat = 4
                elif Char.getDifficulty() == 3:
                    money = 60
                    stat = 6
            else:
                dmgText = " - " + str(Char.getDmgDone())
                dmgBox = gameCanvas.create_text(1250,180, text=dmgText, fill="red", font=("Comic Sans MS", 36,"bold italic"))
                
                text = "You did " + str(Char.getDmgDone()) + " Damage!"
                printSlow(text)
                root.after(1000, gameCanvas.delete, dmgBox)       
        else:
            text = "You took " + str(Char.getDmgTaken()) + " Damage!"
            printSlow(text)
            if Char.getCurrentHp() <= 0:
                print("You are dead")
                root.destroy()
         
        gameCanvas.itemconfig(monHp, text=monHpText)
        gameCanvas.itemconfig(playerHp, text=playerHpText)
        
        print("Mon HP is ", Mon.getCurrentHp())
        print("Player HP is ", Char.getCurrentHp())
        print("================")
        moneyText = "You gained " + str(money) +"G and " + str(stat) + " stat point!"
        printSlow(moneyText)
    else:
        if Char.getDifficulty() == 1:
            Char.gainStat(1)
            Char.incMoney(20)

        elif Char.getDifficulty() == 2:
            Char.gainStat(2)
            Char.incMoney(40)

        elif Char.getDifficulty() == 3:
            Char.gainStat(3)
            Char.incMoney(60)
        
        elif Char.getDifficulty() == 4:
            Char.gainStat(5)
            Char.incMoney(100)
            
    save()
    update(root)
    endFrame(root)

def save():
    path = os.path.dirname(os.path.abspath(__file__)) + "/saves"
    with open("saves/data.json", "r") as jsonFile:
        data = json.load(jsonFile)
    
    data["currentHp"] = Char.getCurrentHp()
    data["stats"] = Char.getStats()
    data["bag"] = Char.getBagList()
    data["money"] = Char.getMoney()
    data["redSkills"] = Char.getRedSkill()
    data["blueSkills"] = Char.getBlueSkill()
    data["greenSkills"] = Char.getGreenSkill()
    
    with open("saves/data.json", "w") as jsonFile:
        json.dump(data, jsonFile,indent=4)
    
    jsonFile.close()
 

"""
===============================================================
                         Gen New Mon
===============================================================                  
"""

def genMon():
    global photo, Mon
    Mon = Monster(Char)
    photo = PhotoImage(file = Mon.genMonName())
    gameCanvas.create_image(950, 480, image=photo)


"""
=============================================================
               GAME GENERATION CODE
=============================================================
"""
def new(root):
    gameCanvas.delete("all")
    Mon = genMon()
    game(root)
    
def init_game(root):
    global Char
    genCanvas(root)
    Char = Player()
    genMon()
    game(root)

def genCanvas(root):
    global gameCanvas,gameFrame,Char
    gameFrame = Frame(root,bg="#000000")
    gameCanvas = Canvas(gameFrame,bg="#b1d0f2")

def game(root):
    global monHp,playerHp,playerAtk,playerDef,playerSpd,gameText
    
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
    playerHp = gameCanvas.create_text(1420,680,text=playerHpText,font=("Helvetica", 20),anchor='w')
    playerAtk = gameCanvas.create_text(1650,680,text=playerAtkText,font=("Helvetica", 20),anchor='w')
    playerDef = gameCanvas.create_text(1420,730,text=playerDefText,font=("Helvetica", 20),anchor='w')
    playerSpd = gameCanvas.create_text(1650,730,text=playerSpdText,font=("Helvetica", 20),anchor='w')

    # Render Game Message
    foundText = "You found " + Mon.getName() + "!"
    gameText = gameCanvas.create_text(560,930,text="",font=("Helvetica", 30))
    printSlow(foundText)

    atkBtn = Button(gameCanvas, text="ATK",command=lambda:attack(playerHp,root),width=10,border=5,font=("Helvetica", 20)).place(relx=0.65, rely=0.8)
    bagBtn = Button(gameCanvas, text="BAG",width=10,border=5,command=lambda:bag(root,playerHp),font=("Helvetica", 20)).place(relx=0.65, rely=0.9)
    skillbtn = Button(gameCanvas, text="SCROLL",width=10,border=5,command=lambda:skill(root,gameFrame),font=("Helvetica", 20)).place(relx=0.768, rely=0.8)
    runBtn = Button(gameCanvas, text="RUN",width=10,border=5,font=("Helvetica", 20)).place(relx=0.768, rely=0.9)
    saveBtn = Button(gameCanvas, text="Save",command=lambda:save(),width=10,height=4,border=5,font=("Helvetica", 20)).place(relx=0.89, rely=0.805)
    
    gameFrame.pack(fill="both", expand=1)
    gameCanvas.pack(fill="both", expand=1)
        
    root.bind('<Escape>', lambda e: close_win(root))
    root.bind('<F2>', lambda x :shop(root,gameFrame))
    root.bind('b', lambda x :bag(root,playerHp))