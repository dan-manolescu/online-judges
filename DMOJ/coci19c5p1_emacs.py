n, m = (int(item) for item in input().split())

picture = []
result = 0

for i in range(n):
	line = input()
	picture.append(line)
	j = 0
	while j < len(line):
		if line[j] == '*' and (i == 0 or (i > 0 and picture[i-1][j] != '*')):
			# we only count a new rectangle if it's the first * encountered (after .)
			# and there isn't another on the previous line
			# so not part of an already counted rectangle
			result += 1
			while j < len(line) and line[j] == '*':
				j += 1
		j += 1
		
print(result)
		
