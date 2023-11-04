# USACO 2019 December Contest, Bronze Problem 2. Where Am I?

input_file = open('whereami.in', 'r')
output_file = open('whereami.out', 'w')

n = int(input_file.readline())
mailboxes = input_file.readline()

k = 1
found = False
while not found:
	i = 0
	while i + k < n:
		if mailboxes[i:i+k] in mailboxes[i+1:]:
			k += 1
			break
		i += 1
	else:
		found = True

output_file.write(f'{k}\n')

input_file.close()
output_file.close()
