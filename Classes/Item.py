import os
from pathlib import Path
import random

class Item:
    def __init__(self):
        self.name = "default"
        self.price = 20
        self.itemList = []
        self.upgradeList = [0,0,0,0]
        self.path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.path = self.path.parent.absolute()
        self.upgradePath = str(self.path) + "\\Assets\\upgrade"
        self.path = str(self.path) + "\\Assets\\Item"
    
    # Getters
    def genItemList(self):
        temp = next(os.walk(self.path), (None, None, []))[2]
        for word in temp:
            self.itemList.append(word[:-4])
        return self.itemList
    
    def genCurrentUpgrade(self,currLv):
        temp = next(os.walk(self.upgradePath), (None, None, []))[2]
        for item in temp:
            # Helmet
            if currLv[0] == 1:
                self.upgradeList[0] = [item for item in temp if "1a" in item]
            elif currLv[0] == 2:
                self.upgradeList[0] = [item for item in temp if "2a" in item]
            elif currLv[0] == 3:
                self.upgradeList[0] = [item for item in temp if "3a" in item]  
            elif currLv[0] == 4:
                self.upgradeList[0] = [item for item in temp if "4a" in item]  
            # Chestplate
            if currLv[1] == 1:
                self.upgradeList[1] = [item for item in temp if "1b" in item]
            elif currLv[1] == 2:
                self.upgradeList[1] = [item for item in temp if "2b" in item]
            elif currLv[1] == 3:
                self.upgradeList[1] = [item for item in temp if "3b" in item]  
            elif currLv[1] == 4:
                self.upgradeList[1] = [item for item in temp if "4b" in item] 
            # Legging
            if currLv[2] == 1:
                self.upgradeList[2] = [item for item in temp if "1c" in item]
            elif currLv[2] == 2:
                self.upgradeList[2] = [item for item in temp if "2c" in item]  
            elif currLv[2] == 3:
                self.upgradeList[2] = [item for item in temp if "3c" in item]  
            elif currLv[2] == 4:
                self.upgradeList[2] = [item for item in temp if "4c" in item]  
            # Boot    
            if currLv[3] == 1:
                self.upgradeList[3] = [item for item in temp if "1d" in item]
            elif currLv[3] == 2:
                self.upgradeList[3] = [item for item in temp if "2d" in item]  
            elif currLv[3] == 3:
                self.upgradeList[3] = [item for item in temp if "3d" in item]  
            elif currLv[3] == 4:
                self.upgradeList[3] = [item for item in temp if "4d" in item]  
                
            self.upgradeList = [x[0] for x in self.upgradeList]
            
        return self.upgradeList
                                           

    def getItemList(self):
        return next(os.walk(self.path), (None, None, []))[2]
    
    def getUpgradeList(self):
        return self.upgradeList
    
    def getItemPath(self,item):
        return self.path + "\\" + item
    
    def getUpgradePath(self,item):
        return self.upgradePath + "\\" + item

    
    def getName(self,img):
        self.name = img[:-4]
        return self.name
    
    def getNameTag(self,img,price):
        self.name = img[:-4] + " " + str(price) + "G"
        return self.name
    
    def getUpgradeTag(self,img,price):
        self.name = img[3:-4] + " " + str(price) + "G"
        return self.name
    
    