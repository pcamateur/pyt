'''航空运单号列表'''

import json

lis = []

def getList():
    for b in range(3700000, 3800000):
        c = b % 7
        if b < 10:
            data = '000000' + str(b) + str(c)
        elif b < 100:
            data = '00000' + str(b) + str(c)
        elif b < 1000:
            data = '0000' + str(b) + str(c)
        elif b < 10000:
            data = '000' + str(b) + str(c)
        elif b < 100000:
            data = '00' + str(b) + str(c)
        elif b < 1000000:
            data = '0' + str(b) + str(c)
        else:
            data = str(b) + str(c)

        lis.append(data)

getList()

filename = 'billss.json'

with open(filename, 'w') as lists:
    json.dump(lis, lists)