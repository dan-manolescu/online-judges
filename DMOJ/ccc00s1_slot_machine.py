quarters = int(input())
first = int(input())
second = int(input())
third = int(input())

plays = 0

while quarters > 0:
	machine = plays % 3
	quarters -= 1
	
	if machine == 0:
		first += 1
		if first % 35 == 0:
			quarters += 30
	elif machine == 1:
		second += 1
		if second % 100 == 0:
			quarters += 60
	elif machine == 2:
		third += 1
		if third % 10 == 0:
			quarters += 9
			
	plays += 1
		
print(f'Martha plays {plays} times before going broke.')
