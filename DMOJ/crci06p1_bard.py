n = int(input())
e = int(input())

songs = []

for _ in range(e):
	# Get only villagers from input line (ignore first number)
	villagers = set([int(item) for item in input().split()][1:])
	if 1 in villagers:
		songs.append(villagers)
	else:
		# check for each time the bard was present if any of the 
		# villagers were also present then add all current villagers to that song
		for song in songs:
			if len(song & villagers) > 0:
				song.update(villagers)

output = songs[0]
for i in range(1, len(songs)):
	output = output & songs[i]

for villager in sorted(list(output)):
	print(villager)

