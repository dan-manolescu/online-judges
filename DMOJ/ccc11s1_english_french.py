n = int(input())

char_t = 0
char_s = 0

for i in range(n):
	text = input()
	for c in text:
		if c == 't' or c == 'T':
			char_t += 1
		elif c == 's' or c == 'S':
			char_s += 1

if char_t > char_s:
	print('English')
else:
	print('French')

