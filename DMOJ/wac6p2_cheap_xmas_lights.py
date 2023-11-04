# Wesley's Anger Contest 6 Problem 2 - Cheap Christmas Lights

# Main program

import sys
input = sys.stdin.readline

# Read input
n, m = (int(item) for item in input().split())
lights = []
on_lights = 0
for i in input().split():
	light = int(i)
	if light:
		on_lights += 1
	lights.append(light)
flips = [int(item) for item in input().split()]

# Loop each second, count lights and flip others
seconds = 0
while seconds < m and seconds < on_lights:
	flip_light = flips[seconds] - 1
	if lights[flip_light] == 1:
		lights[flip_light] = 0
		on_lights -= 1
	else:
		lights[flip_light] = 1
		on_lights += 1
	seconds += 1

# Write output
if seconds < on_lights:
	print(on_lights)
else:
	print(seconds)
