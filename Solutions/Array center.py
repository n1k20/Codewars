def array_center(array: list[int]) -> list[int]:
    min_array = min(array)
    average = sum(array) / len(array)
    return [i for i in array if abs(i - average) < min_array]
