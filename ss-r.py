from time import time as t
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


# def ssr(stn, etn, a):
#     if a == 1:
#         return 1
#     else:
#         return 
