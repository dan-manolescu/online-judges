s = input()
m = int(input())

combos = []
for i in range(m):
	combos.append(input().split())

combos.sort(key=lambda combo: len(combo[0]), reverse=True)

total = len(s)
i = 0
while i < len(s):
	for combo in combos:
		if s[i:i + len(combo[0])] == combo[0]:
			total += int(combo[1])
			i += len(combo[0])
			break
	else:
		i += 1

print(total)
