# Задание №8
# (Operations with sequence)
# https://www.codewars.com//kata/596ddaccdd42c1cf0e00005c

import numpy as np


def calc(a):
    for i in range(len(a)):
        if a[i] > 0:
            a[i] = a[i] ** 2

    a = np.insert(a, 0, 0)
    print(a)

    a[::3] = a[::3] * 3
    print(a)

    a[::5] = a[::5] * (-1)
    print(a)

    np.delete(a, a[0])

    return (sum(a))
