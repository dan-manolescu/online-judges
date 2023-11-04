word = input()

while word != 'quit!':
	if (len(word) > 4 and
		word[-2:] == 'or' and
		word[-3].lower() not in 'aeiouy'):
			word = word[:-1] + 'ur'
	
	print(word)
	word = input()

		
