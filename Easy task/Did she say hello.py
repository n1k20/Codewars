def validate_hello(greetings: str) -> bool:
    data = [
        'hello',
        'ciao',
        'salut',
        'hallo',
        'hola',
        'ahoj',
        'czesc']
    greetings = greetings.lower()
    return any(word in greetings for word in data)
