# CCO '96 P2 - SafeBreaker

def validate_all_guesses(code, guesses):
	'''
	<code> is a string representing a 4-digit code we're attempting to validate.
	<guesses> is a list of all guessed numbers and clues.
	
	Returns True if code passes all guesses and False otherwise.
	'''
	for guess in guesses:
		if validate_guess(code, guess[0]) != guess[1]:
			return False
	return True
	
def validate_guess(code, guess):
	'''
	<code> is an string representing a 4-digit number for a code.
	<guess> is a string representing a 4-digit attempt to guess the code number.
	
	Returns a string as a clue for the guess in the format <correct digits>/<partial digits>.
	'''
	code = list(code)
	guess = list(guess)
	
	correct = 0
	for i in range(4):
		if guess[i] == code[i]:
			correct += 1
			code[i] = '*'
			guess[i] = '*'
	
	partial = 0
	for i in range(4):
		if guess[i] != '*' and guess[i] in code:
			code[code.index(guess[i])] = '*'
			partial += 1
	
	return '{0}/{1}'.format(correct, partial)	

n = int(input())
for _ in range(n):
	g = int(input())
	guesses = []
	for _ in range(g):
		guesses.append(input().split())

	code = []
	for i in range(10000):
		code_val = str(i).zfill(4)
		if validate_all_guesses(code_val, guesses):
			code.append(code_val)
		if len(code) > 1:
			break

	if len(code) == 1:
		print(code[0])
	elif len(code) > 1:
		print('indeterminate')
	else:
		print('impossible')
			
	
