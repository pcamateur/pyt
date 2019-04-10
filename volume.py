'''
Dimension Weight App
'''

# Dimension Weight Exchange
# DIM_value = round((width_value + height_value + depth_value) * 6000,1)

# Input Value infomation
width_value_input = input('Please input width and Unit(Uint ex: m,cm,m):')

height_value_input = input('Please input height and Unit(Uint ex: m,cm,m):')

depth_value_input = input('Please input depth and Unit(Uint ex: m,cm,m):')

# loop begin point,and Exit ON/OFF
while width_value_input != 'exit':
    
    # Unit infomation get M or not
    widht_value_unit_one = width_value_input[-1:]
    # Unit infomation get CM or MM or not
    width_value_unit_two = width_value_input[-2:]

    if widht_value_unit_one == 'm':
        if width_value_unit_two == 'mm':
            width_true_value = eval(width_value_input[:-2]) * 0.1

        elif width_value_unit_two == 'cm':
            width_true_value = eval(width_value_input[:-2]) 

        elif width_value_unit_two != 'mm' and 'cm':
            width_true_value = eval(width_value_input[:-1]) * 100

        else:
            print('The Width Value unit is error!The unit rule is cm,m,mm.')
            print(width_value_input)

    # Unit infomation get M or not
    height_value_unit_one = height_value_input[-1:]
    # Unit infomation get CM or MM or not
    height_value_unit_two = height_value_input[-2:]

    if height_value_unit_one == 'm':
        if height_value_unit_two == 'mm':
            height_true_value = eval(height_value_input[:-2]) * 0.1

        elif height_value_unit_two == 'cm':
            height_true_value = eval(height_value_input[:-2]) 

        elif height_value_unit_two != 'mm' and 'cm':
            height_true_value = eval(height_value_input[:-1]) * 100

        else:
            print('The Height Value unit is error!The unit rule is cm,m,mm.')
            print(height_value_input)

    # Unit infomation get M or not
    depth_value_unit_one = depth_value_input[-1:]
    # Unit infomation get CM or MM or not
    depth_value_unit_two = depth_value_input[-2:]

    if depth_value_unit_one == 'm':
        if depth_value_unit_two == 'mm':
            depth_true_value = eval(depth_value_input[:-2]) * 0.1

        elif depth_value_unit_two == 'cm':
            depth_true_value = eval(depth_value_input[:-2]) 

        elif depth_value_unit_two != 'mm' and 'cm':
            depth_true_value = eval(depth_value_input[:-1]) * 100

        else:
            print('The Depth Value unit is error!The unit rule is cm,m,mm.')
            print(depth_value_input)

    width_value = float(width_true_value)

    height_value = float(height_true_value)

    depth_value = float(depth_true_value)

    # Dimension Weight Exchange
    # DIM_value = round((width_value * height_value * depth_value) / 6000,1)
    DIM_value = (width_value * height_value * depth_value) / 6000

    
    print('Width Value is:',width_value)

    print('Height Value is:',height_value)

    print('Depth Value is:',depth_value)

    print(DIM_value,'kg')

    print('欢迎您继续查询，退出请输入exit!')
    # Input Value infomation
    width_value_input = input('Please input width and Unit(Uint ex: m,cm,m):')
    
    if width_value_input == "exit":
         break
    
    height_value_input = input('Please input height and Unit(Uint ex: m,cm,m):')
    
    depth_value_input = input('Please input depth and Unit(Uint ex: m,cm,m):')
    
     # if width_value_input == "exit":
        # break

print('Bye!')

