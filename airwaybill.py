# input AirWayBill Number
input_value = input('Please input Airwaybill without "-":')

while input_value != "exit" :

    # digital the Airwaybill number
    input_num = int(eval(input_value[-7:]))

    # proccess the last Number
    last_num = int(input_num % 7)

    # Unit show
    unit_num = int(eval(input_value[:3]))

    # output Airwaybill and last number
    show_num = str(unit_num) + '-' + str(input_num) + str(last_num)

    # output
    print(show_num)

    # loop
    input_value = input('Please input Airwaybill without "-":')

# End sentence
byebye = "Thanks for your use this system,Bye!"

# Say Bye
print(byebye)