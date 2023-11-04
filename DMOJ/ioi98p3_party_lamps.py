# IOI '98 P3 - Party Lamps

# Main program

import sys
input = sys.stdin.readline

# Read input
n = int(input())
c = int(input())
on_lamps = [int(item) for item in input().split()]
on_lamps.pop()
off_lamps = [int(item) for item in input().split()]
off_lamps.pop()

configurations = set()

# Determine for each button if it was pressed an even (0) or odd (1)
# number of times
for button1 in [0,1]:
	for button2 in [0,1]:
		for button3 in [0,1]:
			for button4 in [0,1]:
				# if the number of combiantions exceeds the number of presses skip
				if button1 + button2 + button3 + button4 > c:
					continue
				if (button1 + button2 + button3 + button4) % 2 != c % 2:
					continue
				# initial state all lamps are on
				state = [1] * n
				# a button pressed an even number resets its action
				if button1 == 1:
					state = [0] * n

				if button2 == 1:
					for i in range(0, n, 2):
						state[i] = 1 - state[i]
				
				if button3 == 1:
					for i in range(1, n, 2):
						state[i] = 1 - state[i]
				
				if button4 == 1:
					for i in range(0, n, 3):
						state[i] = 1 - state[i]
						
				good = True
				for lamp in on_lamps:
					if state[lamp - 1] == 0:
						good = False
						break
				for lamp in off_lamps:
					if state[lamp - 1] == 1:
						good = False
						break
						
				if good:
					configurations.add(tuple(state))
					
if not configurations:
	print('IMPOSSIBLE')
else:
	for config in configurations:
		config = [str(item) for item in list(config)]
		print(''.join(config))

