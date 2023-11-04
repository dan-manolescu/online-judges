for _ in range(10):
	n = int(input())
	diameters = {} # will hold for each minimum diameter found all the roads that use it
	min_d = float('inf') # will hold the minimum diameter from all roads
	for i in range(n):
		road = [int(item) for item in input().split()]
		d = min(road[2:]) # get all diameters from the input
		if d in diameters:
			diameters[d].append(road[0])
		else:
			diameters[d] = [road[0]]
		min_d = min(min_d, d)
		
	print('%d {%s}' % (min_d, ','.join(str(road_id) for road_id in sorted(diameters[min_d]))))

	
