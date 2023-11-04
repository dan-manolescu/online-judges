# COCI '17 Contest 2 #2 ZigZag

# Read input

k, n = (int(item) for item in input().split())

letter_to_word = {}
letter_to_next_word = {}

# Build a mapping for each letter of what words can be used
for _ in range(k):
	word = input()
	if word[0] not in letter_to_word:
		letter_to_word[word[0]] = [word]
	else:
		letter_to_word[word[0]].append(word)
		
# Sort all words that can be used for each letter
for k,v in letter_to_word.items():
	letter_to_word[k] = sorted(v)
	# Map each letter to the next word
	# This will be updated to the next word every time we use it
	letter_to_next_word[k] = 0

letters = []
for _ in range(n):
	letters.append(input())

# For each letter get the word to use it and update the mapping to the next
for letter in letters:
	words = letter_to_word[letter]
	idx_word = letter_to_next_word[letter]
	print(words[idx_word])
	letter_to_next_word[letter] = idx_word + 1 if idx_word < len(words) - 1 else 0

