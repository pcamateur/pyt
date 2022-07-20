from fileinput import filename
from math import sqrt as sq

import json

li = list()

def ss(startn, endn):
    for x in range(startn, endn):
        for y in range(3, x):
            if x % y == 0:
                break
        else:
            li.append(x)


ss(50000, 5000000)

filename = 'ss.json'

with open(filename, 'a') as f_obj:
    json.dump(li, f_obj)