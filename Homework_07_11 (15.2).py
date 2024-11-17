#Було додано перевірку знаменника нул, у class Fraction:

from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може дорівнювати нулю.")
        self.a = a
        self.b = b

    def simplify(self):
        """Скорочує дріб."""
        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor

    def __mul__(self, other):
        """Множення дробів."""
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __add__(self, other):
        """Додавання дробів."""
        new_numerator = self.a * other.b + other.a * self.b
        new_denominator = self.b * other.b
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Віднімання дробів."""
        numerator = self.a * other.b - other.a * self.b
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        """Перевірка на рівність."""
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        """Перевірка на 'більше'."""
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        """Перевірка на 'менше'."""
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')