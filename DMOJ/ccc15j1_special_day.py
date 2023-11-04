month = int(input())
day = int(input())

if month < 2 or (month == 2 and day < 18):
	print('Before')
elif day == 18 and month == 2:
	print('Special')
else:
	print('After')
