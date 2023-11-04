n = int(input())

positions = []

for i in range(n):
	positions.append(int(input()))
	
positions.sort()

min_size = float('inf')

for i in range(1, n-1):
	left = (positions[i] - positions[i-1]) / 2
	right = (positions[i+1] - positions[i]) / 2
	size = left + right
	min_size = min(min_size, size)
		
print(min_size)
