# COCI '06 Regional #3 Firefly

# Main program

# Read input
n, h = (int(item) for item in input().split())
stalagmites = []
stalactites = []
for i in range(n):
	if i % 2 == 0:
		stalagmites.append(int(input()))
	else:
		stalactites.append(int(input()))
		
stalagmites.sort()
stalactites.sort(reverse=True)

# for each height count how many stalagmites are smaller than that height
# for each height count how many stalactites are smaller than that height
obstacles = [0] * h
g = 0 # index for stalagmites
c = 0 # index for stalactites
smaller_stalagmite = 0
smaller_stalactite = len(stalactites)
for i in range(h):
	# count for each stalagmite height how many are smaller
	while g < len(stalagmites) and stalagmites[g] < i + 1:
		smaller_stalagmite += 1
		g += 1
	# count for each stalactite how many are below the height
	while c < len(stalactites) and stalactites[c] >= h - i:
		smaller_stalactite -= 1
		c += 1
	# now count how many obstacles we hit at this height
	# this means that from the total stalagmites we remove the ones that are smaller
	# and from the total stalactites we remove the ones that are not reaching
	obstacles[i] = len(stalagmites) - smaller_stalagmite + len(stalactites) - smaller_stalactite
		
obstacles.sort()

# Read heights and obtain result
min_obstacle = min(obstacles)
min_levels = 0
for obstacle in obstacles:
	if obstacle == min_obstacle:
		min_levels += 1
	elif obstacle > min_obstacle:
		break

# Write output
print(f'{min_obstacle} {min_levels}')

