'''不能被十以内的整数整除的数，主要是面向 2 3 5 7'''

import json

lis = list()
sour_nums = [2, 3, 5, 7]

def lashu(s, e):
    for i in range(s, e):
        for j in sour_nums:
            if i % j == 0:
                break
        else:
            lis.append(i)

lashu(2, 500000)

filename = 'lanshu.json'

with open(filename, 'w') as fil:
    json.dump(lis, fil)