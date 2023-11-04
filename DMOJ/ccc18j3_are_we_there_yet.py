def distances_for_city(distances, city):
	'''
	distances is a list of distances between each pair of cities.
	city is the 0-based integer index of the city for which we 
	calculate the distance to all other cities.
	
	Returns a list of distances from the city to all others ordered by city indexes
	with string values
	'''
	output = [None] * (len(distances) + 1)
	for i in range(len(output)):
		if i == city:
			output[i] = '0'
		elif i < city:
			output[i] = str(sum(distances[i:city]))
		else:
			output[i] = str(sum(distances[city:i]))
	return output

# Main program

# Read input
distances = [int(item) for item in input().split()]

# For each city make a list of distances
for i in range(len(distances) + 1):
	dist_city = distances_for_city(distances, i)
	print(' '.join(dist_city))

