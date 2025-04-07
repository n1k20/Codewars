def first_dup(word: str) -> str | None:
    return next((letter for letter in word if word.count(letter) > 1), None)



