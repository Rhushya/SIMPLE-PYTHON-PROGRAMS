suits = 'hearts diamonds clubs spades'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]

random.shuffle(deck)
print(deck[:5])  
