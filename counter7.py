# preset function
def process_uinte (input_value,Base_Num) :
    pass

# greeting sentence
helloword = 'Please input Numbers(Exit please type 0):'

# get the input infomation
input_num_value = eval(input(helloword))

# test input
# print(input_num_value)

# preset counter default value
i = 0

while input_num_value != 0 :

    # counter loop
    i = i + 1

    # loop show
    print('You have run for the ', i )

    if input_num_value % 7 == 0 :
        print('Loser! A')
    
    elif input_num_value % 10 == 7 :
        print('Loser! B')

    elif input_num_value // 10 == 7 :
        print('Loser! C')

    else :
        print('Yeah!')

    print('Continue or Quit?')

    input_num_value = eval(input(helloword))

print('See You!')






    