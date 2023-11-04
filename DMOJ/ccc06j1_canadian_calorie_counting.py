calorie = 0

burger = int(input())
if burger == 1:
	calorie += 461
elif burger == 2:
	calorie += 431
elif burger == 3:
	calorie += 420
	
side = int(input())
if side == 1:
	calorie += 100
elif side == 2:
	calorie += 57
elif side == 3:
	calorie += 70
	
drink = int(input())
if drink == 1:
	calorie += 130
elif drink == 2:
	calorie += 160
elif drink == 3:
	calorie += 118

dessert = int(input())
if dessert == 1:
	calorie += 167
elif dessert == 2:
	calorie += 266
elif dessert == 3:
	calorie += 75
	
print(f'Your total Calorie count is {calorie}.')

