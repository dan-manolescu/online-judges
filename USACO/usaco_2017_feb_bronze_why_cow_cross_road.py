# Main program

input_file = open('crossroad.in', 'r')
output_file = open('crossroad.out', 'w')

# Read input
n = int(input_file.readline().rstrip())

crossing = {}
total_cross = 0

# Count each crossing
for _ in range(n):
	lst = input_file.readline().split()
	cow = int(lst[0])
	side = int(lst[1])
	
	if cow in crossing and crossing[cow] != side:
		total_cross += 1
	crossing[cow] = side

# Write output
output_file.write(f'{total_cross}\n')

input_file.close()
output_file.close()
