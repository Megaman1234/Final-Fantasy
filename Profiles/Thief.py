# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:01:09 2018

@author: jacob
"""

import random
class Thief(object):
    def __init__(self):    
        self.maxStr = 10
        self.minStr = 1
        self.maxDex = 15
        self.minDex = 1
        self.maxWis = 8
        self.minWis = 1
        self.maxInt = 14
        self.minInt = 1
        self.maxCon = 13
        self.minCon = 1
        self.maxChar = 12
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
        dexterity = random.randint(self.minDex, self.maxDex)
    def getDex():
        return dexterity
        
    def setWis(self):
        global wisdom        
        wisdom = random.randint(self.minWis, self.maxWis)
    def getWis():
        return wisdom
        
    def setInt(self):
        global intelligence  
        intelligence = random.randint(self.minInt, self.maxInt)
    def getInt():
        return intelligence
        
    def setCon(self):
        global constitution
        constitution = random.randint(self.minCon, self.maxCon)
    def getCon():
        return constitution
    
    def setChr(self):
        global charisma
        charisma = random.randint(self.minChr, self.maxChr)
    def getChr():
        return charisma

    def create(self):
        self.setStr()
        self.setDex()
        self.setWis()
        self.setInt()
        self.setCon()
        self.setChr()        
        return [strength, dexterity, wisdom, intelligence, constitution, charisma]