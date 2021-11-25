import json, os , random, math
from pathlib import Path
from Classes.Item import *

class Player:
    def __init__(self):
        self.name = "Default"
        self.hp = 10
        self.atk = 10
        self.armor = 10
        self.spd = 10
        self.luck = 5
        self.stats = 10
        self.currentHp = 10
        self.dmgDone = 0
        self.dmgTaken = 0
        self.money = 0
        self.bag = {}
        self.redSkills = {}
        self.blueSkills = {}
        self.greenSkills = {}
        self.round = 0
        self.difficulty = 2
        self.rarity = ""
        
        self.upgrades = [1,1,1,1]
        
        self.status = {
            "Thunder Bolt" : 0,
            "Shield" : 0,
            "Spike" : 0,
            "Attack" : 0,
            "Armor"  : 0,
            "Speed"  : 0,
        }
        
        
        
        #Load Data
        self.path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.path = self.path.parent.absolute()
        self.path = str(self.path) + "\saves\data.json"
        
        #Load Skill
        self.skillPath = Path(os.path.dirname(os.path.abspath(__file__)))
        self.skillPath = self.skillPath.parent.absolute()
        self.skillPath = str(self.skillPath) + "\Assets\Skills"
        self.loadChar()
        self.genItem()
        self.allSkills = {**self.redSkills, **self.blueSkills, **self.greenSkills}
        
    def loadChar(self): 
        with open(self.path) as fh:
            data = json.load(fh)
        
        self.stats = data["stats"]
        self.name = data["name"]
        self.hp = data["hp"]
        self.atk = data["atk"]
        self.armor = data["def"]
        self.spd = data["spd"]
        self.luck = data["luck"]
        self.currentHp = data["currentHp"]
        self.money = data["money"]
        self.bag = data["bag"]
        self.redSkills = data["redSkills"]
        self.blueSkills = data["blueSkills"]
        self.greenSkills = data["greenSkills"]
        self.upgrades = data["upgrades"]
        
        fh.close()
        # Original Stats
                
        self.atkOG = self.atk
        self.armorOG = self.armor
        self.speedOG = self.spd
        self.atkOG2 = self.atk
        self.armorOG2 = self.armor
    
    def removeBuff(self,Mon):
        if Mon.getCurrentHp() < 0:
            self.status.clear()
            self.atk = self.atkOG2
            self.armor = self.armorOG2
            self.spd = self.speedOG
    
    def tick(self,Mon):       
        self.round += 1
        for key, val in self.status.items():    
            if self.status[key] > 0:
                for key, val in self.status.items():
                    if "Spike" in key:
                        if self.status[key] > 0:
                            tempDMG = abs(int((self.armor/2) - Mon.getAtk()))
                            print("Reflecting DMG", tempDMG)
                            if tempDMG == 0:
                                Mon.setHp(1)
                            else:
                                Mon.setHp(tempDMG)
                    if "Attack" in key:
                        if self.rarity == "Common":
                            dmgUp = 10
                        elif self.rarity == "Normal":
                            dmgUp = 20
                        elif self.rarity == "Rare":
                            dmgUp = 30
                        if self.status[key] > 0:
                            self.atk += dmgUp
                    if "Armor" in key:
                        if self.rarity == "Common":
                            armorUp = 10
                        elif self.rarity == "Normal":
                            armorUp = 20
                        elif self.rarity == "Rare":
                            armorUp = 30
                        if self.status[key] > 0:
                            self.armor += armorUp
                    if self.status[key] == 0:
                        pass
                    else:
                        self.status[key] -= 1
                break
            elif self.status[key] == 0:
                if "Thunder" in key:
                    self.atk = self.atkOG
                if "Shield" in key:
                    self.armor = self.armorOG
                if "Speed" in key:
                    self.spd = self.speedOG
                if "Spike" in key:
                    self.armor = self.armorOG
                if "Armor" in key:
                    self.armor = self.armorOG2
                if "Attack" in key:
                    self.atk = self.atkOG2
                if "Speed" in key:
                    self.spd = self.speedOG
                    
        
    # Player Moves
    def attack(self,Mon):
        self.tick(Mon)
        turn = random.randint(1, self.spd + Mon.getSpd())
        #print("Rolled: ",turn)
        if turn <= self.spd + int(self.luck/4):
            # print("Player attacking")
            print("The attack is ", self.atk)
            if Mon.getArmor() - self.atk >= 0:
                # ACTUAL VALUES
                self.dmgDone = 1
                
                criRoll = random.randint(1,100)
                if criRoll <= (self.luck * 2):
                    self.dmgDone = int((self.dmgDone * (self.luck / 10)))
                    print("CRI DMG", self.dmgDone)
                    if self.dmgDone == 1:
                        self.dmgDone += 1
                Mon.setHp(self.dmgDone)
                
            else:
                self.dmgDone = abs(Mon.getArmor() - self.atk)
                
                Mon.setHp(self.dmgDone)
            return True
        else:
            # print("Monster Attacked")
            dodgeRoll = random.randint(1,100)
            dodgeChance = (self.spd / 10) * (self.luck / 10)
            print("Dodge change is ",dodgeChance) 
            if dodgeRoll <= dodgeChance:
                print("DODGED!")
                return "DODGE"
            else:
                if self.armor - Mon.getAtk() >= 0:
                    self.dmgTaken = 1
                    self.currentHp -= self.dmgTaken
                else:
                    self.dmgTaken = abs(self.armor - Mon.getAtk())
                    self.currentHp -= self.dmgTaken
                return False
    
    """
    ===============================================================
                            Bag
    ===============================================================
    """
    
    def genItem(self):
        item = Item()
        for i in item.genItemList():
            if i in self.bag.keys():
                pass
            else:
                self.bag[i] = 0
            
               
    def useItem(self,name):
        print("Use ", name)
        if name == "Hp Potion":
            if self.bag[name] > 0:
                if self.currentHp <= self.hp:
                    if self.currentHp + 20 >= self.hp:
                        self.currentHp += self.hp - self.currentHp
                    else:
                        self.currentHp += 20
                    print("You have " + str(self.bag[name]) + " left")
                    self.bag[name] -= 1
                else:
                    pass
        elif name == "Portal Warp":
            print("Use scroll")
            self.bag[name] -= 1
        
        elif name == "Mp Potion":
            pass
          
    def buyItem(self,item,price):
        if item == "Hp Potion" or item == "Mp Potion":
            if self.money >= price:       
                self.bag[item] += 1
                self.money -= price
        elif item == "Portal Warp":
            if self.money >= price:       
                self.bag[item] += 1
                self.money -= price
                
    def upgradeGear(self,item,price):
        # if self.money >= price:
        if self.upgrades[item] < 4:
            self.upgrades[item] += 1
            # self.money -= price
            
            
    """
    ===============================================================
                            Skills
    ===============================================================
    """  
    def useScroll(self,skill,count,Mon):
        self.dmgDone = 0
        if skill in self.redSkills:
            if self.redSkills[skill] > 0:
                # Skill mechanic
                if "Bullet Storm" in skill:
                    if "Common" in skill:
                        min,max,rarity = 20,30,"Common"
                    elif "Normal" in skill:
                        min,max,rarity = 30,50,"Normal"
                    elif "Rare" in skill:
                        min,max,rarity = 60,80, "Rare"
                        
                    for i in range(0,3):
                        dmg = random.randint(min, max)
                        temp = ((self.atk * dmg)/100)
                        self.dmgDone += temp
                    self.dmgDone = abs(int((Mon.getArmor()/4) - self.dmgDone))
                    if self.dmgDone <= 3:
                        self.dmgDone = 3
                    
                    Mon.setHp(self.dmgDone)
                    
                elif "Precision Strike" in skill:
                    if "Common" in skill:
                        min,max,rarity = 140,160,"Common"
                    elif "Normal" in skill:
                        min,max,rarity = 160,180,"Normal"
                    elif "Rare" in skill:
                        min,max,rarity = 180,200, "Rare"
                    
                    dmg = random.randint(min, max)
                    temp = ((self.atk * dmg)/100)
                    self.dmgDone += temp
                    self.dmgDone = abs(int((Mon.getArmor()/4) - self.dmgDone))
                    Mon.setHp(self.dmgDone)
                
                elif "Thunder Bolt" in skill:
                    if "Common" in skill:
                        dmg,dmgInc = 120,10
                    elif "Normal" in skill:
                        dmg,dmgInc = 140,20
                    elif "Rare" in skill:
                        dmg,dmgInc = 160,30
                    
                    temp = ((self.atk * dmg)/100)
                    self.dmgDone = abs(int((Mon.getArmor()/2) - self.dmgDone))
                    Mon.setHp(self.dmgDone)
                    self.atk += dmgInc
                    self.status["Thunder Bolt"] = 3 
                self.redSkills[skill] -= 1
            else:
                print("no spells")
        elif skill in self.blueSkills:
            if self.blueSkills[skill] > 0:
                if "Shield" in skill:
                    if "Common" in skill:
                        armorUp,rarity = 20,"Common"
                    elif "Normal" in skill:
                        armorUp,rarity = 30,"Normal"
                    elif "Rare" in skill:
                        armorUp,rarity = 40,"Rare"
                    
                    self.status["Shield"] = 3
                    self.armor += armorUp
                elif "Spike" in skill:
                    if "Common" in skill:
                        armorUp,rarity = 10,"Common"
                    elif "Normal" in skill:
                        armorUp,rarity = 20,"Normal"
                    elif "Rare" in skill:
                        armorUp,rarity = 30,"Rare"
                    
                    self.status["Spike"] = 3
                    self.armor += armorUp 
                self.blueSkills[skill] -= 1
            else:
                print("no spells")
        elif skill in self.greenSkills:
            if self.greenSkills[skill] > 0:
                if "Heal" in skill:
                    if "Common" in skill:
                        amount,rarity = 10,"Common"
                    elif "Normal" in skill:
                        amount,rarity = 20,"Normal"
                    elif "Rare" in skill:
                        amount,rarity = 30,"Rare"
                    self.currentHp += amount
                elif "Attack" in skill:
                    if "Common" in skill:
                        amount,self.rarity = 10,"Common"
                    elif "Normal" in skill:
                        amount,self.rarity = 20,"Normal"
                    elif "Rare" in skill:
                        amount,self.rarity = 30,"Rare"
                    self.atk += amount
                    self.status["Attack"] = 5 
                elif "Armor" in skill:
                    if "Common" in skill:
                        amount,self.rarity = 10,"Common"
                    elif "Normal" in skill:
                        amount,self.rarity = 20,"Normal"
                    elif "Rare" in skill:
                        amount,self.rarity = 30,"Rare"
                    self.armor += amount
                    self.status["Armor"] = 5
                elif "Speed" in skill:
                    if "Common" in skill:
                        amount,rarity = 10,"Common"
                    elif "Normal" in skill:
                        amount,rarity = 20,"Normal"
                    elif "Rare" in skill:
                        amount,rarity = 30,"Rare"
                    self.spd += amount
                    self.status["Speed"] = 5 
                self.greenSkills[skill] -= 1
            else:
                print("no spells")    
            
    def buyScroll(self,Char,item,price):
        temp = random.randint(1,100)
        roll = temp + (int(Char.getLuck()) / 2) # Increase chance of getting better item
        temp = random.randint(1,100)
        itemName = ""
        if self.money >= price:
            self.money -= 20
            rarity = ["Common","Normal","Rare"]
            
            if item == "Red Scroll":
                item = self.redSkills
            elif item == "Blue Scroll":
                item = self.blueSkills
            elif item == "Green Scroll":
                item = self.greenSkills
            
            if roll >= 1 and roll <= 50:            
                skill = [i for i in list(item) if "Common" in i]
                randSkill = random.choice(skill) #Choose random skills
                item[randSkill] += 1
                itemName = randSkill
                print(itemName)
                
            elif roll >= 51 and roll <= 80:            
                skill = [i for i in list(item) if "Normal" in i]
                randSkill = random.choice(skill)
                item[randSkill] += 1  
                itemName = randSkill
            
            elif roll >= 81:   
                skill = [i for i in list(item) if "Rare" in i]
                randSkill = random.choice(skill)
                item[randSkill] += 1
                itemName = randSkill
            
            if item == "Red Scroll":
                self.redSkills = item
            elif item == "Blue Scroll":
                self.blueSkills = item
            elif item == "Green Scroll":
                self.GreenSkills = item
        return itemName
        
    
    # Setters
    def setCurrentHp(self,mode,amount):
        print("Decrease hp by", amount)
        if mode == "dec":
            self.currentHp -= amount
        else:
            self.currentHp += amount
    
    def incMoney(self,amount):
        self.money += amount
    
    def setDifficulty(self,mode):
        self.difficulty = mode
        
    def setHp(self,mode,amount):
        if mode == "dec":
            self.hp -= amount
        else:
            self.hp += amount
    
    def setAtk(self,mode,amount):
        if mode == "dec":
            self.atk -= amount
        else:
            self.atk += amount
        self.atkOG = self.atk
        self.atkOG2 = self.atk
        
    def setArmor(self,mode,amount):
        if mode == "dec":
            self.armor -= amount
        else:
            self.armor += amount
        self.armorOG = self.armor
        self.armorOG2 = self.armor
    
    def setSpd(self,mode,amount):
        if mode == "dec":
            self.spd -= amount
        else:
            self.spd += amount
        self.speedOG = self.spd
        
    def setLuck(self,mode,amount):
        if mode == "dec":
            self.luck -= amount
        else:
            self.luck += amount
    
    def setStats(self,mode,amount):
        if mode == "dec":
            self.stats -= amount
        else:
            self.stats += amount
       
    # Getters
    def getUpgrade(self):
        return self.upgrades
    
    def getStatus(self):
        return self.status
    
    def getLuck(self):
        return self.luck
    
    def getRedSkill(self):
        return self.redSkills
    
    def getBlueSkill(self):
        return self.blueSkills
    
    def getGreenSkill(self):
        return self.greenSkills
    
    def getBag(self,id):
        return "x" + str(self.bag.get(id))
    
    def getBagList(self):
        return self.bag
    
    def getMoney(self):
        return self.money
    
    def getStats(self):
        return self.stats
        
    def getName(self):
        return self.name
    
    def getTotalStats(self):
        totalStats = (self.hp/4) + self.atkOG2 + self.armorOG + self.speedOG + self.luck
        return totalStats
    
    def getDmgDone(self):
        return self.dmgDone
    
    def getDmgTaken(self):
        return self.dmgTaken
    
    def getCurrentHp(self):
        return self.currentHp
    
    def getHp(self):
        return self.hp
    
    def getAtk(self):
        return self.atk
    
    def getArmor(self):
        return self.armor
    
    def getSpd(self):
        return self.spd
    
    # Scrolls
    
    def getRedSkill(self):
        return self.redSkills
    
    def getBlueSkill(self):
        return self.blueSkills
    
    def getGreenSkill(self):
        return self.greenSkills
    
    def genSkillList(self):
        temp = next(os.walk(self.skillPath), (None, None, []))[2]
        for word in temp:
            self.skillList.append(word[:-4])
        return self.skillList
    
    def getSkillPath(self,item):
        return self.skillPath + "\\" + item
    
    def getSkillList(self):
        return next(os.walk(self.skillPath), (None, None, []))[2]
    
    def getSkillTag(self,img,price):
        self.scrollName = img[:-4] + " " + str(price) + "G"
        return self.scrollName
    
    def getDifficulty(self):
        return self.difficulty
    