def count_single_and_teams(cow_set, single_set, team_set):
	'''
	<cow_set> is a set containing all distinct cows in a board row, column or diagonal.
	<single_set> is a set containing single cows that are able to win the board.
	<team_set> is a set containing teams of two cows (sorted) that are able to win the board.
	
	Updates the single_set and team_set with adequate values
	if they win the row, column or diagonal represented by cow_set.
	'''
	if len(cow_set) == 1:
		single_set.add(list(cow_set)[0])
	elif len(cow_set) == 2:
		team_set.add(tuple(sorted(list(cow_set))))

# Main program

input_file = open('tttt.in', 'r')
output_file = open('tttt.out', 'w')

# Read input
board = []
for _ in range(3):
	board.append(input_file.readline().rstrip())

single = set()
team = set()

# For each line count distinct characters if one increment single, if two increment team
for i in range(len(board)):
	cow_set = set(board[i])
	count_single_and_teams(cow_set, single, team)

# For each column do the same
for j in range(len(board[0])):
	cow_set = set()
	for row in board:
		cow_set.add(row[j])
	count_single_and_teams(cow_set, single, team)

# For each diagonal do the same
cow_set_d1, cow_set_d2 = set(), set()
for x in range(len(board)):
	cow_set_d1.add(board[x][x])
	cow_set_d2.add(board[x][-1-x])
count_single_and_teams(cow_set_d1, single, team)
count_single_and_teams(cow_set_d2, single, team)

# Write output
output_file.write(f'{len(single)}\n')
output_file.write(f'{len(team)}\n')


input_file.close()
output_file.close()
