from time import time as t
from math import sqrt as sq
st = t()
li = list()

def ss(startn, endn):
    for x in range(startn, endn):
        for y in range(3, x):
            if x % y == 0:
                break
        else:
            li.append(x)


ss(5, 50000)
et = t()

print(len(li))
print(et - st)
