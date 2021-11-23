import os
from pathlib import Path
import random

class Item:
    def __init__(self):
        self.name = "default"
        self.price = 20
        self.itemList = []
        self.path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.path = self.path.parent.absolute()
        self.path = str(self.path) + "\Assets\Item"
    
    # Getters
    def genItemList(self):
        temp = next(os.walk(self.path), (None, None, []))[2]
        for word in temp:
            self.itemList.append(word[:-4])
        return self.itemList
    
    def getItemList(self):
        return next(os.walk(self.path), (None, None, []))[2]
    
    def getItemPath(self,item):
        #return self.path + "\\" + item + ".png"
        return self.path + "\\" + item
    
    def getName(self,img):
        self.name = img[:-4]
        return self.name
    
    def getNameTag(self,img,price):
        self.name = img[:-4] + " " + str(price) + "G"
        return self.name
    