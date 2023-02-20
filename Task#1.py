# Задание №1
# (Training JS #32: methods of Math---round() ceil() and floor())
# https://www.codewars.com//kata/5732d3c9791aafb0e4001236

import math

def round_it(n):
    str_n = str(n)
    right = (len(str_n) - 1 - str_n.find('.'))
    left = (len(str_n) - 1 - right)
    if left < right:
        answer = math.ceil(n)
    if left > right:
        answer = math.floor(n)
    if left == right:
        answer = round(n)

    return answer