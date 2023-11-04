n = int(input())
measures = [int(i) for i in input().split()]

minim = 10_000
min_i = -1
maxim = 1
max_i = -1

for i in range(n):
	minim = min(minim, measures[i])
	if minim == measures[i]:
		min_i = i
	maxim = max(maxim, measures[i])
	if maxim == measures[i]:
		max_i = i

if min_i < max_i:
	prev = minim
	for i in range(min_i+1, max_i+1):
		if prev >= measures[i]:
			print('unknown')
			break
		prev = measures[i]
	else:
		print(maxim - minim)
else:
	print('unknown')
