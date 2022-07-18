from math import gcd


class Maths():
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def gcd(self):
        r = 1
        while True:
            if self.a % 2 != 0 and self.b % 2 != 0:
                self.a //= 2
                self.b //= 2
                r *= 2
            else:
                break

        while True:
            big = max(self.a, self.b)
            small = min(self.a, self.b)
            if small * 2 == big:
                return small * r
            else:
                self.a, self.b = small, big - small

    
    def lcm(self):
        return self.a * self.b // gcd(self.a, self.b)

    
    def screen(self):
        a = self.a // gcd(self.a, self.b)
        b = self.b // gcd(self.b, self.a)
        return f'{a} : {b}'

def run():
    while True:
        first = input('Please input first number: ')
        second = input('Please input second number: ')
        if first != 'q' and second != 'q' and int(first) and int(second):
            this = Maths(int(first), int(second))
            print(this.screen())
        elif first == 'q' and second == 'q':
            print('Thanks for you use the script,Bye!')
            break
        else:
            print('Please input number!')

if __name__ == '__main__':
    run()