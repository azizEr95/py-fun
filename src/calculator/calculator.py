class Calculator(object):
    _instance = None
    # names of single-digit numbers: English, German, Spanish, Russian, Chinese
    _digits = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "null": 0,
        "eins": 1,
        "zwei": 2,
        "drei": 3,
        "vier": 4,
        "fünf": 5,
        "sechs": 6,
        "sieben": 7,
        "acht": 8,
        "neun": 9,
        "cero": 0,
        "uno": 1,
        "dos": 2,
        "tres": 3,
        "cuatro": 4,
        "cinco": 5,
        "seis": 6,
        "siete": 7,
        "ocho": 8,
        "nueve": 9,
        "ноль": 0,
        "один": 1,
        "два": 2,
        "три": 3,
        "четыре": 4,
        "пять": 5,
        "шесть": 6,
        "семь": 7,
        "восемь": 8,
        "девять": 9,
        "零": 0,
        "一": 1,
        "二": 2,
        "三": 3,
        "四": 4,
        "五": 5,
        "六": 6,
        "七": 7,
        "八": 8,
        "九": 9,
    }

    # values of Latin (Roman) numerals
    _roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def add(_self, a, b):
        return _self._num(a) + _self._num(b)

    def sub(_self, a, b):
        return _self._num(a) - _self._num(b)

    def mul(_self, a, b):
        return _self._num(a) * _self._num(b)

    def div(_self, a, b):
        return _self._num(a) / _self._num(b)

    def factorize(_self, n):
        n = _self._num(n)
        factors = []
        p = 2
        while p * p <= n:
            while n % p == 0:
                factors.append(p)
                n //= p
            p += 1
        if n > 1:
            factors.append(n)
        return factors

    # convert argument (number, digit string, number name, Roman numeral) to a number
    def _num(_self, x):
        if not isinstance(x, str):
            return x
        s = x.strip()
        try:
            return int(s)
        except ValueError:
            pass
        try:
            return float(s)
        except ValueError:
            pass
        if s.lower() in _self._digits:
            return _self._digits[s.lower()]
        if s and all(c in _self._roman for c in s.upper()):
            return _self._from_roman(s.upper())
        raise ValueError(f'not a number: "{x}"')

    # convert Roman numeral, e.g. "IV" -> 4
    def _from_roman(_self, s):
        total = 0
        for i, c in enumerate(s):
            v = _self._roman[c]
            if i + 1 < len(s) and v < _self._roman[s[i + 1]]:
                total -= v
            else:
                total += v
        return total

    def __init__(self):
        pass

    # Singleton pattern by overloading the new operator, see
    # https://stackoverflow.com/questions/31875/is-there-a-simple-elegant- way-to-define-singletons
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
