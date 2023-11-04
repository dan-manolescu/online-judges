# COCI '20 Contest 1 #1 Patkice

def navigate(sea, start_s, start_r, direction):
	'''
	<sea> is a list of strings representing the input map.
	<start_r> is an integer representing the index of the row
	containing origin point 'o'.
	<start_s> is an integer representing the index of the column
	containing origin point 'o'.
	<direction> is a string representing the start direction.
	
	Returns an integer with the voyage time or -1 if impossible to get to 'x'.
	'''
	time = 0
	next_pos = start_s, start_r
	current = convert_direction(direction)
	while current not in ('x', '.', 'o'):
		next_pos = calculate_next_pos(next_pos[0], next_pos[1], current)
		time += 1
		current = sea[next_pos[0]][next_pos[1]]
	return time if current == 'x' else -1
	
def calculate_next_pos(pos_r, pos_s, direction):
	'''
	pos_r is the row of the current position on the map
	pos_s is the column of the current position on the map
	direction is a string representing the direction to next position
	
	Returns the row and column for the next position based on direction
	'''
	if direction == '^':
		return pos_r - 1, pos_s
	elif direction == '>':
		return pos_r, pos_s + 1
	elif direction == '<':
		return pos_r, pos_s - 1
	else:
		return pos_r + 1, pos_s
	
def convert_direction(direction):
	'''
	direction is a string with geographic directions as N, E, W or S.
	
	Returns a current direction corresponding to this as ^, >, < or v.
	'''
	if direction == 'N':
		return '^'
	elif direction == 'E':
		return '>'
	elif direction == 'W':
		return '<'
	else:
		return 'v'

# Main program

# Read input

r, s = (int(item) for item in input().split())

sea = []
for _ in range(r):
	sea.append(input())

directions = 'NEWS'
voyages = []

# Locate origin point
start_r, start_s = 0, 0
for i in range(r):
	for j in range(s):
		if sea[i][j] == 'o':
			start_r = i
			start_s = j
			break

# For each direction initiate navigation and record voyage time
for direction in directions:
	time = navigate(sea, start_r, start_s, direction)
	if time != -1:
		voyages.append((time, direction))

# Determine shortest voyage
voyages.sort()

# TODO: Write output
if len(voyages) > 0:
	print(':)')
	print(voyages[0][1])
else:
	print(':(')
