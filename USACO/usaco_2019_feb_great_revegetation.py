def read_cows(input_file, num_cows):
	'''
	input_file is a file open for reading; cow information is next to read.
	num_cows is the number of cows in the file.
	
	Read the cows' favorite pasture from input_file.
	Return a list of each cow's two favorite pastures;
	each value in the list is a list of two values giving the 
	favorite pastures for one cow.
	'''
	favorites = []
	for i in range(num_cows):
		lst = [int(item) for item in input_file.readline().split()]
		favorites.append(lst)
	return favorites
	
def cows_with_favorites(favorites, pasture):
	'''
	favorites is a list of favorite pastures, as returned by read_cows.
	pasture is a pasture number.
	
	Return a list of cows that care about pasture.
	'''
	cows = []
	for i in range(len(favorites)):
		if favorites[i][0] == pasture or favorites[i][1] == pasture:
			cows.append(i)
	return cows
	
def types_used(favorites, cows, pasture_types):
	'''
	favorites is a list of favorite pastures, as returned by read_cows.
	cows is a list of cows.
	pasture_types is a list of grass types.
	
	Return a list of the grass types already used by the cows.
	'''
	used = []
	for cow in cows:
		pasture_a = favorites[cow][0]
		pasture_b = favorites[cow][1]
		if pasture_a < len(pasture_types):
			used.append(pasture_types[pasture_a])
		if pasture_b < len(pasture_types):
			used.append(pasture_types[pasture_b])
	return used
	
def smallest_available(used):
	'''
	used is a list of used grass type.
	
	Return the smallest numbered grass type that is not in used.
	'''
	grass_type = 1
	while grass_type in used:
		grass_type += 1
	return grass_type
	
def write_pastures(output_file, pasture_types):
	'''
	output_file is a file open for writing.
	pasture_types is a list of integer grass types.
	
	Output pastrue_types to output_file.
	'''
	pasture_types_str = [str(item) for item in pasture_types]
	output = ''.join(pasture_types_str)
	output_file.write(f'{output}\n')

# Main Program

input_file = open('revegetate.in', 'r')
output_file = open('revegetate.out', 'w')

# Read input
lst = input_file.readline().split()
num_pastures = int(lst[0])
num_cows = int(lst[1])
favorites = read_cows(input_file, num_cows)

pasture_types = [0] # initialized with 0 so we keep index 1 for pasture 1

for i in range(1, num_pastures + 1):

	# Identify cows that care about pasture
	cows = cows_with_favorites(favorites, i)

	# Eliminate grass types for pasture
	eliminated = types_used(favorites, cows, pasture_types)

	# Choose smallest-numbered grass type for pasture
	pasture_type = smallest_available(eliminated)
	pasture_types.append(pasture_type)

# Write output
write_pastures(output_file, pasture_types[1:])

input_file.close()
output_file.close()

