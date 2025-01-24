def rank_of_element(array: list[int], i) -> int:
    return sum(p <= array[i] if k < i else p < array[i] for k, p in enumerate(array))
