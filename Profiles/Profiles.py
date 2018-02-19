# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:26:24 2018

@author: jacob
"""
import random
from Fighter import Fighter

class Profiles:
    def __init__(self):
        self.Name = ''
        self.Gender = ''
        self.Class = ''
        self.Attributes = ''
        self.strength = ''
        self.dexterity = ''
        self.wisdom = ''
        self.intelligence = ''
        self.constitution = ''
        self.charisma = ''
        
    def setName(self):
        self.Name = input('What is your name?')
        
    
    def setGender(self):
        self.Gender = input('Are you Male or Female')
        
    def setClass(self):
        print('Next, What class do you want to be?')
        print('each class has its own stregnth and weaknesses so choose wisely')
        print(' F - Fighter: a brash, stotic hero ready to fight at a moments notice')
        print(' T - Thief: A sneaky but clever hero, with a tool for every situation')
        self.Class = input(' M - Mage: A wise and elegant hero that use magic to fight evil')

        
    def setAttributes(self):
        self.Attributes = (self.strength, self.dexterity, self.wisdom, self.intelligence, self.constitution, self.charisma)
    
    def setStrength(self):
        Fighter.setStr 

    def setDexterity(self):
        Fighter.setDex

    def setWisdon(self):
        Fighter.setWis
    
    def setIntelligence(self):
        Fighter.setInt

    def setConstitution(self):
        Fighter.setCon

    def setCharisma(self):
        Fighter.setChr        
    

class Class:
    None
    
class Attributes:
    None

class Gender:
    None
        
class Thief:
    
    maxStr = 10
    minStr = 1
    maxDex = 15
    minDex = 1
    maxWis = 8
    minWis = 1
    maxInt = 14
    minInt = 1
    maxCon = 13
    minCon = 1
    maxChar = 12
    minChar = 1
    
    strength = 0
    dexterity = 0
    wisdom = 0
    intelligence = 0
    constitution = 0
    charisma = 0
        
    def setStr(minStr=minStr, maxStr=maxStr):
        global strength 
        strength= random.randint(minStr, maxStr)

    def getStr():
        return strength
    
    def setDex(minDex=minDex, maxDex=maxDex):
        global dexterity        
        dexterity = random.randint(minDex, maxDex)
    def getDex():
        return dexterity
        
    def setWis(minWis=minWis, maxWis=maxWis):
        global wisdom        
        wisdom = random.randint(min, 8)
    def getWis():
        return wisdom
        
    def setInt(minInt=minInt, maxInt=maxInt):
        global intelligence  
        intelligence = random.randint(1, 12)
    def getInt():
        return intelligence
        
    def setCon(minCon=minCon, maxCon=maxCon):
        global constitution
        constitution = random.randint(1, 13)
    def getCon():
        return constitution
    
    def setChr(minChar=minChar, maxChar=maxChar):
        global charisma
        charisma = random.randint(1, 10)
    def getChr():
        return charisma

    def create():
        Thief.setStr()
        Thief.setDex()
        Thief.setWis()
        Thief.setInt()
        Thief.setCon()
        Thief.setChr()        
        return [strength, dexterity, wisdom, intelligence, constitution, charisma]
        
class Mage:
    
    maxStr = 10
    minStr = 1
    maxDex = 12
    minDex = 1
    maxWis = 14
    minWis = 1
    maxInt = 15
    minInt = 1
    maxCon = 13
    minCon = 1
    maxChar = 8
    minChar = 1
    
    strength = 0
    dexterity = 0
    wisdom = 0
    intelligence = 0
    constitution = 0
    charisma = 0
        
    def setStr(minStr=minStr, maxStr=maxStr):
        global strength 
        strength= random.randint(minStr, maxStr)

    def getStr():
        return strength
    
    def setDex(minDex=minDex, maxDex=maxDex):
        global dexterity        
        dexterity = random.randint(1, 14)
    def getDex():
        return dexterity
        
    def setWis(minWis=minWis, maxWis=maxWis):
        global wisdom        
        wisdom = random.randint(1, 8)
    def getWis():
        return wisdom
        
    def setInt(minInt=minInt, maxInt=maxInt):
        global intelligence  
        intelligence = random.randint(1, 12)
    def getInt():
        return intelligence
        
    def setCon(minCon=minCon, maxCon=maxCon):
        global constitution
        constitution = random.randint(1, 13)
    def getCon():
        return constitution
    
    def setChr(minChar=minChar, maxChar=maxChar):
        global charisma
        charisma = random.randint(1, 10)
    def getChr():
        return charisma

    def create():
        Mage.setStr()
        Mage.setDex()
        Mage.setWis()
        Mage.setInt()
        Mage.setCon()
        Mage.setChr()        
        return [strength, dexterity, wisdom, intelligence, constitution, charisma]
        
        
