n = int(input())

contestants = {}

for _ in range(n):
	contestant = input()
	contestants[contestant] = 1 + contestants.get(contestant, 0)
	
for _ in range(n - 1):
	completed = input()
	contestants[completed] -= 1
	if contestants[completed] == 0:
		del contestants[completed]

print(list(contestants.keys())[0])
