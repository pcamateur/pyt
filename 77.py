num = 1
while num <= 99:
    num = num + 1
    if (num % 7 == 0) or (num % 10 == 7) : #or (num // 10 == 7):
        continue
    else:
        print(num)