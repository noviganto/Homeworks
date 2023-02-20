# Задание №3
# (Is your period late?)
# https://www.codewars.com//kata/578a8a01e9fd1549e50001f1

import datetime


def period_is_late(last, today, cycle_length):
    if (today - last).days > cycle_length:
        period_is_late = True
    else:
        period_is_late = False

    return period_is_late