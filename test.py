# from time import time as t
# from math import sqrt as sq
# st = t()
# li = list()

# def ss(startn, endn):
#     for x in range(startn, endn):
#         z = int(sq(x))
#         for y in range(2, z + 1):
#             if x % y == 0:
#                 break
#         else:
#             li.append(x)


# ss(5, 50000)
# et = t()

# print(len(li))
# print(et - st)

from math import sqrt as sq
from time import time as t
st = t()


def getss(n):
    
    return filter(lambda x: not [x % i for i in range(2, int(sq(x)) + 1) if x % i == 0], range(2, n + 1))

  

print(len(list(getss(500000))))

et = t()

print(et - st)

