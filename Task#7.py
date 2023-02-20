# Задание №7
# (Count the number of cubes with paint on)
# https://www.codewars.com//kata/5763bb0af716cad8fb000580

def count_squares(cuts):
    x = (cuts + 1) * (cuts + 1) * (cuts + 1)
    if cuts > 1:
        x = x - (cuts - 1) * (cuts - 1) * (cuts - 1)
    return x