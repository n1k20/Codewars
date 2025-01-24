from math import ceil
def count_number(number: int, x: int) -> int:
    return sum(x % a == 0 for a in range(ceil(x / number), number + 1))

