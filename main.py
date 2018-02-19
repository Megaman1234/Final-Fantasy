# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:24:38 2018

@author: jacob
"""
from Fighter import Fighter
#Charater creator
print('Welome to Final Fantasy.py')
print('lets create a character')


print('Next, What class do you want to be?')
print('each class has its own stregnth and weaknesses so choose wisely')

print(' F - Fighter: a brash, stotic hero ready to fight at a moments notice')
print(' T - Thief: A sneaky but clever hero, with a tool for every situation')
print(' M - Mage: A wise and elegant hero that use magic to fight evil')

classChoice = input()
createChoice = True
while createChoice:
    if classChoice.upper() == 'F':
        attributes = Fighter.create()    
    if classChoice.upper() == 'T':
        attributes = Thief.create()
    if classChoice.upper() == 'M':
        attributes = Mage.create        
    print('strength = ' + str(attributes[0]))
    print('dexerity = ' + str(attributes[1]))
    print('wisdom = ' + str(attributes[2]))
    print('intelligence = ' + str(attributes[3]))
    print('constitution = ' + str(attributes[4]))
    print('charisma = ' + str(attributes[5]))
    createChoice = input('do you want to reroll Y/N? ')
    if createChoice.upper() == 'n':
        createChoice = False
        
