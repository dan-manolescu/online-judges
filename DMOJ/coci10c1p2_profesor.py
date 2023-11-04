# COCI '10 Contest 1 #2 Profesor

def add_desk_to_grade(grade, desk, grade_to_desks, result_cnt, result_grade):
	'''
	grade is an integer representing a grade for a student.
	desk is an integer representing the desk number where the student sits.
	grade_to_desks is a dictionary mapping grades to list of desks where
	students with those grades sit.
	result_grade is an integer for the current result grade
	result_cnt is the current maximum number of students with result_grade
	
	Updates grade_to_desks to include the given grade and desk number and
	returns the current result_grade and result_cnt
	'''
	current, maximum = 1, 1
	
	if grade in grade_to_desks:
		prev_desk, current, maximum = grade_to_desks[grade]
		if desk == prev_desk + 1:
			current += 1
			maximum = max(maximum, current)
		else:
			current = 1
	
	grade_to_desks[grade] = (desk, current, maximum)
	
	if maximum > result_cnt:
		result_cnt = maximum
		result_grade = grade
	elif maximum == result_cnt:
		result_grade = min(grade, result_grade)
	
	return result_cnt, result_grade
		

# Main program

# Read input

n = int(input())

# dictionary will map grades to a 
# tuple of (last desk having this grade, current consecutive desk number
# and max consecutive desk numbers so far
grade_to_desks = {}
result_grade = 0
result_cnt = 0

for i in range(n):
	grade1, grade2 = (int(item) for item in input().split())
	result_cnt, result_grade = add_desk_to_grade(grade1, i, grade_to_desks, result_cnt, result_grade)
	if grade1 != grade2:
		result_cnt, result_grade = add_desk_to_grade(grade2, i, grade_to_desks, result_cnt, result_grade)

# Write output
print(result_cnt, result_grade)

