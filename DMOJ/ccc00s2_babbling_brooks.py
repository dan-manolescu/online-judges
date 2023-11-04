n = int(input())

streams = [int(input()) for i in range(n)]

flow = ''
while True:
	flow = input()
	if flow == '99':
		split = int(input())
		split_flow = int(input())
		original_value = streams[split-1]
		streams[split-1] = round(original_value * split_flow / 100)
		streams.insert(split, original_value - streams[split-1])
	elif flow == '88':
		join = int(input())
		streams[join-1] += streams[join]
		streams.pop(join)
	else:
		break
	
for stream in streams:
	print(stream, end=' ')
