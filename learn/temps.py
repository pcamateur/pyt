def sum(a,b):
    while True:
        if a > b and a % b == 0:
            return [a,b]
        else:
            a += 1

print(sum(6,8))