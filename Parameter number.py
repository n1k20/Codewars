from math import gcd

def parameter(number: int) -> int:
    sum_n, prod_n = 0, 1
    for i in str(number):
        sum_n += int(i)
        prod_n *= int(i)
    return sum_n * prod_n / gcd(sum_n, prod_n)
