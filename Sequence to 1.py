def seq_to_one(number: int) -> list[int]:
    step = (-1) ** (number > 0)
    return list(range(number, 1 + step, step))
