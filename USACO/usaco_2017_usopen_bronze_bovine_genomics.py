def find_genomes(genomes, pos):
	'''
	<genomes> is a list of strings representing all cow genomes.
	<pos> is an integer representing the position in the genome we are looking at.
	
	Returns a set with all distinct characters found at position <pos> in all genomes.	
	'''
	result = set()
	for genome in genomes:
		result.add(genome[pos])
	return result

# Main program

input_file = open('cownomics.in', 'r')
output_file = open('cownomics.out', 'w')

# Read input
n, m = (int(item) for item in input_file.readline().split())
spotty, plain = [], []
for _ in range(n):
	spotty.append(input_file.readline().rstrip())
for _ in range(n):
	plain.append(input_file.readline().rstrip())

positions = 0
# For each position obtain distinct chars on spotty and plain cows
for i in range(m):
	spotty_set = find_genomes(spotty, i)
	plain_set = find_genomes(plain, i)

	# If there is no intersection count position
	if len(spotty_set & plain_set) == 0:
		positions += 1

# Write output
output_file.write(f'{positions}\n')

input_file.close()
output_file.close()
