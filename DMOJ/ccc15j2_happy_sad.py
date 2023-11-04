mood = input()

happy = mood.count(':-)')
sad = mood.count(':-(')

if happy == 0 and sad == 0:
	print('none')
elif happy > sad:
	print('happy')
elif happy < sad:
	print('sad')
else:
	print('unsure')
