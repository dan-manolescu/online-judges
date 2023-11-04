for _ in range(10):
	t, n = input().split()
	t, n = int(t), int(n)
	
	delay = 0
	for i in range(n):
		if input() == 'B':
			delay = delay + t if delay >= i else i + t
	
	if delay > n:
		print(delay - n)
	else:
		print(0)
