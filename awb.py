def get_value(n):
	num1 = int(n[-7:]) % 7
	return n + str(num1)
	

i = input('value:')
print(get_value(i))