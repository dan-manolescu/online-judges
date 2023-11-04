# COCI '11 Contest 5 #2 Eko

import sys
input = sys.stdin.readline

# Main program

# Read input
n, m = (int(item) for item in input().split())
trees = [int(item) for item in input().split()]

# sort trees
trees.sort()

# Search in reverse, tree by tree with each height until we get to required wood
wood = 0
i = n - 2
height = 0
while wood < m:
	height = trees[i]
	wood_diff = trees[i+1] - trees[i]
	wood += wood_diff * (n - i - 1)
	i -= 1

# If we cut more wood than needed than adjust the height up by how many trees there are	
excess = 0	
if wood > m:
	excess = wood - m
height += excess // (n - i - 2)

# Write output
print(height)
