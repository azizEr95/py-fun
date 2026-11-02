class Calculator(object):
    _instance = None

    NUMBERS = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'null': 0, 'eins': 1, 'zwei': 2, 'drei': 3, 'vier': 4, 'fünf': 5, 'sechs': 6, 'sieben': 7, 'acht': 8, 'neun': 9,
        'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9,
        'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9,
        '零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
        'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6, 'vii': 7, 'viii': 8, 'ix': 9, 'x': 10,
    }

    def num(_self, x):
        # Eingabe in Text umwandeln, Leerzeichen weg, alles klein
        text = str(x).strip().lower()

        # Suche in der Liste der definierten Zahlen
        if text in _self.NUMBERS:
            return _self.NUMBERS[text]

        # Ist es eine ganze Zahl? ("1", "-3")
        if text.lstrip('-').isdigit():
            return int(text)

        # Sonst Kommazahl ("1.600")
        return float(text)
    
    def add(_self, a, b):
        return _self.num(a) + _self.num(b)

    def sub(_self, a, b):
        return _self.num(a) - _self.num(b)

    def mul(_self, a, b):
        return _self.num(a) * _self.num(b)

    def div(_self, a, b):
        b = _self.num(b)
        return _self.num(a) / b if b != 0 else None

    def factorize(_self, n):
        n = _self.num(n)
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors

    def __init__(self):
        pass