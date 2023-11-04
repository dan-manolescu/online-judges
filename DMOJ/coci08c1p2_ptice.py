n = int(input())
answers = input()

adrian = 'ABC'
bruno = 'BABC'
goran = 'CCAABB'

adrian_score = 0
bruno_score = 0
goran_score = 0

for i in range(n):
	if answers[i] == adrian[i % len(adrian)]:
		adrian_score += 1
	if answers[i] == bruno[i % len(bruno)]:
		bruno_score += 1
	if answers[i] == goran[i % len(goran)]:
		goran_score += 1
		
max_score = max(adrian_score, bruno_score, goran_score)
print(max_score)
if max_score == adrian_score:
	print('Adrian')
if max_score == bruno_score:
	print('Bruno')
if max_score == goran_score:
	print('Goran')

	
