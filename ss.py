from time import time as t

s = t()
li = list()

# datas = [a for a in range(5, 50000) if a % 2 != 0]

# for x in datas:
for x in range(5, 50000):
    for y in range(2, x):
        if x % y == 0:
            break
    
    else:
        li.append(x)

e = t()

# print(li)
print(len(li))
print(e - s)