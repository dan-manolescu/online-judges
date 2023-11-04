import math

order = ['orange','blue','green','yellow','pink','violet','brown','red']

for i in range(10):
	smarties = {}
	smarty = ''
	while smarty != 'end of box':
		smarty = input()
		if smarty != 'end of box':
			smarties[smarty] = 1 + smarties.get(smarty, 0)
		else:
			seconds = 0
			for o in order:
				if o in smarties:
					if o != 'red':
						seconds += math.ceil(smarties[o] / 7) * 13
					else:
						seconds += smarties[o] * 16
			print(seconds)
