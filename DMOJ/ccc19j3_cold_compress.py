n = int(input())

for _ in range(n):
	line = input()
	pairs = []
	
	i = 0
	while i < len(line):
		c = line[i]
		occurence = 0
		while i < len(line) and line[i] == c:
			i += 1
			occurence += 1
			
		pairs.append(f'{occurence} {c}')
		
	print(' '.join(pairs))
