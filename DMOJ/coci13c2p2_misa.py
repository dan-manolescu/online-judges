DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def get_church_pos(seats, i, j):
	'''
	<seats> is the total number of seats in a row in the church
	<i> is the current row
	<j> is the current seat
	
	Returns an integer position representing the current position
	obtained by counting all seats from the first row then continuing with
	all seats from next row etc
	'''
	return (i - 1) * seats + j

def calc_handshake_all(church):
	'''
	<church> is a 2d list of r*s size containing '.' for empty spot
	and 'o' for a taken spot
	
	Returns the total number of handshakes possible in this configuration as an integer
	'''
	shaken = set() # set to contain already taken handshakes
	result = 0
	for i in range(len(church)):
		for j in range(len(church[i])):
			if church[i][j] == 'o':
				seat = get_church_pos(len(church[i]), i, j)
				for di, dj in DIRECTIONS:
					di += i
					dj += j
					if (0 <= di < len(church) and 
						0 <= dj < len(church[di]) and
						church[di][dj] == 'o'):
						other_seat = get_church_pos(len(church[di]), di, dj)
						shake = (min(seat, other_seat), max(seat, other_seat))
						if shake not in shaken:
							result += 1
							shaken.add(shake)
	return result
	
def calc_handshake_misa(church, i, j):
	'''
	<church> is a 2d list of r*s size containing '.' for empty spot
	and 'o' for a taken spot
	<i> is the row where misa stays
	<j> is the seat where misa stays
	
	Returns the number of handshakes that misa is able to do
	'''
	result = 0
	for di, dj in DIRECTIONS:
		di += i
		dj += j
		if (0 <= di < len(church) and 
			0 <= dj < len(church[di]) and
			church[di][dj] == 'o'):
			result += 1
	return result
						

# Main program

# Read input
r, s = (int(item) for item in input().split())

church = []
for _ in range(r):
	church.append(list(input()))

# First calculate handshakes for occupied seats
other_handshakes = calc_handshake_all(church)

# Then for each empty spot calculate if Misa would stay there and keep maximum
misa_handshake = 0
for i in range(r):
	for j in range(s):
		if church[i][j] == '.':
			misa_handshake = max(misa_handshake, calc_handshake_misa(church, i, j))

# Output maximum handshakes
print(other_handshakes + misa_handshake)
