from time import time as t

s = t()
li = list()

for x in range(4, 50000):
    for y in range(2, x):
        if x % y == 0:
            break
    
    else:
        li.append(x)

e = t()

print(li)
print(e - s)