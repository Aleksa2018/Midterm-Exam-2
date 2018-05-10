"""
===================   TASK 2   ====================
* Name: Roll The Dice
*
* Write a script that will simulate rolling the
* dice. The script should fetch the number of times
* the dice should be "rolled" as user input.
* At the end, the script should print how many times
* each number appeared (1 - 6).
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

from random import randint

import random

jedinica=0
dvojka=0
trojka=0
cetvorka=0
petica=0
sestica=0

for i in range(1000):
    pala=random.randint(1,6)

    if pala==1:
        jedinica+=1

    elif pala==2:
        dvojka +=1

    elif pala==3:
        trojka +=1

    elif pala==4:
        cetvorka +=1

    elif pala==5:
        petica +=1

    elif pala==6:
        sestica +=1


print("Pala jedinica: " + str(jedinica))
print("Pala dvojka: " + str(dvojka))
print("Pala trojka: " + str(trojka))
print("Pala cetvorka: " + str(cetvorka))
print("Pala petica: " + str(petica))
print("Pala sestica: " + str(sestica))