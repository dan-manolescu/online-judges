# DMOPC '17 Contest 1 P1 - Fujō Neko

import sys
input = sys.stdin.readline

r, c = (int(item) for item in input().split())

# Record monsters x and y coordinates in two separate sets
# Then we just need to look if either x or y from Q is found for a monster
monster_row = set()
monster_col = set()


for i in range(r):
	row = input()
	for j in range(c):
		if row[j] == 'X':
			monster_row.add(i+1)
			monster_col.add(j+1)

q = int(input())

for i in range(q):
	x, y = (int(item) for item in input().split())
	if x in monster_col or y in monster_row:
		print('Y')
	else:
		print('N')

