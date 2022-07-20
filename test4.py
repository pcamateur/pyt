dic = { 
    'Name': "John", 
    'Ago': "18", 
    'Sex': 'Male', 
    'Bro':"Goods", 
    'Phone':"None",
    'Level':"1",
    'Model':"Null"
    }


def list_keys(dic):
    
    list_numb = list()
    for list_numbs in range(len(dic)):
        list_numb.append(list_numbs + 1)

    list_key = list()
    for x, y in dic.items():
        list_key.append(x)

    lts = list(zip(list_numb, list_key))

    for a in range(len(lts)):
        print(lts[a][0],':',lts[a][1])

list_keys(dic)
