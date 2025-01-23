def beeramid(bonus: int, price: int) -> int:
    can_buy, counter_level = 0, bonus // price
    while (counter_level + 1) ** 2 <= can_buy:
        counter_level += 1
        can_buy -= counter_level ** 2
    return counter_level
