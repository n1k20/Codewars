def correct_polish_letters(words: str) -> str:
    data = {'ą': 'a',
            'ć': 'c',
            'ę': 'e',
            'ł': 'l',
            'ń': 'n',
            'ó': 'o',
            'ś': 's',
            'ź': 'z',
            'ż': 'z'}
    return ''.join([data[letter] if letter in 'ąćęłńóśźż' else letter for letter in words])