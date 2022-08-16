# def digits(n,s,e):
#     lis = []
#     for x in range(s, e + 1):
#         if x % n == 0:
#             lis.append(x)
#     return lis


# # print(digits(6, 1, 65535))

# def three():
#     lis = []
#     for x in range(1, 65535):
#         if x % 2 == 0 and x % 3 == 0:
#             lis.append(x)
    
#     return lis

# sets = set(digits(6, 1, 65535)) - set(three())

# print(sets)
# print(len(sets))
# print(len(digits(6, 1, 65535)))
# print(len(three()))

def sevens(n, s, e):
    lis = []
    for x in range(s, e + 1):
        if x % n == 0:
            lis.append(x)
            
    return lis

l1 = sevens(7, 1, 65535)

def checks():
    lis = []
    for x in l1:
        if x > 10:
            sw = int(str(x)[:-1]) - int(str(x)[-1]) * 2


            lis.append((sw, x))
    return lis

print("--------------------------")
print("--------------------------")
print("--------------------------")
print(checks())

