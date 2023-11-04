def invert_dict(dictionary):
	'''
	dictionary to be inverted.
	
	Returns a dict keys as input dictionary values and value as a list of input
	dictionary keys corresponding to that value.
	'''
	inverted = {}
	for key in dictionary.keys():
		val = dictionary[key]
		if val not in inverted:
			inverted[val] = [key]
		else:
			inverted[val].append(key)
	return inverted

n = int(input())

lst = input().split()

lst_to_count = {}
for item in lst:
	item = int(item)
	lst_to_count[item] = 1 + lst_to_count.get(item, 0)
	
count_to_lst = invert_dict(lst_to_count)
max_mode = max(count_to_lst.keys())
print(' '.join([str(val) for val in sorted(count_to_lst[max_mode])]))


