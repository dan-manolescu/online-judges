k = int(input())

a = 1
b = 0

for i in range(k):
	tmp = b
	b += a
	a = tmp
	
print(a, b)

