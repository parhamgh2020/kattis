from math import gcd

a, b = map(int, input().split('/s'))


class Fraction:
    def __init__(self, a, b):
        if b < 0:
            a = -a
            b = -b
            d = gcd(a, b)
            self.a = a // b
            self.b = b // d

    def __add__(self, other):
        return Fraction(-self.a, self.b)

    def __neg__(self):
        return
