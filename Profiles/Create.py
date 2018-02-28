# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:08:10 2018

@author: jacob
"""
from Profiles.Fighter import *
from Profiles.Thief import *
from Profiles.Mage import *

print('lets create a character')


print('Next, What class do you want to be?')
print('each class has its own stregnth and weaknesses so choose wisely')

print(' F - Fighter: a brash, stotic hero ready to fight at a moments notice')
print(' T - Thief: A sneaky but clever hero, with a tool for every situation')
print(' M - Mage: A wise and elegant hero that use magic to fight evil')

classChoice = input()
while createChoice:
    if classChoice.upper() == 'F':
        F = Fighter()   
        attributes = F.create()
    if classChoice.upper() == 'T':
        T = Thief()
        attributes = T.create()
    if classChoice.upper() == 'M':
        M = Mage()
        attributes = M.create()        
    print('strength = ' + str(attributes[0]))
    print('dexerity = ' + str(attributes[1]))
    print('wisdom = ' + str(attributes[2]))
    print('intelligence = ' + str(attributes[3]))
    print('constitution = ' + str(attributes[4]))
    print('charisma = ' + str(attributes[5]))
    createChoice = input('do you want to reroll Y/N? ')
if createChoice.upper() == 'Y':
    createChoice = True
if createChoice.upper() == 'N':
    createChoice = False
