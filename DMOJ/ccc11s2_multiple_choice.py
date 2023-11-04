n = int(input())

student_ans = [None] * n
correct_ans = [None] * n

correct_num = 0

for i in range(n):
	student_ans[i] = input()
	
for i in range(n):
	correct_ans[i] = input()
	if student_ans[i] == correct_ans[i]:
		correct_num += 1

print(correct_num)
	

