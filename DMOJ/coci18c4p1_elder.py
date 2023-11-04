elder = input()
n = int(input())

obey = set(elder)

for i in range(n):
	duel = input()
	if duel[-1] == elder:
		elder = duel[0]
		obey.add(elder)
		
print(elder)
print(len(obey))
