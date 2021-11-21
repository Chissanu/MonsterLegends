import os
from pathlib import Path
import random

class Monster:
    def __init__(self,Char):
        self.hp = 100
        self.atk = 5
        self.armor = 10
        self.spd = 5
        self.currentHp = 100
        self.monName = "Slime"
        self.monId = "Slime"
        self.playerStat = Char.getTotalStats()
        self.genStats(Char)
        # Path
        self.path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.path = self.path.parent.absolute()
        self.bossPath = self.path
        self.bossPath = str(self.path) + "\Assets\Mon\Boss"
        self.path = str(self.path) + "\Assets\Mon"
    
    def genMonName(self):
        monsList = next(os.walk(self.path), (None, None, []))[2]
        self.monId = random.choice(monsList)
        self.monName = self.monId[:-4]
        self.genMonTitle()
        return self.path + "\\" + self.monId
    
    def genBossName(self):
        bossList = next(os.walk(self.bossPath), (None, None, []))[2]
        self.monId = random.choice(bossList)
        self.monName = self.monId[:-4]
        self.genMonTitle()
        return self.bossPath + "\\" + self.monId
    
    def genMonTitle(self):
        title = ["Weak ","Sharp ","Speedy ","Sluggish ","Heavy ","Strong ","Small ","Legendary "]
        titleName = random.choice(title)
        self.monName = titleName + self.monName
        print(self.monName)
        print("================")
        if "Weak" in self.monName:
            print("In weak")
            self.hp = self.hp * 0.85
            self.atk = self.atk * 0.85
            self.armor = self.armor * 0.85
            self.spd = self.spd * 0.8
        elif "Strong" in self.monName:
            print("In strong")
            self.atk = self.atk * 1.1
        elif "Small" in self.monName:
            print("In Small")
            self.spd = self.spd * 1.05
        elif "Legendary" in self.monName:
            self.atk = self.atk * 1.2
            self.hp = self.hp * 1.2
            self.armor = self.armor * 1.2
            self.spd = self.spd * 1.2
        elif "Sharp" in self.monName:
            self.atk = self.atk * 1.1
        elif "Heavy" in self.monName:
            self.spd = self.spd * 0.85
            self.atk = self.atk * 1.25
        elif "Speedy" in self.monName:
            self.spd = self.spd * 1.2
        elif "Sluggish" in self.monName:
            self.spd = self.spd * 0.9
            
        self.atk = int(self.atk)
        self.hp = int(self.hp)
        self.armor = int(self.armor)
        self.spd = int(self.spd)
        self.currentHp = self.hp
        
        
    def genStats(self,Char):
        tempList = ["hp","atk","armor","spd"]
        monPoint = 0
        if Char.getDifficulty() == 1:
            monPoint = self.playerStat * 0.8
            print("Fighting easy mon")
        elif Char.getDifficulty() == 2:
            monPoint = self.playerStat
            print("Fighting normal mon")
        elif Char.getDifficulty() == 3:
            monPoint = self.playerStat * 1.2
            print("Fighting hard mon")
        elif Char.getDifficulty() == 4:
            monPoint = self.playerStat * 1.6
            print("Fighting Boss mon")
            
        temp = int(monPoint / 4)
        self.hp = random.randint(1,temp)
        self.atk = random.randint(1,temp)
        self.armor = random.randint(1,temp)
        self.spd = random.randint(1,temp)

        if ((self.hp + self.atk + self.armor + self.spd) <= self.getPlayerStats()):
            remainStats = self.getPlayerStats() - (self.hp + self.atk + self.armor + self.spd)
            remainStats = int(remainStats / 4)
            self.hp += remainStats
            self.armor += remainStats
            self.atk += remainStats
            self.spd += remainStats
            self.currentHp = int(self.hp)

    # Setters   
    def setHp(self,dmg):
        self.currentHp -= dmg
    
    # Getters
    def getMonId(self):
        return self.monId[:-4]
    
    def getMonName(self):
        return self.path + "\\" + self.monId
    
    def getPlayerStats(self):
        return self.playerStat
    
    def getName(self):
        return self.monName
    
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
    