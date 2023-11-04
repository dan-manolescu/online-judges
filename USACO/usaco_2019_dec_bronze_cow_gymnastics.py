def lower_rank_cows(sessions, cow):
	'''
	<sessions> is a list of practice sessions with each session a list of cows
	ordered by performance in a decreasing way.
	<cow> is the number of the cow for which we filter the list of lower ranked cows.
	
	Returns a set containing all cows that are lower ranked than the input <cow>
	with each cow there being lower in all practice sessions.
	'''
	# first construct a list with all other cows, then filter it with each session
	lower_rank = {other_cow for other_cow in range(1, n+1) if other_cow != cow}
	
	for session in sessions:
		for other_cow in session:
			# if we reached the input cow then we already removed all better cows
			if other_cow == cow:
				break
			elif other_cow in lower_rank:
				lower_rank.remove(other_cow)
	return lower_rank

# Main program

input_file = open('gymnastics.in', 'r')
output_file = open('gymnastics.out', 'w')

# Read input
k, n = (int(item) for item in input_file.readline().split())
sessions = []
for _ in range(k):
	session = [int(item) for item in input_file.readline().split()]
	sessions.append(session)
	
pairs = 0

for cow in range(1, n+1):
	# For each cow make a list of other potential cows lower than it
	lower_rank = lower_rank_cows(sessions, cow)

	# Count pairs between cow and any remaining in the list
	pairs += len(lower_rank)
	

# Write output
output_file.write(f'{pairs}\n')

input_file.close()
output_file.close()
