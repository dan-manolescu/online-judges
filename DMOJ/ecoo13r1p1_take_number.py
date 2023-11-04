next = int(input())
activity = ''
students = 0
line = 0

while activity != 'EOF':
	activity = input()
	if activity == 'TAKE':
		students += 1
		line += 1
		next += 1
		if next == 1000:
			next = 1
	elif activity == 'SERVE':
		line -= 1
	elif activity == 'CLOSE':
		print(students, line, next)
		students = 0
		line = 0
		
