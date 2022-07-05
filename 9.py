from random import randint as rn
lis = [i for i in range(5)]
x = rn(0,9)
lis.append(x)
print(lis)
liss = []
cns = 0
for x in range(0, len(lis)):
    for y in range(x + 1, len(lis)):
        if lis[x] == lis[y]:
            cns += 1
            liss.append(lis[x])
            break
if cns != 0:
    print("true")
    print(liss)
else:
    print('False')

