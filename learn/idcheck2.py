import json
from datetime import datetime as dt

def getID():
    ids = input('Please input you IDs number:')
    if len(ids) != 17 or int(ids[6:10]) > 2022 or int(ids[6:10]) < 1920 or int(ids[10:12]) > 12 or int(ids[10:12]) == 00 or int(ids[12:14]) == 00 or int(ids[12:14]) > 31:
        while True:
            ids = input('Please type right IDs Number(17bit):')
            if len(ids) != 17 or int(ids[6:10]) > 2022 or int(ids[6:10]) < 1920 or int(ids[10:12]) > 12 or int(ids[10:12]) == 00 or int(ids[12:14]) == 00 or int(ids[12:14]) > 31:
                continue
            elif ids.isdigit():
                break
            else:
                continue
    
    return ids
    

def check(ids):
    xsl = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

    modsl = [1, 0, 'x', 9, 8, 7, 6, 5, 4, 3, 2]

    idss = [int(z) for z in ids]

    suml = [a * b for a, b in zip(xsl, idss)]

    sums = sum(suml) % 11

    totel = modsl[sums]

    return totel


def myids(ids):

    mydisinfo = ids

    if int(mydisinfo[-1]) % 2 == 0:
        sexual = '女'
    else:
        sexual = '男'

    return sexual


def mybirthday(ids):

    mybirthdays = ids

    date = f'{mybirthdays[6:10]} 年 {mybirthdays[10:12]} 月 {mybirthdays[12:14]} 日'

    return date


files = f'D:\git\github\pcamateur\pyt\learn\\2020.json'

with open(files, 'r', encoding='utf8') as fis:
    datasl = json.load(fis)


def local(datasl, query):
    query = query[0:6]
    try:
        if query in datasl:

            pr = query[0:2]
            prs = pr + '0000'
            provice = datasl[prs]

            ci = query[0:4]
            cis = ci + '00'
            city = datasl[cis]

            district = datasl[query]

            total = provice + city + district
            return total

    except Exception as e:
        print(e)


def xingzuo(ids):
    xzn = ['摩羯座',
           '水瓶座',
           '双鱼座',
           '白羊座',
           '金牛座',
           '双子座',
           '巨蟹座',
           '狮子座',
           '处女座',
           '天秤座',
           '天蝎座',
           '射手座']

    xzd = ((1,20),
           (2,19),
           (3,21),
           (4,21),
           (5,21),
           (6,22),
           (7,23),
           (8,23),
           (9,23),
           (10,23),
           (11,23),
           (12,23))

    xvz = xzn[len(list(filter(lambda x: x < (int(ids[10:12]), int(ids[12:14])), xzd))) % 12]

    return xvz 
    
    
def sengx(ids):
    
    animal = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
    
    anv = animal[int(ids[6:10]) % 12]
    
    return anv 


def ages(ids):
    today = dt.today()
    
    brith = int(ids[6:10])
    
    age = today.year - brith
    
    return age


def run():
    
    ids = getID()

    print('身份证号码： ', ids + str(check(ids)))

    print('性别： ' ,myids(ids))

    print('出生日期： ', mybirthday(ids))

    print('地址： ', local(datasl, ids))

    print('星座： ', xingzuo(ids))
    
    print('生肖： ', sengx(ids))

    print('年龄： ', ages(ids))

if __name__ == '__main__':
    run()