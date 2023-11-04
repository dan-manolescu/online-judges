# Avocado Trees!

import sys
input = sys.stdin.readline

n, q, h = (int(item) for item in input().split())

# Build a prefix sum
prefix_tree = []
prefix_sum = 0
for _ in range(n):
	height, avocado = (int(item) for item in input().split())
	# keep only avocadoes for trees with proper height
	if height > h:
		avocado = 0
	prefix_sum += avocado
	prefix_tree.append(prefix_sum)
	
max_avocado = 0
for _ in range(q):
	start, end = (int(item) for item in input().split())
	# This is the prefix sum we need to decrease to compensate for ranges starting beyond 1
	prefix_sum = prefix_tree[start-2] if start > 1 else 0
	max_avocado = max(max_avocado, prefix_tree[end-1] - prefix_sum)
	
print(max_avocado)
