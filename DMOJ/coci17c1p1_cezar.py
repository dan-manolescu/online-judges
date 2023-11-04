n = int(input())

# holding how many cards we have in the deck (4 by default)
# there are no cards with value 0 and 1 so make sure they are 0
cards = [4 if i >= 2 else 0 for i in range(12)]
# the 10 value card is 16 (4 10s, jacks, queens, kings)
cards[10] = 16

# will count the total for Cezar (how many cards he has)
total = 0

for _ in range(n):
	card = int(input())
	total += card
	cards[card] -= 1
	
diff = 21 - total
less = sum(cards[:diff+1])
greater = sum(cards[diff+1:])

if greater >= less:
	print('DOSTA')
else:
	print('VUCI')

