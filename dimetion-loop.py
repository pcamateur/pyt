def calculate():
    q = float(input("Please input quantity: "))
    d = float(input("Please input dimension: "))

    lis = []

    def t1(d):
        tw1 = d * 166
        return tw1

    def count(q, t1):
        for x in range(10, 200):
            for y in range(x, 200):
                for z in range(y, 200):
                    dw = x * y * z * q / 6000
                    if dw - t1 < 2 and t1 - dw < 2:
                        lis.append([x, y, z])

    count(q, t1(d))

    print(lis)

while True:
    calculate()
    # answer = input("Do you want to continue? (yes/no): ")
    # if answer.lower() != "yes":
    #     break