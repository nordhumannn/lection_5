import math

class UnsupportedValue(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

class RationalFraction:
    
    def __init__(self, a: int, b: int):
        if not isinstance(a, int) or not isinstance(b, int) or b == 0:
            raise UnsupportedValue('Unsupported value')
        self.a = a
        self.b = b

    def __add__(self, other):
        denominator = math.lcm(self.b, other.b)
        numerator = denominator // self.b * self.a + denominator // other.b * other.a

        return RationalFraction(numerator, denominator)

    def __truediv__(self, other):
        denominator = self.b * other.a
        numerator = self.a * other.b

        return RationalFraction(numerator, denominator)

    def __mul__(self, other):
        denominator = self.b * other.b
        numerator = self.a * other.a 

        return RationalFraction(numerator, denominator)

    def __sub__(self, other):
        denominator = math.lcm(self.b, other.b)
        numerator = denominator // self.b * self.a - denominator // other.b * other.a
        gcd = math.gcd(denominator, numerator)

        denominator //= gcd
        numerator //= gcd

        return RationalFraction(numerator, denominator)

    def __gt__(self, other):
        denominator = math.lcm(self.b, other.b)
        numerator_1 = denominator // self.b * self.a
        numerator_2 = denominator // other.b * other.a

        return numerator_1 > numerator_2

    def __lt__(self, other):
        denominator = math.lcm(self.b, other.b)
        numerator_1 = denominator // self.b * self.a
        numerator_2 = denominator // other.b * other.a

        return numerator_1 < numerator_2

    def __str__(self):
        if self.a / self.b > 1:
            return f'{self.a // self.b} ({self.a - self.a // self.b * self.b} / {self.b})'
        if self.a == self.b:
            return '1'   
        gcd = math.gcd(self.a, self.b)
        self.a // gcd
        self.b // gcd
        return f'{self.a}/{self.b}'   

num_1 = RationalFraction(1, 2)
num_2 = RationalFraction(2, 4)
num_3 = RationalFraction(3, 7)

print(num_1 + num_2)
