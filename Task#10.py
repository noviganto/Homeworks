# Задание №10
# (Sum of the first nth term of Series)
# https://www.codewars.com//kata/555eded1ad94b00403000071

def series_sum(n):
    if n == 0:
        float_answer = 0
    if n == 1:
        float_answer = 1
    if n == 2:
        float_answer = 1.25
    if n > 2:
        float_answer = 1 + 1 / 4

        for i in range(n - 2):
            float_answer = (float_answer + (1 / (4 + (i + 1) * 3)))

    answer = str(f"{float_answer:.{2}f}")

    return answer