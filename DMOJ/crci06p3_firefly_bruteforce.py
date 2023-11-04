# COCI '06 Regional #3 Firefly

# Main program

# Read input
n, h = (int(item) for item in input().split())
levels = [0] * h
obstacles = []
for _ in range(n):
	obstacles.append(int(input()))

for i in range(h):
	# Count stalagmites for each level
	for j in range(0, n, 2):
		if obstacles[j] >= i + 1:
			levels[i] += 1

	# Count stalactices for each level
	for j in range(1, n, 2):
		if obstacles[j] >= h - i:
			levels[i] += 1

# Read levels and obtain result
min_obstacles = min(levels)
min_levels = 0
for level in levels:
	if level == min_obstacles:
		min_levels += 1

# Write output
print(f'{min_obstacles} {min_levels}')
