# BMI formula
#BMI_VALUE = weight_value // height_value**2

# input weight_value
weight_num = input('Please input Your weight and weight unit(kg,g or jin):')

# conversion weight_value

# anaylsis weight unit
weight_input_unit_one = weight_num[-1]
weight_input_unit_two = weight_num[-2:]
weight_input_unit_three = weight_num[-3:]

# judeg kg and g or jin or other error
if weight_input_unit_one == 'g' :
    if weight_input_unit_two != 'kg' :
        weight_true_value = eval(weight_num[:-1]) * 1000
    else :
        pass

elif weight_input_unit_two == 'kg' :
    weight_true_value = eval(weight_num[:-2])

elif weight_input_unit_three == 'jin' :
    weight_true_value = eval(weight_num[:-3])

else :
    print('The unit is error!The unit rule is kg,g,jin.')
    print(weight_num)

print(weight_num[:-1])
print(weight_num[:-2])
print(weight_num[:-3])