n = int(input())

boxes = [100, 500, 1_000, 5_000, 10_000, 25_000, 50_000, 100_000, 500_000, 1_000_000]
opened = set()

for _ in range(n):
	opened.add(int(input())-1)
	
banker = int(input())

total = 0
for i in range(len(boxes)):
	total += 0 if i in opened else boxes[i]
	
avg = total / (len(boxes) - n)

if banker > avg:
	print('deal')
else:
	print('no deal')


