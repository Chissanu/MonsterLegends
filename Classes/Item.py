import os
from pathlib import Path
import random

class Item:
    def __init__(self):
        self.name = "default"
        self.price = 20
        self.itemList = []
        self.upgradeList = []
        self.path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.path = self.path.parent.absolute()
        self.upgradePath = str(self.path) + "\\Assets\\upgrade"
        self.path = str(self.path) + "\\Assets\\Item"
        self.genUpgrade1List()
    
    # Getters
    def genItemList(self):
        temp = next(os.walk(self.path), (None, None, []))[2]
        for word in temp:
            self.itemList.append(word[:-4])
        return self.itemList
    
    def genUpgrade1List(self):
        temp = next(os.walk(self.upgradePath), (None, None, []))[2]
        for word in temp:
            if word[0] == str(1):
                self.upgradeList.append(word)
        print("here", self.upgradeList)
        return self.upgradeList
    
    
    def getItemList(self):
        return next(os.walk(self.path), (None, None, []))[2]
    
    def getUpgradeList(self):
        return self.upgradeList
    
    def getItemPath(self,item):
        return self.path + "\\" + item
    
    def getUpgrade1Path(self,item):
        return self.upgradePath + "\\" + item
    
    def getUpgrade2Path(self,item):
        return self.upgradePath + "\\" + item
    
    def getUpgrade3Path(self,item):
        return self.upgradePath + "\\" + item
    
    def getUpgrade4Path(self,item):
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
    
    