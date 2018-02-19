# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:50:57 2018

@author: jacob
"""
#import Final Fantasy profiles
import random
#import class Fighter
#Classes and Class stats
#Class stats are randomly generated between 1 and one of 6 preset numbers (15,14,13,12,10,8)
#each stat has a different number and the stat numbers differ between classes
#Create cracter


#says player's stats
playLv = '1'
hP = 36
playXp = 10
print(playerName)
print('Lv' + playLv)
print(str(test))
print(hP)
#says imp's stats
impDmg = random.randint(4, 8)
impHp = 8
impXp = 6
#healing items
potions = 50
hi_potion = 150
#attacking
print('You see an imp what do you do?')
input()
impHp = (int(impHp) - int(test))
while impHp >= 0:
    action = input()
    if action == 'z': 
        print(int(figStr))
        if test >= 0: 
            print('you delt ' + str(test) + ' damage')
            impHp = (int(impHp) - int(test))
        if test == 0:
            print('Missed')
        if test == 15:
            print('CRITICAL')
    if impHp <= 0:
        print('enemy terminated')  
        print('you gained ' + str(impXp) + 'XP')
        playXp = (int(playXp + int(impXp)))        
        print('you currently have ' + str(playXp) + 'XP')
        break        
    if impHp >= 0: 
        print('the imp has ' + str(impHp) + ' HP')
        print('the imp attacks you for ' + str(impDmg) + ' damage')
        hP = int(hP) - int(impDmg)
        print('you have ' + str(hP) + ' HP')
        print('what do you next')
#when the imp attacks you
     
#when you heal yourself
    
