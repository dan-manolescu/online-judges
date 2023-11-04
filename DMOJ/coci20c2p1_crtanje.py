n = int(input())

# we need to account for a matrix of -n to +n
# so we build a list of 2n and start at n

drawing = [['.' for j in range(2 * n)] for i in range(2 * n)]

line = input()
row = n
col = 0
for i in range(len(line)):
	row_delta = 0
	if line[i] == '+':
		drawing[row][col] = '/'
		row_delta = -1
	elif line[i] == '-':
		drawing[row][col] = '\\'
		row_delta = 1
	else:
		drawing[row][col] = '_'
	col += 1
	if i < len(line) - 1 and line[i] == line[i+1]:
		row += row_delta
	elif line[i:i+2] == '+=':
		row += -1
	elif line[i:i+2] == '=-':
		row += 1

# figure out the actual limits of the drawing
# by figuring the first and last row,col where a special char starts to appear		
min_col, min_row, max_row, max_col = 2*n, 2*n, -1, -1

for i in range(len(drawing)):
	for j in range(len(drawing[i])):
		if drawing[i][j] in '/\\_':
			min_row = min(min_row, i)
			min_col = min(min_col, j)
			max_row = max(max_row, i)
			max_col = max(max_col, j)

for i in range(min_row, max_row + 1):
	print(''.join(drawing[i][min_col:max_col+1]))





