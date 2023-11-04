p = int(input())
n = int(input())
r = int(input())

days = 0
total = n

while total <= p:
	days += 1
	n = n * r
	total += n

print(days)
