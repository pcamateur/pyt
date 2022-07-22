from base64 import encode
import json
from textwrap import indent

files = f'D:\git\github\pcamateur\pyt\learn\\2020.json'

with open(files, 'r', encoding='utf-8') as jd:
    data = json.load(jd, encoding = 'utf8')

def querys(data, infor):
    try:
        if infor in data:
            
            pr = infor[0:2]
            prs = pr + '0000'
            province = data[prs]
            
            ci = infor[0:4]
            cis = ci + '00'
            city = data[cis]
            
            district = data[infor]
            
            total = province + city + district
            return total

    except Exception as e:
        print(e)


def run():
    infor =  input('Please in put nubers:')

    print(querys(data, infor))


if __name__ == '__main__':
    run()

