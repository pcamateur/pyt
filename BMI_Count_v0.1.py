# BMI formula
# BMI_VALUE = weight_value // height_value**2

# input weight_value
weight_num = input('Please input Your weight and weight unit(kg,g or jin):')

# input height_value
height_num = input('Please input Your height and height unit(cm,m or mm):')

while weight_num != 'exit':
    # conversion weight_value

    # anaylsis weight unit
    weight_input_unit_one = weight_num[-1]
    weight_input_unit_two = weight_num[-2:]
    weight_input_unit_three = weight_num[-3:]

    # judeg kg and g or jin or other error
    # If the input unit contains g, but not kg, the system will report an error.
    if weight_input_unit_one == 'g':
        if weight_input_unit_two != 'kg':
            weight_true_value = eval(weight_num[:-1]) * 0.001

        elif weight_input_unit_two == 'kg':
            weight_true_value = eval(weight_num[:-2])

        else:
            print('The unit is error!The unit rule is kg,g,jin.')
            print(weight_num)

    elif weight_input_unit_three == 'jin':
        weight_true_value = eval(weight_num[:-3]) * 0.5

    else:
        print('The unit is error!The unit rule is kg,g,jin.')
        print(weight_num)

    # print(weight_true_value)
    # conversion height_value

    # anaylsis height unit
    height_input_unit_one = height_num[-1:]
    height_input_unit_two = height_num[-2:]

    # judeg cm or m or mm or other error
    # If the input unit contains m, but not cm or mm, the system will report an error.
    if height_input_unit_one == 'm':
        if height_input_unit_two == 'mm':
            height_true_value = eval(height_num[:-2]) * 0.001

        elif height_input_unit_two == 'cm':
            height_true_value = eval(height_num[:-2]) * 0.01

        elif height_input_unit_two != 'mm' and 'cm':
            height_true_value = eval(height_num[:-1])

        else:
            print('The unit is error!The unit rule is cm,m,mm.')
            print(height_num)

    else:
        print('The unit is error!The unit rule is cm,m,mm.')
        print(height_num)
    # print(height_true_value)
    # count BMI value
    BMI_value = round(weight_true_value / (height_true_value ** 2),1)

    print(weight_true_value)
    print(height_true_value)
    print(BMI_value)

    if BMI_value < 18.5 :
        BMI_t = "您的体形过瘦！一定要加强锻炼哦~"

    elif 18.5 <= BMI_value <= 23.9 :
        BMI_t = "Perfect!好羡慕您教科书式的身材，可否传授我一点秘诀~"

    elif 24 <= BMI_value <= 27.9 :
        BMI_t = "WOW和标准就差那么一小丢丢，加油！完美身材马上回来~"

    elif 28 <= BMI_value <= 32 :
        BMI_t = "亲，要注意体形喽！"

    elif BMI_value > 32 :
        BMI_t = "相扑力士！抱拳了~"

    else :
        print('Error 404:Value not found!')

    print(BMI_t)

    print('欢迎您继续查询，退出请输入exit!')
    # input weight_value
    weight_num = input('Please input Your weight and weight unit(kg,g or jin):')

    if weight_num == "exit":
         break

    # input height_value
    height_num = input('Please input Your height and height unit(cm,m or mm):')

print('Bye!')