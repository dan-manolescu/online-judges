def calculate_diamonds(diamonds, start_size, end_size):
	'''
	<diamonds> is a list of integers representing the size of each diamond.
	<start_size> is an integer representing the minimum size to choose for a diamond.
	<end_size> is an integer representing the maximum size to choose for a diamond.
	
	Returns the number of diamonds that can be chosen from the input list that
	fall between start_size and end_size.
	'''
	result = 0
	for diamond in diamonds:
		if start_size <= diamond <= end_size:
			result += 1
	return result

# Main program: USACO 2016 US Open Contest, Bronze Problem 1. Diamond Collector

input_file = open('diamond.in', 'r')
output_file = open('diamond.out', 'w')

# Read input
n, k = (int(item) for item in input_file.readline().split())

diamonds = []
for _ in range(n):
	diamonds.append(int(input_file.readline()))

# Choose the minimum diamond and calculate all diamonds k-greatest than it
max_diamonds = 0
diamond_sizes = set(diamonds)

for size in diamond_sizes:
	number_diamonds = calculate_diamonds(diamonds, size, size + k)
	max_diamonds = max(max_diamonds, number_diamonds)

# Write output
output_file.write(f'{max_diamonds}\n')

input_file.close()
output_file.close()
