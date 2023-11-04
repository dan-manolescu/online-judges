def calc_min_moves(herd):
	'''
	<herd> is a list of three integers representing the position of the three cows.
	
	Returns the minimum number of moves to have the cows in consecutive locations as an int.
	'''
	# Find min and max distance between two cows
	min_interval = min(herd[1]-herd[0], herd[2]-herd[1])
	max_interval = max(herd[1]-herd[0], herd[2]-herd[1])
	if min_interval == 1:
		# if already consecutive return 0 (max_interval == 1)
		# if we have a case 1,3,4 return 1 (max_interval == 2)
		# if we have a case 1,4,5 and we move to 1,3,4 then 1,4,3
		# so for anything max_interval > 2 return 2
		return 2 if max_interval > 2 else max_interval - 1
	else:
		# if we have something like 1,3,7 and we move 1,2,3
		# if we have something like 1,4,8 and we move 1,3,4 then 3,4,5					
		return 2 if min_interval > 2 else 1
		
def calc_max_moves(herd):
	'''
	<herd> is a list of three integers representing the position of the three cows.
	
	Returns the maximum number of moves to have the cows in consecutive locations as an int.
	'''
	max_interval = max(herd[1]-herd[0], herd[2]-herd[1])
	return max_interval - 1


# Main program

input_file = open('herding.in', 'r')
output_file = open('herding.out', 'w')

# Read input
herd = [int(item) for item in input_file.readline().split()]

# Determine min moves
min_moves = calc_min_moves(herd)

# Determine max moves
max_moves = calc_max_moves(herd)

# Write output
output_file.write(f'{min_moves}\n')
output_file.write(f'{max_moves}\n')

input_file.close()
output_file.close()
