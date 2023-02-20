# Задание №9
# (Transpose two strings in an array)
# https://www.codewars.com//kata/581f4ac139dc423f04000b99

def transpose_two_strings(arr):
    list_assistant = []

    if len(arr[0]) < len(arr[1]):

        for i in range(len(arr[0])):
            list_assistant.append(arr[0][i] + ' ' + arr[1][i] + '\n')

        for i in range(len(arr[1]) - len(arr[0]) - 1):
            list_assistant.append('  ' + arr[1][i + len(arr[0])] + '\n')

        list_assistant.append('  ' + arr[1][len(arr[1]) - 1])

    if len(arr[0]) > len(arr[1]):

        for i in range(len(arr[1])):
            list_assistant.append(arr[0][i] + ' ' + arr[1][i] + '\n')

        for i in range(len(arr[0]) - len(arr[1]) - 1):
            list_assistant.append(arr[0][i + len(arr[1])] + '  ' + '\n')

        list_assistant.append(arr[0][len(arr[0]) - 1] + '  ')

    if len(arr[0]) == len(arr[1]):
        for i in range(len(arr[1]) - 1):
            list_assistant.append(arr[0][i] + ' ' + arr[1][i] + '\n')
        list_assistant.append(arr[0][len(arr[1]) - 1] + ' ' + arr[1][len(arr[1]) - 1])

    transpose_str = str()

    for i in list_assistant:
        transpose_str = transpose_str + i

    return transpose_str