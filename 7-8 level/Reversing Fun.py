def reverse_fun(number):
    for position in range(len(number)):
        number = number[:position] + number[position:][::-1]
    return number
