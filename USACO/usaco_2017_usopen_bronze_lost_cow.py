# Main program

input_file = open('lostcow.in', 'r')
output_file = open('lostcow.out', 'w')

# Read input
x, y = (int(item) for item in input_file.readline().split())

# Move logic
distance = 0
travel = 1
prev_pos = x
while True:
	new_pos = x + travel
	# check if we found the cow
	if ((x < y and new_pos >= y) or (x > y and new_pos <= y)):
		distance += abs(y - prev_pos)
		break
	else:
		distance += abs(new_pos - prev_pos)
		prev_pos = new_pos
		travel *= -2

# Write output
output_file.write(f'{distance}\n')

input_file.close()
output_file.close()
