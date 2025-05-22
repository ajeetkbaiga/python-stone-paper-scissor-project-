# -*- coding: utf-8 -*-
"""
Created on Wed May 21 21:57:18 2025

@author: HP
"""

import random


computer = random.randint(1,3)
player = int(input("inter your number 1 for stone , 2 for paper , 3 for scissor "))
# stone < paper < scissor < stone
 
# computer choose 
if computer == 1 :
    print("computer choose stone ")
elif computer == 2 :
    print ("computer choose paper ")
else :
    print("computer chooes scissor")
    
# player choose 
if player == 1 :
    print("you choose stone ")
elif player ==2 :
    print("you choose  paper ")
else :
    print ("you choose scissor")

# game condition
while True :
    if computer == player :
        print ("drow")
        break
    
    elif (computer == 1 and player == 2 ) or \
         ( computer == 2 and player == 3 ) or\
           ( computer == 3 and player == 1 ):
               print("you win ")
               break
    else :
        print ("computer win ") 
        break