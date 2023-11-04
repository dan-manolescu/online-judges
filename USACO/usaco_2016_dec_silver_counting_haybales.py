# USACO 2016 December Contest, Silver Problem 1. Counting Haybales

from bisect import bisect_left, bisect_right

def count_haybales(left, right, haybales):
	'''
	<left> is an integer representing the left position.
	<right> is an integer representing the right position.
	<haybales> is a sorted list with all the haybales positions.
	
	Returns the number of haybales between left and right.
	'''
	left = bisect_left(haybales, left)
	right = bisect_right(haybales, right)
	return right - left

# Main program

input_file = open('haybales.in', 'r')
output_file = open('haybales.out', 'w')

# Read input
n, q = (int(item) for item in input_file.readline().split())

haybales = [int(item) for item in input_file.readline().split()]

queries = []
for _ in range(q):
	queries.append([int(item) for item in input_file.readline().split()])

# Sort haybales
haybales.sort()

results = []
# For each query append the number of haybales
for query in queries:
	results.append(count_haybales(query[0], query[1], haybales))

# Write output
for result in results:
	output_file.write(f'{result}\n')

input_file.close()
output_file.close()
