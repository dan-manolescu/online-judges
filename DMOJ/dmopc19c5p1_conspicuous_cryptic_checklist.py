n, m = (int(item) for item in input().split())

tzak_items = set()
for _ in range(n):
	tzak_items.add(input())
	
completed = 0

# Iterate over each assignment and check if we have all items
for _ in range(m):
	t = int(input())
	flunked = False
	for i in range(t):
		if input() not in tzak_items:
			flunked = True
	if not flunked:
		completed += 1

print(completed)
