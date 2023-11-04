seq = input()

c_count = 0
a_count = 0

prev = '|'

for char in seq:
	if prev == '|':
		if char in ('C','F','G'):
			c_count += 1
		elif char in ('A','D','E'):
			a_count += 1
	prev = char
	
if c_count > a_count:
	print('C-dur')
elif c_count < a_count:
	print('A-mol')
else:
	if seq[-1] == 'C':
		print('C-dur')
	else:
		print('A-mol')
