from random import *
from cards import *

def Shuffle(lst):
    i = 0
    emp = []

    while i < 52:
        num1 = randint(0, 51)
        num2 = randint(0, 51)

        if num1 != num2 and (num1, num2) not in emp:
            temp = lst[num1]
            lst[num1] = lst[num2]
            lst[num2] = temp
            i += 1
            emp.append((num1, num2))

    return ''
