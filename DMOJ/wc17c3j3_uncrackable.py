password = input()

lower = 0
upper = 0
digit = 0

if 8 <= len(password) <= 12:
	for char in password:
		if char.isupper():
			upper += 1
		elif char.islower():
			lower += 1
		elif char.isdigit():
			digit += 1
	
	if lower < 3 or upper < 2 or digit < 1:
		print('Invalid')
	else:
		print('Valid')
else:
	print('Invalid')
