bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())

baby_bowl = min(bowl1, bowl2, bowl3)
father_bowl = max(bowl1, bowl2, bowl3)

if baby_bowl < bowl1 < father_bowl:
	print(bowl1)
elif baby_bowl < bowl2 < father_bowl:
	print(bowl2)
else:
	print(bowl3)

