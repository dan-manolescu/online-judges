word = input()

honi = 0
prev = ''

for char in word:
	if char == 'H' and prev == '':
		prev = 'H'
	elif char == 'O' and prev == 'H':
		prev = 'O'
	elif char == 'N' and prev == 'O':
		prev = 'N'
	elif char == 'I' and prev == 'N':
		prev = ''
		honi += 1

print(honi)
