# BMI formula
#BMI_VALUE = weight_value // height_value**2

# input weight_value
weight_num = input('Please input Your weight and weight unit(kg,g or jin):')

# input height_value
height_num = input('Please input Your height and height unit(cm,m or mm):')

# conversion weight_value

# anaylsis weight unit
weight_input_unit_one = weight_num[-1]
weight_input_unit_two = weight_num[-2:]
weight_input_unit_three = weight_num[-3:]

# judeg kg and g or jin or other error
if weight_input_unit_one == 'g':
    if weight_input_unit_two != 'kg':
        #weight_true_value = eval(weight_num[:-1]) * 1000
        pass
    else:
        pass

elif weight_input_unit_two == 'kg':
    weight_true_value = eval(weight_num[:-2])

elif weight_input_unit_three == 'jin':
    #weight_true_value = eval(weight_num[:-3]) * 2
    pass

else:
    print('The unit is error!The unit rule is kg,g,jin.')
    print(weight_num)
print(weight_true_value)
# conversion height_value

# anaylsis height unit
height_input_unit_one = height_num[-1]
height_input_unit_two = height_num[-2]

# judeg cm or m or mm or other error
if height_input_unit_one == 'm' :
    if height_input_unit_two != 'cm' or 'mm':
        height_true_value = eval(height_num[:-1])
    else:
        pass
elif height_input_unit_two == 'cm':
    height_true_value = eval(height_num[:-2]) * 100

elif height_input_unit_two == 'mm':
    height_true_value = eval(height_num[:-2]) * 1000

else:
    print('The unit is error!The unit rule is cm,m,mm.')
    print(height_num)
print(height_true_value)
# count BMI value
#BMI_value = eval(weight_true_value) / eval(height_true_value) **2

#print(weight_true_value)
#print(height_true_value)
