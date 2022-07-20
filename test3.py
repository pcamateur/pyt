def adds(a, b):
    if str(a).isdigit() and str(b).isdigit():
        print('That is a digit!')
        return str(a) + str(b)
        
    else:
        print('That is a text!')
        return a + b
        

s = adds(True, False)

print(s)