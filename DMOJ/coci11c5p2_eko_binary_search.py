# COCI '11 Contest 5 #2 Eko

import sys
input = sys.stdin.readline

def extract_wood(trees, height):
	'''
	trees is a sorted list of tree heights in non-ascending order.
	height is an integer for the height at which we cut trees.
	
	Returns the amount of wood obtained from cutting the trees at the given height.
	'''
	wood = 0
	for tree in trees:
		if height < tree:
			wood += tree - height
		else:
			break
	return wood

# Main program

# Read input
n, m = (int(item) for item in input().split())
trees = [int(item) for item in input().split()]

# sort trees
trees.sort(reverse=True)

# Binary search on height
low = 0
high = max(trees)
wood = 0
height = 0
stop = False
while not stop:
	mid = low + (high - low) // 2
	wood = extract_wood(trees, mid)
	if wood < m:
		high = mid - 1
	elif wood > m:
		low = mid + 1
	else:
		height = mid
		stop = True

# Write output
print(height)
