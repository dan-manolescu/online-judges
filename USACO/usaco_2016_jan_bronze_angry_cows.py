# USACO 2016 January Contest, Bronze Problem 2. Angry Cows

from bisect import bisect_left, bisect_right

def explode_left(idx, bales):
	'''
	<idx> is the integer index of the hay bale being hit.
	<bales> is a list with the positions of all bales
	
	Returns the index of the last bale exploded to the left of the idx bale.
	'''
	left = idx
	stop = False
	radius = 1
	while not stop:
		new_left = bisect_left(bales, bales[left] - radius)
		if new_left == left or new_left == 0:
			stop = True
		else:
			radius += 1
		left = new_left
	return left
	
	
def explode_right(idx, bales):
	'''
	<idx> is the integer index of the hay bale being hit.
	<bales> is a list with the positions of all bales
	
	Returns the index of the last bale exploded to the right of the idx bale.
	'''
	right = idx
	stop = False
	radius = 1
	while not stop:
		new_right = bisect_right(bales, bales[right] + radius)
		if new_right == right + 1 or new_right >= len(bales):
			stop = True
		else:
			radius += 1
		right = new_right - 1
	return right if right < len(bales) else len(bales) - 1


# Main program

input_file = open('angry.in', 'r')
output_file = open('angry.out', 'w')

# Read input

n = int(input_file.readline())
bales = []
for _ in range(n):
	bales.append(int(input_file.readline()))
	
bales.sort()
max_bale = 1

for i in range(n):
	left = explode_left(i, bales)
	right = explode_right(i, bales)
	max_bale = max(max_bale, right - left + 1)

# Write output	
output_file.write(f'{max_bale}\n')

input_file.close()
output_file.close()
