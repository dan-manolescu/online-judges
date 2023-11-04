# Main program

input_file = open('mixmilk.in', 'r')
output_file = open('mixmilk.out', 'w')

# Read input
buckets = []
capacities = []
for _ in range(3):
	lst = input_file.readline().split()
	capacities.append(int(lst[0]))
	buckets.append(int(lst[1]))

# Loop
for i in range(100):
	first = i % 3
	second = (i + 1) % 3
	if buckets[first] + buckets[second] <= capacities[second]:
		buckets[second] += buckets[first]
		buckets[first] = 0
	else:
		buckets[first] = buckets[first] + buckets[second] - capacities[second]
		buckets[second] = capacities[second]


# Write output
for bucket in buckets:
	output_file.write(f'{bucket}\n')

input_file.close()
output_file.close()
