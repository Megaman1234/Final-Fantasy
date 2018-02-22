# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:26:24 2018

@author: jacob
"""

from Fighter import Fighter
from Thief import Thief
from Mage import Mage

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
        

        

        
        
