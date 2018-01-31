# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:53:28 2018

@author: jacob
"""
import random
#Profiles
#Fighter
class Fighter:
    
    global strength
    global dexterity
    global wisdom
    global intelligence
    global constitution
    global charisma
        
    def setStr():
        strength = random.randint(1, 15)
        return strength
    def getStr():
        return strength
    
    def setDex():
        dexterity = random.randint(1, 14)
        return dexterity
    def getDex():
        return dexterity
        
    def setWis():
        wisdom = random.randint(1, 8)
        return wisdom
    def getWis():
        return wisdom
        
    def setInt():
        intelligence = random.randint(1, 12)
        return intelligence
    def getInt():
        return intelligence
        
    def setCon():
        constitution = random.randint(1, 13)
        return constitution
    def getCon():
        return constitution
    
    def setChr():
        charisma = random.randint(1, 10)
        return charisma
    def getChr():
        return charisma
