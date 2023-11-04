n, h = (int(item) for item in input().split())

actions = []

for _ in range(2 * n):
	actions.append(input().split())
	
charlie = h
bot = h
for i in range(n):
	# charlie's turn
	if actions[i][0] == 'A' and (i == 0 or actions[n+i-1][0] != 'D'):
		bot -= int(actions[i][1])
		if bot <= 0:
			print('VICTORY')
			break
	elif actions[i][0] == 'D' and actions[n+i][0] != 'A':
		charlie -= int(actions[i][1])
		if charlie <= 0:
			print('DEFEAT')
			break
	
	# enemy's turn
	if actions[n+i][0] == 'A' and actions[i][0] != 'D':
		charlie -= int(actions[n+i][1])
		if charlie <= 0:
			print('DEFEAT')
			break
	elif actions[n+i][0] == 'D' and (i == n-1 or actions[i + 1][0] != 'A'):
		bot -= int(actions[n+i][1])
		if bot <= 0:
			print('VICTORY')
			break
else:
	print('TIE')
		
		
