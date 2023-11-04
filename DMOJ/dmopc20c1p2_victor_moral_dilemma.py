# DMOPC '20 Contest 1 P2 - Victor's Moral Dilemma

import sys
input = sys.stdin.readline

# Main program

# Read input
n, d = (int(item) for item in input().split())
trolleys = [int(item) for item in input().split()]
days = []
for _ in range(d):
	days.append(int(input()))

for day in days:
	f = sum(trolleys[:day])
	s = sum(trolleys[day:])
	if f >= s:
		trolleys = trolleys[day:]
		print(f)
	else:
		trolleys = trolleys[:day]
		print(s)
	
