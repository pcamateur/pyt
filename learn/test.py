from random import randint as ri
import json

# lisa = [ri(1, 65535) for _x in range(50000)]

# slis = set(lisa)

# while len(slis) < 50000:
#     tempa = 50000 - len(slis)
#     tempb = tempa / 50000
#     tempc = tempb * 100
#     tempd = 100 - tempc
    
#     lisa.append(ri(1, 65535))
#     slis = set(lisa)
    
#     strc = str(int(tempd))
#     print(strc + '%')
    
# lisb = [_y for _y in range(65535)]
# lisc = [ri(1,65535) for _z in range(65535)]

# kcc = set(lisb) - set(lisc)

# print(len(list(kcc)))

# ba = 65535 - len(list(kcc))
# bb = ba / 65535
# bc = bb * 100
# bd = 100 - bc
# print(str(int(bd)) + str('%'))

    
# print('Done!')

# def randomums(n):
#     lis = [ri(1, 65535) for _x in range(n)]
#     while len(set(lis)) < n:
#         for _y in range(n - len(set(lis))):
#             lis.append(ri(1, 65535))
    
#     return lis

# numbs = int(input('Please input numbs: '))

# print(len(set(randomums(numbs))))

# print(sorted(set(randomums(numbs))))



# def rnd(n):
#     lis = [ri(1, 65535) for _x in range(n)]
#     while len(set(lis)) < n:
#         for _y in range(n - len(set(lis))):
#             lis.append(ri(1, 65535))
            
#     dic = {}
#     for _i, _j in enumerate(sorted(set(lis)), 1):
#         dic[_i] = _j
        
#     return dic
    

# numbs = int(input('Please input numbs: '))

# print(rnd(numbs))


# lst = [x for x in range(65583)]
# lis = []
# dic = {}
# for x in lst:
#     if x % 2 == 0 and (x + 1) % 3 == 0 and (x + 2) % 4 == 0 and (x + 3) % 5 == 0 and (x + 4) % 6 == 0:
#         lis.append(x)
        
# print(lis)         

# x = 2
# lt = [2]
# while x < 65535:
#     x += 60
#     lt.append(x)
    
# print(lt)

# if lt == lis:
#     print('OK!')


# 
lis = [x for x in range(100000)]
lst = []
for x in lis:
    if x % 2 == 0 and (x + 1) % 3 == 0 and (x + 2) % 4 == 0 and (x + 3) % 5 == 0:
        lst.append(x)
        
print(lst)
print(len(lst))