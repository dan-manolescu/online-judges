# Main program

input_file = open('shell.in', 'r')
output_file = open('shell.out', 'w')

# Read input

n = int(input_file.readline())

swaps = []
for _ in range(n):
	lst = [int(item) for item in input_file.readline().split()]
	swaps.append(lst)

max_points = 0

# For each possible start run the swaps and total points
for i in range(1,4):
	pebble = i
	points = 0
	for swap in swaps:
		# move the pebble if part of the swap
		if pebble == swap[0]:
			pebble = swap[1]
		elif pebble == swap[1]:
			pebble = swap[0]
		# check if guess is right
		if pebble == swap[2]:
			points += 1
	max_points = max(max_points, points)

# Write output
output_file.write(f'{max_points}\n')

input_file.close()
output_file.close()
