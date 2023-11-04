points_a = int(input())
scores = []

for _ in range(points_a):
	scores.append([int(input()), 'A'])
	
points_b = int(input())
for _ in range(points_b):
	scores.append([int(input()), 'B'])
	
scores.sort()
halftime = 2 * 12 * 60

# initialize leading team with the first team that scores
leading = scores[0][1]

score_a = 0
score_b = 0
half_score = 0
turn_around = 0

for score in scores:
	if score[0] <= halftime:
		half_score += 1

	if score[1] == 'A':
		score_a += 1
	else:
		score_b += 1
		
	if score_a > score_b and leading != 'A':
		turn_around += 1
		leading = 'A'
	elif score_b > score_a and leading != 'B':
		turn_around += 1
		leading = 'B'
		
print(half_score)
print(turn_around)

