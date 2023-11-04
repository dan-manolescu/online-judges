# ECOO '16 R1 P2 - Spindie

def calculate_combination(spin_cnt, points, spinners, targets):
	'''
	<spin_cnt> is an integer representing how many spins we have so far.
	<points> is an integer representing how many points we have so far
	<spinners> is a set with all spinner values.
	<targets> is a dictionary with key as target points and value T or F

	'''
	if spin_cnt == 3:
		if points in targets:
			targets[points] = 'T'
	else:
		for spin in spinners:
			if spin_cnt == 0:
				calculate_combination(1, spin, spinners, targets)
			else:
				calculate_combination(spin_cnt + 1, points + spin, spinners, targets)
				calculate_combination(spin_cnt + 1, points * spin, spinners, targets)
		
	

for _ in range(10):
	n = int(input())
	spinners = set([int(item) for item in input().split()])
	targets = {int(item): 'F' for item in input().split()}

	calculate_combination(0, 0, spinners, targets)

	# On output we take advantage of the fact that dict are now key ordered
	print(''.join([item[1] for item in targets.items()]))

