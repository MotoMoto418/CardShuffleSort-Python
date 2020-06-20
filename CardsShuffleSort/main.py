from cards import *
from shuffle import *
from sort import *

enums = []

print("")
print("The original deck is: ")
for card in Cards:
    print(card, "\n")


for crd in Cards:              #to get a list of enums
    x = Cards_dic.get(crd)
    enums.append(x)

Shuffle(enums)

print("The shufled numbers are: ")
for enum in enums:
    print(enum)
print("")
print("The corresponding shuffled deck is: ")
for i in enums:
    print(Rev_cards_dic[i])     #getting values from reversed card dictionary

Sort(enums)

print("")
print("The sorted numbers are: ")
for enum in enums:
    print(enum)
print("")
print("The corresponding sorted deck is: ")
for i in enums:
    print(Rev_cards_dic[i])