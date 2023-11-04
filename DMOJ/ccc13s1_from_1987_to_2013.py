def is_year_distinct_digits(year):
	"""
	year is an integer representing a year
	
	Returns True if year is composed of distinct digits, False otherwise
	"""
	s = str(year)
	return len(s) == len(set(s))

# Main program

# Read input
y = int(input())

# Check every year after input until one is correct
year = y + 1
keep_looking = True
while keep_looking:
	if is_year_distinct_digits(year):
		keep_looking = False
	else:
		year += 1
		
print(year)
