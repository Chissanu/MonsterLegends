from Classes.Monster import Monster
from Classes.Player import Player
from Classes.Item import Item
import Setup as char
import Menu as menu
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
from winsound import *
import pygame as pg
import json,os,time,random, math,pyglet


"""
===============================================================
                       Sound Effects
===============================================================
"""

def bgMusic():
    path = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\sound\\"
    bgSound = path + "menu.wav"
    bg = pg.mixer.Sound(bgSound)
    bg.play()

def click():
    global play
    path = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\sound\\"
    clickSound = path + "click.wav"
    click = pg.mixer.Sound(clickSound)
    click.play()

def attackSound(turn):
    global play
    path = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\sound\\"
    if turn == "Mon":
        attackSound = path + "hit.wav"
        atkSound = pg.mixer.Sound(attackSound)
        atkSound.play()
    else:
        turn == "Player"
        hurtingSound = path + "hurt.wav"
        hurtSound = pg.mixer.Sound(hurtingSound)
        hurtSound.play()

"""
===============================================================
                       Key Binds
===============================================================
"""
def close_win(root):
    click()
    root.destroy()
        
"""
===============================================================
                      Skill Frame
===============================================================
"""
def useSkill(spell,count,root):
    click()
    Char.useScroll(spell,count,Mon)
    update(root)
    text = "You did " + str(Char.getDmgDone()) + " Damage!"
    printSlow(text)
    playerAtkText = "ATK:" + str(Char.getAtk())
    if "Thunder Bolt" in spell:
        if "Common" in spell:
            text = "Your Attack has increased by "+ str(10)
            printSlow(text)
        elif "Normal" in spell:
            text = "Your Attack has increased by " + str(20)
            printSlow(text)
        elif "Rare" in spell:
            text = "Your Attack has increased by "+ str(30)
            printSlow(text)
    save()
    skillFrame.pack_forget()
    skill(root,gameFrame)

def skill(root,previousFrame):
    global countText,skillCanvas,skillFrame
    gameFrame.pack_forget()
    click()
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
    skillText = skillCanvas.create_text(960,50,text="Scroll List",font=("alagard", 40),anchor='center')
    skillBox = skillCanvas.create_rectangle(300, 100, 1620, 800, fill="white",width=5, outline='black')
    
    # Render Scrolls Name
    redText = skillCanvas.create_text(370,130,text="Red Scrolls",font=("alagard", 20),anchor='w')  
    blueText = skillCanvas.create_text(900,130,text="Blue Scrolls",font=("alagard", 20),anchor='w')
    greenText = skillCanvas.create_text(1320,130,text="Blue Scrolls",font=("alagard", 20),anchor='w')   
    
    # Red Scrolls
    for key,value in Char.getRedSkill().items():
        text = skillCanvas.create_text(320,y5,text=key,font=("alagard", 15),anchor='w')
        countText = skillCanvas.create_text(600,y5,text=value,font=("alagard", 15),anchor='w')
        useRedBtn.append(Button(skillCanvas, text="USE",command=lambda key = key:useSkill(key,value,root),font=("alagard", 10)).place(x=630, y=y5-15))
        y5 += 30
    
    # Blue Scrolls
    y5 = 160
    for key,value in Char.getBlueSkill().items():
        text = skillCanvas.create_text(850,y5,text=key,font=("alagard", 15),anchor='w')
        countText = skillCanvas.create_text(1100,y5,text=value,font=("alagard", 15),anchor='w')
        useBlueBtn.append(Button(skillCanvas, text="USE",command=lambda key = key:useSkill(key,value,root),font=("alagard", 10)).place(x=1130, y=y5-15))
        y5 += 30
    
    # Green Scrolls
    y5 = 160   
    for key,value in Char.getGreenSkill().items():
        text = skillCanvas.create_text(1250,y5,text=key,font=("alagard", 15),anchor='w')
        countText = skillCanvas.create_text(1500,y5,text=value,font=("alagard", 15),anchor='w')
        useGreenBtn.append(Button(skillCanvas, text="USE",command=lambda key = key:useSkill(key,value,root),font=("alagard", 10)).place(x=1530, y=y5-15))
        y5 += 30
    
    backBtn = Button(skillCanvas,text=" Back ",font=("alagard", 15), command= lambda: back(skillFrame,previousFrame,root)).place(x=1530,y=735)
    skillFrame.pack(fill="both", expand=1)
    skillCanvas.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda x: back(skillFrame,previousFrame,root))
    
"""
===============================================================
                       Death Scene
===============================================================
"""
def goToMenu(root):
    deathFrame.pack_forget()
    menu.init_menu(root)
    
def death(root):
    global text,bg,deathFrame
    gameFrame.pack_forget()
    
    deathFrame = Frame(root)
    deathCanvas = Canvas(deathFrame,bg="#b1d0f2")
    
    deathPath = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\sound\\dead.wav"
    
    deathSound = pg.mixer.Sound(deathPath)
    deathSound.play()
    
    bgPath = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\background\\Menu\\death.png"
    textPath = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\fancyText\\gameOver.png"
    
    bg = PhotoImage(file = bgPath)
    overBg = deathCanvas.create_image(960, 540, image=bg)
    
    text = PhotoImage(file = textPath)
    overText = deathCanvas.create_image(960, 340, image=text)
    
    startAgain = Button(deathCanvas,text="START AGAIN",command=lambda:goToMenu(root),font=("alagard", 40)).place(x=780,y=750)
    
    deathFrame.pack(fill="both", expand=1)
    deathCanvas.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda e: close_win(root))


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

def goToStats(root,endFrame):
    endFrame.pack_forget()
    update(Mon)
    addPoint(root,endFrame)
  
def endGame(root):
    global endFrame, endCanvas , bg
    gameFrame.pack_forget()
    endFrame = Frame(root)
    endCanvas = Canvas(endFrame,bg="#b1d0f2")
    
    Char.removeBuff(Mon)
    
    path = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\background\Menu\\"
    
    bgLink = str(path) + "end.png"
    bg = PhotoImage(file = bgLink)
    startBg = endCanvas.create_image(960, 540, image=bg)

    if Mon.getCurrentHp() > 0:
        endText = "You teleported away from " + str(Mon.getName()) + "!"
    else:
        endText = "You defeated the " + str(Mon.getName()) + "!"
    
    endTextBox = endCanvas.create_text(964,204,text=endText,font=("alagard", 40),fill="blue",anchor='center')
    endTextBox_fg = endCanvas.create_text(960,200,text=endText,font=("alagard", 40),fill="white",anchor='center')
    endCanvas.tag_raise(endTextBox_fg,endTextBox)
    
    diffText = endCanvas.create_text(1664,344,text="Choose difficultly!",font=("alagard", 40),fill="blue",anchor='center')
    diffText_fg = endCanvas.create_text(1660, 340, text="Choose difficultly!", font=("alagard", 40), fill='white')
    endCanvas.tag_raise(diffText_fg,diffText)

    easyBtn = Button(endCanvas, text="Easy",command=lambda:newGame(root,1,endFrame),width=30,font=("alagard", 15)).place(x=1500, y=400)
    medBtn = Button(endCanvas, text="Medium",command=lambda:newGame(root,2,endFrame),width=30,font=("alagard", 15)).place(x=1500, y=480)
    hardBtn = Button(endCanvas, text="Hard",command=lambda:newGame(root,3,endFrame),width=30,font=("alagard", 15)).place(x=1500, y=560)
    bossBtn = Button(endCanvas, text="BOSS",command=lambda:newGame(root,4,endFrame),width=30,font=("alagard", 15)).place(x=1500, y=640)
    shopBtn = Button(endCanvas, text="SHOP",command=lambda:goToShop(root,endFrame),width=30,font=("alagard", 15)).place(x=1500, y=720)
    statBtn = Button(endCanvas, text="STATS",command=lambda:goToStats(root,endFrame),width=30,font=("alagard", 15)).place(x=1500, y=800)
    saveBtn = Button(endCanvas, text="SAVE",command=lambda:save(),width=30,font=("alagard", 15)).place(x=1500, y=880)
    exitBtn = Button(endCanvas, text="EXIT",command=lambda:close_win(root),width=30,font=("alagard", 15)).place(x=1500, y=960)

    endFrame.pack(fill="both", expand=1)
    endCanvas.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda e: close_win(root))
    


"""
===============================================================
                      Bag Frame
===============================================================
"""
def useItem(itemName,root):
    click()
    Char.useItem(itemName)
    if itemName == "Portal Warp":
        bagFrame.pack_forget()
        endGame(root)
    elif itemName == "Hp Potion":
        bagCanvas.itemconfig(hpCount,text=Char.getBag("Hp Potion"))
    elif itemName == "Sus Potion":
        bagCanvas.itemconfig(susCount,text=Char.getBag("Sus Potion"))
     
    save()
    
def bag(root,playerHp,previousFrame):
    global imgList,bagFrame, bagCanvas, hpCount,susCount,warpCount
    gameFrame.pack_forget()
    item = Item()
    imgList = {}
    useBtn = []
    itemID = 1
    x,y = 860 , 160 # Item Sprite cords
    x2,y2 = 960, 165 # Item name cords
    x3,y3 = 1050, 165
    x4,y4 = 0.58,0.136
    click()
    bagFrame = Frame(root)
    bagCanvas = Canvas(bagFrame,bg="#b1d0f2")
    bagText = bagCanvas.create_text(960,50,text="Inventory",font=("alagard", 40),anchor='center')
    statBox = bagCanvas.create_rectangle(500, 100, 800, 800, fill="white",width=5, outline='black')
    bagBox = bagCanvas.create_rectangle(800, 100, 1360, 800, fill="white",width=5, outline='black')

    # Render item list
    for imgs in item.getItemList():
            img = PhotoImage(file = item.getItemPath(imgs)).subsample(4)
            imgList[img] = itemID
            bagCanvas.create_image(x, y, image=img)
            bagCanvas.create_text(x2,y2,text=item.getName(imgs),font=("alagard", 20))
            y += 80
            y2 += 80
            itemID += 1
    
    # Render item counts
    hpCount = bagCanvas.create_text(x3,y3,text=Char.getBag("Hp Potion"),font=("alagard", 20),anchor='center')
    susCount = bagCanvas.create_text(x3,y3 + 160,text=Char.getBag("Sus Potion"),font=("alagard", 20),anchor='center')
    warpCount = bagCanvas.create_text(x3,y3 + 80,text=Char.getBag("Portal Warp"),font=("alagard", 20),anchor='center')
    
    # Render Use Buttons
    for i in item.getItemList():
        useBtn.append(Button(bagCanvas, text="USE",command=lambda i = i:useItem(i[:-4],root),font=("alagard", 15)).place(relx=x4, rely=y4))
        y4 += 0.075
    
    # Render stats box
    statBox = bagCanvas.create_text(650,150,text="Stats",font=("alagard", 35),anchor='center')

    nameText = "Name:" + str(Char.getName())
    nameTextBox = bagCanvas.create_text(650,240,text=nameText,font=("alagard", 20),anchor='center')

    hpText = "Health: " + str(Char.getHp())
    hpTextBox = bagCanvas.create_text(650,290,text=hpText,font=("alagard", 20),anchor='center')

    atkText = "Attack: " + str(Char.getAtk())
    atkTextBox = bagCanvas.create_text(650,340,text=atkText,font=("alagard", 20),anchor='center')

    defText = "Armor: " + str(Char.getArmor())
    defTextBox = bagCanvas.create_text(650,390,text=defText,font=("alagard", 20),anchor='center')

    spdText = "Speed: " + str(Char.getSpd())
    spdTextBox = bagCanvas.create_text(650,440,text=spdText,font=("alagard", 20),anchor='center')
    
    luckText = "Luck: " + str(Char.getLuck())
    spdTextBox = bagCanvas.create_text(650,490,text=luckText,font=("alagard", 20),anchor='center')

    moneyText = "Money: " + str(Char.getMoney())
    moneyTextBox = bagCanvas.create_text(650,530,text=moneyText,font=("alagard", 20),anchor='center')
    
    backBtn = Button(bagCanvas,text=" Back ",font=("alagard", 15), command= lambda: back(bagFrame,previousFrame,root)).place(x=1260,y=740)
    bagFrame.pack(fill="both", expand=1)
    bagCanvas.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda e: back(bagFrame,previousFrame,root))
    
"""
===============================================================
                      Stat Frame
===============================================================
"""
def increase(stat,charCreateMenu,remainStatsBox,textBox):
    click()
    if Char.getStats() >= 1:
        Char.setStats("dec",1)
        remainStatsText = "Remaining:" + str(Char.getStats())
        charCreateMenu.itemconfig(remainStatsBox, text=remainStatsText)
        if stat == "hp":     
            Char.setHp("inc",1)
            hpText = "Health:" + str(Char.getHp())
            charCreateMenu.itemconfig(textBox, text=hpText)
            print("Increase HP by One")
        elif stat == "atk":     
            Char.setAtk("inc",1)
            atkText = "Attack:" + str(Char.getAtk())
            charCreateMenu.itemconfig(textBox, text=atkText)
            print("Increase Attack by One")
        elif stat == "armor":     
            Char.setArmor("inc",1)
            defText = "Defend:" + str(Char.getArmor())
            charCreateMenu.itemconfig(textBox, text=defText)
            print("Increase armor by One")
        elif stat == "spd":     
            Char.setSpd("inc",1)
            spdText = "Speed:" + str(Char.getSpd())
            charCreateMenu.itemconfig(textBox, text=spdText)
            print("Increase speed by One")
        elif stat == "luck":     
            Char.setLuck("inc",1)
            luckText = "Luck:" + str(Char.getSpd())
            charCreateMenu.itemconfig(textBox, text=luckText)
            print("Increase speed by One")    
    else:
        print("No more stats")
    save()
        
def decrease(stat,charCreateMenu,remainStatsBox,textBox):
    click()
    if stat == "hp":
        if Char.getHp() > 1:
            Char.setStats("inc",1)  
            Char.setHp("dec",1)
            hpText = "Health:" + str(Char.getHp())
            charCreateMenu.itemconfig(textBox, text=hpText)
            print("Decrease HP by One")
    elif stat == "atk":
        if Char.getAtk() > 1:
            Char.setAtk("dec",1)
            Char.setStats("inc",1)
            atkText = "Attack:" + str(Char.getAtk())
            charCreateMenu.itemconfig(textBox, text=atkText)
            print("Decrease Attack by One")
    elif stat == "armor":
        if Char.getArmor() > 1:
            Char.setStats("inc",1)
            Char.setArmor("dec",1)
            defText = "Defend:" + str(Char.getArmor())
            charCreateMenu.itemconfig(textBox, text=defText)
            print("Decrease Armor by One")
    elif stat == "spd":
        if Char.getSpd() > 1:
            Char.setStats("inc",1)
            Char.setSpd("dec",1)
            spdText = "Speed:" + str(Char.getSpd())
            charCreateMenu.itemconfig(textBox, text=spdText)
            print("Decrease Speed by One")
    elif stat == "luck":
        if Char.getLuck() > 1:
            Char.setStats("inc",1)
            Char.setLuck("dec",1)
            luckText = "Luck:" + str(Char.getLuck())
            charCreateMenu.itemconfig(textBox, text=luckText)
            print("Decrease Luck by One")
        
    remainStatsText = "Remaining:" + str(Char.getStats())
    charCreateMenu.itemconfig(remainStatsBox, text=remainStatsText)
    save()

def addPoint(root,previousFrame):
    xBox1, yBox1, xBox2, yBox2 = 100,150,300,200
    create = Frame(root,bg="#000000")
    label1 = Label(create, text="STATS",foreground="cyan",bg="#318beb",font=("alagard", 40))
    label1.pack(pady=20)

    charCreateMenu = Canvas(create, bg="#b1d0f2",height=700,width=400)
    charCreateMenu.create_window(200,100)

    # Username Text Box
    charNameText = charCreateMenu.create_text(200,80,text=Char.getName(),font=("alagard", 40))

    # Remaining Stats Box
    RemainStat = charCreateMenu.create_rectangle(xBox1, yBox1, xBox2, yBox2, fill="#ffffff")
    remainStatsText = "Remaining:" + str(Char.getStats())
    remainStatsBox = charCreateMenu.create_text(200,175,text=remainStatsText,font=("alagard", 20))

    # Remaining Health Stats
    charCreateMenu.create_rectangle(xBox1, yBox1 + 80, xBox2, yBox2 + 80, fill="#ffffff")
    hpText = "Health:" + str(Char.getHp())
    hpTextBox = charCreateMenu.create_text(200,255,text=hpText,font=("alagard", 20))
    hpButtonIncrease = Button(create, text=" + ", command=lambda:increase("hp",charCreateMenu,remainStatsBox,hpTextBox)).place(relx=0.56, rely=0.325)
    hpButtonDecrease = Button(create, text=" - ", command=lambda:decrease("hp",charCreateMenu,remainStatsBox,hpTextBox)).place(relx=0.43, rely=0.325)

    # Remaining Attack Stats
    charCreateMenu.create_rectangle(xBox1, yBox1 + 160, xBox2, yBox2 + 160, fill="#ffffff")
    atkText = "Attack:" + str(Char.getAtk())
    atkTextBox = charCreateMenu.create_text(200,335,text=atkText,font=("alagard", 20))
    atkButtonIncrease = Button(create, text=" + ", command=lambda:increase("atk",charCreateMenu,remainStatsBox,atkTextBox)).place(relx=0.56, rely=0.398)
    atkButtonDecrease = Button(create, text=" - ", command=lambda:decrease("atk",charCreateMenu,remainStatsBox,atkTextBox)).place(relx=0.43, rely=0.398)

    # Remaining Defend Stats
    charCreateMenu.create_rectangle(xBox1, yBox1 + 240, xBox2, yBox2 + 240, fill="#ffffff")
    defText = "Defend:" + str(Char.getArmor())
    defTextBox = charCreateMenu.create_text(200,415,text=defText,font=("alagard", 20))
    defButtonIncrease = Button(create, text=" + ", command=lambda:increase("armor",charCreateMenu,remainStatsBox,defTextBox)).place(relx=0.56, rely=0.471)
    defButtonDecrease = Button(create, text=" - ", command=lambda:decrease("armor",charCreateMenu,remainStatsBox,defTextBox)).place(relx=0.43, rely=0.471)

    # Remaining Speed Stats
    charCreateMenu.create_rectangle(xBox1, yBox1 + 320, xBox2, yBox2 + 320, fill="#ffffff")
    spdText = "Speed:" + str(Char.getSpd())
    spdTextBox = charCreateMenu.create_text(200,495,text=spdText,font=("alagard", 20))
    spdButtonIncrease = Button(create, text=" + ", command=lambda:increase("spd",charCreateMenu,remainStatsBox,spdTextBox)).place(relx=0.56, rely=0.544)
    spdButtonDecrease = Button(create, text=" - ", command=lambda:decrease("spd",charCreateMenu,remainStatsBox,spdTextBox)).place(relx=0.43, rely=0.544)
    
    # Remaining Luck Stats
    charCreateMenu.create_rectangle(xBox1, yBox1 + 400, xBox2, yBox2 + 400, fill="#ffffff")
    luckText = "Luck:" + str(Char.getLuck())
    luckTextBox = charCreateMenu.create_text(200,575,text=luckText,font=("alagard", 20))
    luckButtonIncrease = Button(create, text=" + ", command=lambda:increase("luck",charCreateMenu,remainStatsBox,luckTextBox)).place(relx=0.56, rely=0.618)
    luckButtonDecrease = Button(create, text=" - ", command=lambda:decrease("luck",charCreateMenu,remainStatsBox,luckTextBox)).place(relx=0.43, rely=0.618)

    backBtn = Button(create,text=" Back ",font=("alagard", 15), command= lambda: back(create,previousFrame,root)).place(x=1075,y=760)

    charCreateMenu.pack()
    create.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda x: back(create,previousFrame,root))
    

"""
===============================================================
                      Shop Frame
===============================================================
"""
def upgrade(itemName,root):
    if "helmet" in itemName:
        Char.upgradeGear(0,50)
        text = "Helmet upgraded"
    elif "chestplate" in itemName:
        Char.upgradeGear(1,50)
        text = "Chestplate upgraded"
    elif "legging" in itemName:
        Char.upgradeGear(2,50)
        text = "Legging Upgraded"
    elif "boot" in itemName:
        Char.upgradeGear(3,50)
        text = "Boots Upgraded"
     
    save()
    shopFrame.pack_forget()
    shop(root,gameFrame)

def buy(itemName,item,shopCanvas,moneyTextBox,root):   
    # Render bought item name
    buyBox = shopCanvas.create_rectangle(1400, 350, 1900, 500, fill="white",width=5, outline='black')
    itemName = itemName[:-4]
    if itemName == "Hp Potion":
        done = Char.buyItem("Hp Potion",20)
    elif itemName == "Sus Potion":
        done = Char.buyItem("Sus Potion",20)
    elif itemName == "Portal Warp":
        done = Char.buyItem("Portal Warp",50)
    elif itemName == "Red Scroll":
        itemName, done = Char.buyScroll(Char,"Red Scroll",20)
    elif itemName == "Blue Scroll":
        itemName, done = Char.buyScroll(Char,"Blue Scroll",20)
    elif itemName == "Green Scroll":
        itemName, done = Char.buyScroll(Char,"Green Scroll",20)
        
    if done == "":
        text = "Not enough money"
    else:
        text = "You bought " + itemName
        
    buyText = shopCanvas.create_text(1650,420,text="",font=("alagard", 20))
    printSlowShop(text,buyText,shopCanvas)
    
    root.after(3000, shopCanvas.delete, buyText,buyBox) 
    
    moneyText = "Money: " + str(Char.getMoney()) + "G"
    shopCanvas.itemconfig(moneyTextBox,text=moneyText)
    save()

def shop(root,previousFrame):
    global imgList, skillList,upgradeList,startBg,bg,shopFrame,shopCanvas
    
    gameFrame.pack_forget()
    shopFrame = Frame(root)
    shopCanvas = Canvas(shopFrame,bg="#b1d0f2")
    
    path = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\background\Shop\\"
    
    bgLink = str(path) + "main.png"
    bg = PhotoImage(file = bgLink)
    startBg = shopCanvas.create_image(960, 540, image=bg)
    
    item = Item()
    imgList = {}
    skillList = {}
    upgradeList = {}
    buyBtn = []
    skillBtn = []
    upgradeBtn = []
    itemID = 1
    skillID = 1
    upgradeID = 1
    x,y = 600 , 160 # Item cords
    x2,y2 = 860, 140 #  Buy cords
    x3,y3 = 750, 165 # Item name cords
    
    # Render Shop GUI
    shopText = shopCanvas.create_text(960,50,text="SHOP",font=("alagard", 40),anchor='center')
    shopBox = shopCanvas.create_rectangle(560, 100, 1360, 800, fill="white",width=5, outline='black')
    
    # Render items
    for imgs in item.getItemList():       
        img = PhotoImage(file = item.getItemPath(imgs)).subsample(4)
        imgList[img] = itemID
        if imgs[:-4] == "Portal Warp":
            price = 50
        else:
            price = 20
        shopCanvas.create_image(x, y, image=img)
        shopCanvas.create_text(x3,y,text=item.getNameTag(imgs,price),font=("alagard", 20))
        y += 80
        itemID += 1
    
    for imgs in Char.getSkillList():       
        img = PhotoImage(file = Char.getSkillPath(imgs)).subsample(4)
        skillList[img] = skillID
        shopCanvas.create_image(x, y, image=img)
        shopCanvas.create_text(x3,y,text = Char.getSkillTag(imgs,20),font=("alagard", 20))
        y += 80
        skillID += 1
    
    gear = Char.getUpgrade()
    # Render armor upgrades
    for imgs in item.genCurrentUpgrade(gear):
        img = PhotoImage(file = item.getUpgradePath(str(imgs))).subsample(4)
        upgradeList[img] = upgradeID
        shopCanvas.create_image(x + 360, y3, image=img)
        shopCanvas.create_text(x3 + 280,y3,text=item.getUpgradeTag(imgs,upgradeID - 1),font=("alagard", 20),anchor="w")
        y += 100
        y3 += 80
        upgradeID += 1
                

    # Render Money
    moneyText = "Money: " + str(Char.getMoney()) + "G"
    moneyTextBox = shopCanvas.create_text(960,760,text=moneyText,font=("alagard", 20))
       
    # Render Buy
    for i in item.getItemList():
        buyBtn.append(Button(shopCanvas, text="BUY", command=lambda i=i: buy(i,item,shopCanvas,moneyTextBox,root), font=("alagard", 15)).place(x=x2, y=y2))
        y2 += 80
    
    for i in Char.getSkillList():
        skillBtn.append(Button(shopCanvas, text="BUY", command=lambda i=i: buy(i,item,shopCanvas,moneyTextBox,root), font=("alagard", 15)).place(x=x2, y=y2))
        y2 += 80
        
    # Render Upgrade
    for i in item.getUpgradeList():
        upgradeBtn.append(Button(shopCanvas, text="UPGRADE", command=lambda i=i: upgrade(i,root), font=("alagard", 15)).place(x=x2 + 370, y=y2 - 480))
        y2 += 80
    
    backBtn = Button(shopCanvas,text=" Back ",font=("alagard", 15), command= lambda: back(shopFrame,previousFrame,root)).place(x=1260,y=740)
    
    # Render Frame and Canvas
    shopFrame.pack(fill="both", expand=1)
    shopCanvas.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda x: back(shopFrame,previousFrame,root))

"""
===============================================================
                        Game Mechanics
===============================================================
"""

def back(frame,previousFrame,root):
    global bg,endBgImg
    update(root)
    click()
    frame.pack_forget()
    path = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\background\Game\\"
    altPath = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\background\\"
    
    bgLink = str(path) + randomBg
    bg = PhotoImage(file = bgLink)
    startBg = gameCanvas.create_image(960, 440, image=bg)  
    gameCanvas.tag_lower(startBg)
    
    try:
        endLink = altPath + "menu\\end.png"
        endBgImg = PhotoImage(file = endLink)
        endBg = endCanvas.create_image(960, 540, image=endBgImg)  
        endCanvas.tag_lower(endBg)
    except:
        pass
    
    previousFrame.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda e: close_win(root))
    

def run(root):
    turn = random.randint(1, Char.getSpd() + Mon.getSpd())
    if Char.getCurrentHp() >= 0:
        if turn <= Char.getSpd() + Char.getLuck():
            text = "Escape succesfully!"
            printSlow(text)
            new(root)
        else:
            text = "Failed to escape..."
            dmg = abs(Char.getArmor() - Mon.getAtk())
            Char.setCurrentHp("dec",int(dmg))
            printSlow(text)
    else:
        death(root)
    update(root)
        
def playAnimation(root):
    global newPhoto
    path = os.path.dirname(os.path.abspath(__file__))
    for i in range(1,6):
        text = path + "\\Assets\\Mon\\" + Mon.getMonId() + "\\" + str(i) + ".png"
        newPhoto = PhotoImage(file = text)
        gameCanvas.itemconfig(monPhoto,image=newPhoto)
        root.update()
        time.sleep(0.05)
    
    if Char.getDifficulty() == 4:
        newPhoto = PhotoImage(file = Mon.getBossName())
    else:
        newPhoto = PhotoImage(file = Mon.getMonName())
    gameCanvas.itemconfig(monPhoto,image=newPhoto)
    update(root)


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

def printSlowShop(myText,itembox,canvas):
    delta = 50
    delay = 0
    for x in range(len(myText)+1):
        s = myText[:x]
        newText = lambda s=s: canvas.itemconfigure(itembox,text=s)
        canvas.after(delay,newText)
        delay += delta
   
def printSlow(myText):
    delta = 50
    delay = 0
    for x in range(len(myText)+1):
        s = myText[:x]
        newText = lambda s=s: gameCanvas.itemconfigure(gameText,text=s)
        gameCanvas.after(delay,newText)
        delay += delta

def attack(playerHp,root):
    click()
    if Mon.getCurrentHp() > 0:
        turn = Char.attack(Mon)
        gainStat = 0
        gainMon = 0
        # Change HP text
        monHpText = "HP: " + str(Mon.getCurrentHp()) + "/" + str(Mon.getHp())
        playerHpText = "HP:" + str(Char.getCurrentHp()) + "/" + str(Char.getHp())
        if turn == True:
            if Mon.getCurrentHp() <= 0:
                text = "You defeated " + str(Mon.getName())
                printSlow(text)
            else:
                dmgText = " - " + str(Char.getDmgDone())
                dmgBox = gameCanvas.create_text(1250,180, text=dmgText, fill="red", font=("alagard", 36,"bold italic"))
                
                text = "You did " + str(Char.getDmgDone()) + " Damage!"
                attackSound("Mon")
                playAnimation(root)
                printSlow(text)
                root.after(1000, gameCanvas.delete, dmgBox)       
        elif turn == False:
            text = "You took " + str(Char.getDmgTaken()) + " Damage!"
            attackSound("Player")
            printSlow(text)
            if Char.getCurrentHp() <= 0:
                print("You are dead")
                death(root)
        elif turn == "DODGE":
            text = "You dodged the attack!"
            printSlow(text)
         
        gameCanvas.itemconfig(monHp, text=monHpText)
        gameCanvas.itemconfig(playerHp, text=playerHpText)
        
        print("Mon HP is ", Mon.getCurrentHp())
        print("Player HP is ", Char.getCurrentHp())
        print("================")
    else:
        if Char.getDifficulty() == 1:
            print("Increase Stat by 1")
            Char.setStats("inc",1)
            Char.incMoney(20)
            gainStat = 1
            gainMon = 20

        elif Char.getDifficulty() == 2:
            print("Increase Stat by 2")
            Char.setStats("inc",2)
            Char.incMoney(40)
            gainStat = 2
            gainMon = 40

        elif Char.getDifficulty() == 3:
            print("Increase Stat by 3")
            Char.setStats("inc",3)
            Char.incMoney(60)
            gainStat = 3
            gainMon = 60
        
        elif Char.getDifficulty() == 4:
            print("Increase Stat by 4")
            Char.setStats("inc",4)
            Char.incMoney(100)
            gainStat = 5
            gainMon = 100
            
        moneyText = "You gained " + str(gainMon) +"G and " + str(gainStat) + " stat point!"
        printSlow(moneyText)
        endGame(root)
    # print("Changing stats", Char.getArmor())        
    save()
    update(root)

def save():
    #print("Game Saved!")
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
    data["atk"] = Char.getAtk()
    data["spd"] = Char.getSpd()
    data["def"] = Char.getArmor()
    data["upgrades"] = Char.getUpgrade()
    
    with open("saves/data.json", "w") as jsonFile:
        json.dump(data, jsonFile,indent=4)
    
    jsonFile.close()
 

"""
===============================================================
                         Gen New Mon
===============================================================                  
"""

def genMon():
    global photo, Mon,monPhoto,bg,startBg, randomBg
    
    #Gen random Background
    path = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\background\Game\\"
    bgList = next(os.walk(path), (None, None, []))[2]
    randomBg = random.choice(bgList)
    
    bgLink = str(path) + randomBg
    bg = PhotoImage(file = bgLink)
    startBg = gameCanvas.create_image(960, 440, image=bg)
    
    #Gen mon
    Mon = Monster(Char)
    photo = PhotoImage(file = Mon.genMonName())
    monPhoto = gameCanvas.create_image(950, 480, image=photo)
    if Char.getDifficulty() == 4:
        photo = PhotoImage(file = Mon.genBossName())
        monPhoto = gameCanvas.create_image(950, 480, image=photo)
    


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
    fontPath = str(Path(os.path.dirname(os.path.abspath(__file__)))) + "\Assets\\Font\\alagard.ttf"
    pyglet.font.add_file(fontPath)
    genCanvas(root)
    Char = Player()
    pg.mixer.init()
    pg.init()
    genMon()
    game(root)
    bgMusic()

def genCanvas(root):
    global gameCanvas,gameFrame,Char
    gameFrame = Frame(root,bg="#000000")
    gameCanvas = Canvas(gameFrame,bg="#b1d0f2")

def game(root):
    global monHp,playerHp,playerAtk,playerDef,playerSpd,gameText
    
    textBox = gameCanvas.create_rectangle(5, 800, 1195, 1075, fill="#14171c",width=5, outline='#d5dde8')
    ActionBox = gameCanvas.create_rectangle(1200, 800, 1915, 1075, fill="#14171c",width=5, outline='#d5dde8')

    # Render enemy's health
    monHpBox = gameCanvas.create_rectangle(5, 5, 500, 200, fill="#14171c",width=5, outline='#d5dde8')

    # Generate Mon Stats
    monHpText = "HP: " + str(Mon.getCurrentHp()) + "/" + str(Mon.getHp())
    monAtkText = "ATK: " + str(Mon.getAtk())
    monDefText = "Def: " + str(Mon.getArmor())
    monSpdText = "Spd: " + str(Mon.getSpd())

    monName = gameCanvas.create_text(250,50,text=(Mon.getName()),font=("alagard", 30),fill="white")
    monHp = gameCanvas.create_text(64,100,text=monHpText,font=("alagard", 20),anchor='w',fill="white")
    monAtk = gameCanvas.create_text(64,150,text=monAtkText,font=("alagard", 20),anchor='w',fill="white")
    monDef = gameCanvas.create_text(280,100,text=monDefText,font=("alagard", 20),anchor='w',fill="white")
    monSpd = gameCanvas.create_text(280,150,text=monSpdText,font=("alagard", 20),anchor='w',fill="white")
    

    # Render Character's health
    playerHpBox = gameCanvas.create_rectangle(1400, 600, 1915, 795, fill="#14171c",width=5, outline='#d5dde8')

    # Generate Player stats
    playerHpText = "HP:" + str(Char.getCurrentHp()) + "/" + str(Char.getHp())
    playerAtkText = "ATK:" + str(Char.getAtk())
    playerDefText = "Def:" + str(Char.getArmor())
    playerSpdText = "Spd:" + str(Char.getSpd())

    playerName = gameCanvas.create_text(1650,640,text=(Char.getName()),font=("alagard", 30),fill="white")
    playerHp = gameCanvas.create_text(1460,680,text=playerHpText,font=("alagard", 20),anchor='w',fill="white")
    playerAtk = gameCanvas.create_text(1690,680,text=playerAtkText,font=("alagard", 20),anchor='w',fill="white")
    playerDef = gameCanvas.create_text(1460,730,text=playerDefText,font=("alagard", 20),anchor='w',fill="white")
    playerSpd = gameCanvas.create_text(1690,730,text=playerSpdText,font=("alagard", 20),anchor='w',fill="white")

    # Render Game Message
    foundText = "You found " + Mon.getName() + "!"
    gameText = gameCanvas.create_text(560,930,text="",font=("alagard", 30),fill="white")
    printSlow(foundText)

    atkBtn = Button(gameCanvas, text="ATK",command=lambda:attack(playerHp,root),width=10,border=5,font=("alagard", 20)).place(relx=0.65, rely=0.8)
    bagBtn = Button(gameCanvas, text="BAG",width=10,border=5,command=lambda:bag(root,playerHp,gameFrame),font=("alagard", 20)).place(relx=0.65, rely=0.9)
    skillbtn = Button(gameCanvas, text="SCROLL",width=10,border=5,command=lambda:skill(root,gameFrame),font=("alagard", 20)).place(relx=0.768, rely=0.8)
    runBtn = Button(gameCanvas, text="RUN",width=10,border=5,command=lambda:run(root),font=("alagard", 20)).place(relx=0.768, rely=0.9)
    saveBtn = Button(gameCanvas, text="SHOP",command=lambda:goToShop(root,gameFrame),width=10,height=4,border=5,font=("alagard", 20)).place(relx=0.89, rely=0.81)
    
    gameFrame.pack(fill="both", expand=1)
    gameCanvas.pack(fill="both", expand=1)
        
    root.bind('<Escape>', lambda e: close_win(root))
    root.bind('<F2>', lambda x :shop(root,gameFrame))
    root.bind('b', lambda x :bag(root,playerHp,gameFrame))