for _ in range(10):
	lst = input().split()
	n = int(lst[0])
	m = int(lst[1])
	d = int(lst[2])
	
	events = {} 
	# capture all events in a dictionary 
	# (key: event day, val: number of shirts) 
	# as there can be multiple events per day
	for event in input().split():
		event = int(event)
		events[event] = 1 + events.get(event, 0)
		
	# initialize total shirts and how many are clean
	total = n
	clean = total
	washes = 0
	for day in range(1, d+1):
		if day in events:
			total += events[day]
			clean += events[day]
		clean -= 1
		if clean == 0 and day != d:
			washes += 1
			clean = total
	print(washes)
