"""
===================   TASK 3  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def getSum(piece):
    if len(piece) == 0:
        return 0
    else:
        return piece[0] + getSum(piece[1:])

print(getSum([9, 8, 7, 6, 5]))



