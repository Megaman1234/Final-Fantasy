# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 18:59:57 2018

@author: jacob
"""
import random
#Fighter Profile clas
class Fighter:
    def __init__(self):
        self.maxStr = 15
        self.minStr = 1
        self.maxDex = 14
        self.minDex = 1
        self.maxWis = 8
        self.minWis = 1
        self.maxInt = 12
        self.minInt = 1
        self.maxCon = 13
        self.minCon = 1
        self.maxChar = 10
        self.minChar = 1
    
        self.strength = 0
        self.dexterity = 0
        self.wisdom = 0
        self.intelligence = 0
        self.constitution = 0
        self.charisma = 0
        
    def setStr(self):
        global strength 
        strength= random.randint(self.minStr, self.maxStr)

    def getStr():
        return strength
    
    def setDex(self):
        global dexterity        
        dexterity = random.randint(1, 14)
    def getDex():
        return dexterity
        
    def setWis(self):
        global wisdom        
        wisdom = random.randint(1, 8)
    def getWis():
        return wisdom
        
    def setInt(self):
        global intelligence  
        intelligence = random.randint(1, 12)
    def getInt():
        return intelligence
        
    def setCon(self):
        global constitution
        constitution = random.randint(1, 13)
    def getCon():
        return constitution
    
    def setChr(self):
        global charisma
        charisma = random.randint(1, 10)
    def getChr():
        return charisma

    def create():
        Fighter.setStr()
        Fighter.setDex()
        Fighter.setWis()
        Fighter.setInt()
        Fighter.setCon()
        Fighter.setChr()        
        return [strength, dexterity, wisdom, intelligence, constitution, charisma]
