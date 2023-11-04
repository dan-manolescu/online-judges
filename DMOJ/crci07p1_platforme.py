def calculate_legs(platform, cache):
	'''
	platform is a list of a interger y coordinate and
	a tuple of x1 and x2 integer coordinates defining a platform.
	cache is a dictionary constantly updated as each platform is
	processed with key = x coord and value = y coord of the most recent platform.

	Assumes the cache contains all the previosu platforms ordered by y from 0.
	
	Returns a tuple of legs for the platform
	'''
	y = platform[0]
	x1, x2 = platform[1]
	leg1 = y if x1 not in cache else y - cache[x1]
	leg2 = y if x2 not in cache else y - cache[x2]
	
	refresh_cache(platform, cache)
	return leg1, leg2
	

def refresh_cache(platform, cache):
	'''
	platform is a list of a interger y coordinate and
	a tuple of x1 and x2 integer coordinates defining a platform.
	cache is a dictionary constantly updated as each platform is
	processed with key = x coord and value = y coord of the most recent platform.
	
	Updates cache so that the most current x1 to x2 keys are using y
	'''
	y = platform[0]
	x1, x2 = platform[1]
	for x in range(x1, x2 + 1):
		cache[x] = y
		

# Main Program

# Read input
n = int(input())

platforms = []
for _ in range(n):
	y, x1, x2 = input().split()
	# decrement 1 for x2 in order to prevent overlap
	# for example when one plaform ends at 5 and another starts at 5
	platforms.append([int(y), (int(x1), int(x2) - 1)])

# Sort input
platforms.sort()

# For each platform starting from bottom calculate legs
cache = {} # key: x coord, value = most recent platform by y
total = 0
for platform in platforms:
	leg1, leg2 = calculate_legs(platform, cache)
	total += leg1 + leg2

# Output result
print(total)
