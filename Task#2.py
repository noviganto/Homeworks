# Задание №2
# (Add new item (collections are passed by reference))
# https://www.codewars.com//kata/566dc05f855b36a031000048

def add_extra(list_of_numbers):
    new_list_of_numbers = list_of_numbers.copy()
    new_list_of_numbers.append(13)
    return new_list_of_numbers