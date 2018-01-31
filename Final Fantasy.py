# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:50:57 2018

@author: jacob
"""
import random
#Classes and Class stats
#Class stats are randomly generated between 1 and one of 6 preset numbers (15,14,13,12,10,8)
#each stat has a different number and the stat numbers differ between classes
#Create cracter
print('Welome to Final Fantasy.py')
print('lets create a character')
print('First, What is your Name?')
input()
playerName = input
print('Next, What class do you want to be?')
print('Fighter - a brash, stotic hero ready to fight at a moments notice')
print('Theif - A sneaky but clever hero, with a tool for every situation')
print('Mage - A wise and elegant hero that use magic to fight evil')
print('each class has its own stregnth and weaknesses so choose wisely')
input()
choice = input   
if choice == 'fighter':
    return class Fighter
#says player's stats
playLv = '1'
hP = 36
playXp = 10
print(playerName)
print('Lv' + playLv)
print(str(figStr))
print(hP)
#says imp's stats
impDmg = 3
impHp = 8
impXp = 10
#healing items
potions = 50
hi_potion = 150
#attacking
print('You see an imp what do you do?')
input()
action = input()
if action == 'attack': 
    print(int(figStr))
    playXp = (int(playXp + int(impXp)))
if figStr >= 0: 
    print('you delt ' + str(figStr) + ' damage')
    impHp = (int(impHp) - int(figStr))
#when the imp attacks you
if impHp <= 0:
    print('enemy terminated')  
    print('you gained ' + str(impXp) + 'XP')
    print('you currently have ' + str(playXp) + 'XP')
if impHp >= 0:    
    print('the imp has ' + str(impHp) + ' HP')
    print('the imp attacks you for 3 damage')
    hP = int(hP) - int(impDmg)
    print('you have ' + str(hP) + ' HP')
#when you heal yourself
