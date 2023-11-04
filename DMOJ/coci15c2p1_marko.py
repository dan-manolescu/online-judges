n = int(input())

words = set()
for _ in range(n):
	words.add(input())
	
s = input()

phone = {'2': set('abc'), '3': set('def'), '4': set('ghi'), 
		'5': set('jkl'), '6': set('mno'), '7': set('pqrs'),
		'8': set('tuv'), '9': set('wxyz')}
		
for i in range(len(s)):
	chars = phone[s[i]]
	new_words = words.copy()
	for word in words:
		if i >= len(word) or word[i] not in chars:
			new_words.remove(word)
	words = new_words

print(len(words))
