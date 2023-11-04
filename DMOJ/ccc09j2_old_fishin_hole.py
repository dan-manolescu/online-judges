# CCC '09 J2 - Old Fishin' Hole

def calculate_points(combination, fishes):
	'''
	<combination> is a list with three integers representing how many of each fish type.
	<fishes> is a list with three integers representing points for each fish type.
	
	Returns the amount of points for the given combination of fishes.
	'''
	points = 0
	for i in range(len(combination)):
		points += combination[i] * fishes[i]
	return points

def make_combination(combination, fishes, total, combinations):
	'''
	<combination> is a list with three integers representing how many of each fish type.
	<fishes> is a list with three integers representing points for each fish type.
	<total> is an integer for the total points allowed.
	<combinations> is a set with all possible combinations of fish types discovered so far.
	
	Returns an updated combinations set.
	'''
	if tuple(combination) in combinations:
		return combinations		
	
	points = calculate_points(combination, fishes)
	if total < points:
		return combinations
	
	combinations.add(tuple(combination))
	if total > points:
		for i in range(len(fishes)):
			new_combination = combination.copy()
			new_combination[i] += 1
			combinations = make_combination(new_combination, fishes, total, combinations)
	return combinations


# Main program

# Read input

fishes = []
for _ in range(3):
	fishes.append(int(input()))
total = int(input())

# Create branching logic for each type of fish
combinations = make_combination([0,0,0], fishes, total, set())
# Remove the initial combination of 0,0,0
combinations.remove((0,0,0))

# Write output
for c in combinations:
	print(f'{c[0]} Brown Trout, {c[1]} Northern Pike, {c[2]} Yellow Pickerel')
print(f'Number of ways to catch fish: {len(combinations)}')


