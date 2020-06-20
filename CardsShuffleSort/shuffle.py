from random import *
from cards import *

def Shuffle(lst):

    for ele in lst:
        num1 = randint(0, 51)
        num2 = randint(0, 51)

        if num1 != num2:
            temp = lst[num1]
            lst[num1] = lst[num2]
            lst[num2] = temp

    return ''

