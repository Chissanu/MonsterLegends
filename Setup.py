from tkinter import *
import json
import os
import Game as game

global name,stats,hp,atk,armor,spd

name,stats,hp,atk,armor,spd,luck = "",10,100,10,10,10,5


def increase(stat,charCreateMenu,remainStatsBox,textBox):
    global stats,hp,atk,armor,spd,luck
    if stats >= 1:
        stats -= 1
        remainStatsText = "Remaining:" + str(stats)
        charCreateMenu.itemconfig(remainStatsBox, text=remainStatsText)
        if stat == "hp":     
            hp += 1
            hpText = "Health:" + str(hp)
            charCreateMenu.itemconfig(textBox, text=hpText)
            print("Increase HP by One")
        elif stat == "atk":     
            atk += 1
            atkText = "Attack:" + str(atk)
            charCreateMenu.itemconfig(textBox, text=atkText)
            print("Increase Attack by One")
        elif stat == "armor":     
            armor += 1
            defText = "Defend:" + str(armor)
            charCreateMenu.itemconfig(textBox, text=defText)
            print("Increase armor by One")
        elif stat == "spd":     
            spd += 1
            spdText = "Speed:" + str(spd)
            charCreateMenu.itemconfig(textBox, text=spdText)
            print("Increase speed by One")
        elif stat == "luck":     
            luck += 1
            luckText = "Luck:" + str(luck)
            charCreateMenu.itemconfig(textBox, text=luckText)
            print("Increase speed by One")    
    else:
        print("No more stats")
        
def decrease(stat,charCreateMenu,remainStatsBox,textBox):
    global stats,hp,atk,armor,spd,luck
    stats += 1
    remainStatsText = "Remaining:" + str(stats)
    charCreateMenu.itemconfig(remainStatsBox, text=remainStatsText)
    if stat == "hp":     
        hp -= 1
        hpText = "Health:" + str(hp)
        charCreateMenu.itemconfig(textBox, text=hpText)
        print("Decrease HP by One")
    elif stat == "atk": 
        atk -= 1
        atkText = "Attack:" + str(atk)
        charCreateMenu.itemconfig(textBox, text=atkText)
        print("Decrease Attack by One")
    elif stat == "armor": 
        armor -= 1
        defText = "Defend:" + str(armor)
        charCreateMenu.itemconfig(textBox, text=defText)
        print("Decrease Armor by One")
    elif stat == "spd": 
        spd -= 1
        spdText = "Speed:" + str(spd)
        charCreateMenu.itemconfig(textBox, text=spdText)
        print("Decrease Speed by One")
    elif stat == "luck": 
        luck -= 1
        luckText = "Luck:" + str(luck)
        charCreateMenu.itemconfig(textBox, text=luckText)
        print("Decrease Luck by One")

def submit(charCreateName,charCreateMenu,root,create):
    name = charCreateName.get()
    path = os.path.dirname(os.path.abspath(__file__)) + "/saves"
    myData = {
        "name": name,
        "stats": stats,
        "hp": hp,
        "atk": atk,
        "def": armor,
        "spd": spd,
        "luck" : luck,
        "money": 100,
        "bag" : {},
        "redSkills" : {
            "Common Bullet Storm" : 0,
            "Normal Bullet Storm" : 0,
            "Rare Bullet Storm" : 0,
            "Common Precision Strike" : 0,
            "Normal Precision Strike" : 0,
            "Rare Precision Strike" : 0,
            "Common Thunder Bolt" : 0,
            "Normal Thunder Bolt" : 0,
            "Rare Thunder Bolt" : 0,   
        },
        "blueSkills" : {
            "Common Shield" : 0,
            "Normal Shield" : 0,
            "Rare Shield" : 0,
            "Common Spike Shield" : 0,
            "Normal Spike Shield" : 0,
            "Rare Spike Shield" : 0,
        },
        "greenSkills" : {
            "Common Heal" : 0,
            "Normal Heal" : 0,
            "Rare Heal": 0,
            "Common Attack Up" : 0,
            "Normal Attack Up" : 0,
            "Rare Attack Up": 0,
            "Common Armor Up" : 0,
            "Normal Armor Up" : 0,
            "Rare Armor up": 0,
            "Common Speed Up" : 0,
            "Normal Speed Up" : 0,
            "Rare Speed up": 0,
        },
        "currentHp": hp 
    }
    try:
        os.makedirs("saves")
    except:
        print("Folder already exitsts")
        pass
    with open("saves/data.json", 'w') as json_file:
        json.dump(myData, json_file,indent=4)
    game.init_game(root)
    charCreateMenu.pack_forget()
    create.pack_forget()

    
def close_win(root):
    root.destroy()
       
def init_Char(root):
    xBox1, yBox1, xBox2, yBox2 = 100,150,300,200
    create = Frame(root,bg="#000000")
    label1 = Label(create, text="Create Character",foreground="cyan",bg="#318beb",font=("Helvetica", 40))
    label1.pack(pady=20)

    charCreateMenu = Canvas(create, bg="#b1d0f2",height=700,width=400)
    charCreateMenu.create_window(200,100)

    # Username Text Box
    charCreateName = Entry(root,width=12,font=("Calibri 41"), justify='center')
    charCreateMenu.create_window(200, 80, window=charCreateName)

    # Remaining Stats Box
    RemainStat = charCreateMenu.create_rectangle(xBox1, yBox1, xBox2, yBox2, fill="#ffffff")
    remainStatsText = "Remaining:" + str(stats)
    remainStatsBox = charCreateMenu.create_text(200,175,text=remainStatsText,font=("Helvetica", 20))

    # Remaining Health Stats
    charCreateMenu.create_rectangle(xBox1, yBox1 + 80, xBox2, yBox2 + 80, fill="#ffffff")
    hpText = "Health:" + str(hp)
    hpTextBox = charCreateMenu.create_text(200,255,text=hpText,font=("Helvetica", 20))
    hpButtonIncrease = Button(create, text=" + ", command=lambda:increase("hp",charCreateMenu,remainStatsBox,hpTextBox)).place(relx=0.56, rely=0.325)
    hpButtonDecrease = Button(create, text=" - ", command=lambda:decrease("hp",charCreateMenu,remainStatsBox,hpTextBox)).place(relx=0.43, rely=0.325)

    # Remaining Attack Stats
    charCreateMenu.create_rectangle(xBox1, yBox1 + 160, xBox2, yBox2 + 160, fill="#ffffff")
    atkText = "Attack:" + str(atk)
    atkTextBox = charCreateMenu.create_text(200,335,text=atkText,font=("Helvetica", 20))
    atkButtonIncrease = Button(create, text=" + ", command=lambda:increase("atk",charCreateMenu,remainStatsBox,atkTextBox)).place(relx=0.56, rely=0.398)
    atkButtonDecrease = Button(create, text=" - ", command=lambda:decrease("atk",charCreateMenu,remainStatsBox,atkTextBox)).place(relx=0.43, rely=0.398)

    # Remaining Defend Stats
    charCreateMenu.create_rectangle(xBox1, yBox1 + 240, xBox2, yBox2 + 240, fill="#ffffff")
    defText = "Defend:" + str(armor)
    defTextBox = charCreateMenu.create_text(200,415,text=defText,font=("Helvetica", 20))
    defButtonIncrease = Button(create, text=" + ", command=lambda:increase("armor",charCreateMenu,remainStatsBox,defTextBox)).place(relx=0.56, rely=0.471)
    defButtonDecrease = Button(create, text=" - ", command=lambda:decrease("armor",charCreateMenu,remainStatsBox,defTextBox)).place(relx=0.43, rely=0.471)

    # Remaining Speed Stats
    charCreateMenu.create_rectangle(xBox1, yBox1 + 320, xBox2, yBox2 + 320, fill="#ffffff")
    spdText = "Speed:" + str(spd)
    spdTextBox = charCreateMenu.create_text(200,495,text=spdText,font=("Helvetica", 20))
    spdButtonIncrease = Button(create, text=" + ", command=lambda:increase("spd",charCreateMenu,remainStatsBox,spdTextBox)).place(relx=0.56, rely=0.544)
    spdButtonDecrease = Button(create, text=" - ", command=lambda:decrease("spd",charCreateMenu,remainStatsBox,spdTextBox)).place(relx=0.43, rely=0.544)
    
    # Remaining Luck Stats
    charCreateMenu.create_rectangle(xBox1, yBox1 + 400, xBox2, yBox2 + 400, fill="#ffffff")
    luckText = "Luck:" + str(luck)
    luckTextBox = charCreateMenu.create_text(200,575,text=luckText,font=("Helvetica", 20))
    luckButtonIncrease = Button(create, text=" + ", command=lambda:increase("luck",charCreateMenu,remainStatsBox,luckTextBox)).place(relx=0.56, rely=0.618)
    luckButtonDecrease = Button(create, text=" - ", command=lambda:decrease("luck",charCreateMenu,remainStatsBox,luckTextBox)).place(relx=0.43, rely=0.618)

    submitBtn = Button(create, text="Next", command=lambda:submit(charCreateName,charCreateMenu,root,create),font=("Helvetica", 15)).place(relx=0.485, rely=0.7)

    charCreateMenu.pack()
    create.pack(fill="both", expand=1)
    root.bind('<Escape>', lambda e: close_win(root))


    
        