class Calculator(object):
    _instance = None

    NUMBERS = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
        'null': 0, 'eins': 1, 'zwei': 2, 'drei': 3, 'vier': 4, 'fünf': 5, 'fuenf': 5, 'sechs': 6, 'sieben': 7, 'acht': 8, 'neun': 9, 'zehn': 10,
        'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9, 'diez': 10,
        'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10,
        '零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
        'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6, 'vii': 7, 'viii': 8, 'ix': 9, 'x': 10,
    }

    # Singleton pattern by overloading the new operator, see
    # https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons

    def __new__(cls):
        # Singleton: immer dieselbe Instanz zurückgeben
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def num(self, x):
        # None zählt als 0
        if x is None:
            return 0

        # Zahlen direkt zurückgeben
        if isinstance(x, (int, float)):
            return x

        # Eingabe in Text umwandeln, Leerzeichen weg, alles klein
        text = str(x).strip().lower()

        # Suche in der Liste der definierten Zahlen
        if text in self.NUMBERS:
            return self.NUMBERS[text]

        # Ganze Zahl ("1", "-3")
        try:
            return int(text)
        except ValueError:
            pass

        # Kommazahl ("1.600"), sonst 0
        try:
            return float(text)
        except ValueError:
            return 0

    def add(self, a, b):
        return self.num(a) + self.num(b)

    def sub(self, a, b):
        return self.num(a) - self.num(b)

    def mul(self, a, b):
        return self.num(a) * self.num(b)

    def div(self, a, b):
        b = self.num(b)
        return self.num(a) / b if b != 0 else float('inf')

    def factorize(self, n):
        n = self.num(n)
        if isinstance(n, float):
            if not n.is_integer():
                raise ValueError(f"cannot factorize non-integer: {n}")
            n = int(n)
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