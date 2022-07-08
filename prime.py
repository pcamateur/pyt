from re import A


class Numbs():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    
    def decide(self):
        if self.a % 2 == 0 and self.b % 2 == 0:
            while self.a % 2 != 0 or self.b % 2 != 0:
                self.a //= 2
                self.b //= 2

        if self.a > self.b:
            temp_a = 0
            while temp_a == self.b:
                temp_a = self.a - self.b
            return temp_a

        elif self.a < self.b:
            temp_b = 0
            while temp_b == self.a:
                temp_b = self.b - self.a
            return temp_b

