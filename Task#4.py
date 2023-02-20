# Задание №4
# (Filtering even numbers (Bug Fixes))
# https://www.codewars.com//kata/566dc566f6ea9a14b500007b

def kata_13_december(lst):
    newlist = []
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            newlist.append(lst[i])
    return newlist