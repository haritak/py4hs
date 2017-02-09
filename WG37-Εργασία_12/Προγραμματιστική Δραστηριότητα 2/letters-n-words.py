import random
import string

def draw_cards():
#20 τυχαία γράμματα σε τυχαία σειρά στη μία πλευρά
	s1=random.sample(list(string.ascii_uppercase), 20)

#Τα 6 γράμματα που δεν μπήκαν στην πλευρά
	remaining=set(list(string.ascii_uppercase)) - set(s1)

#Στην άλλη πλευρά τα 6 γράμματα και άλλα 14 διαφορετικά τυχαία
#με τυχαία σειρά
	s2=random.sample(
	 random.sample(list(set(string.ascii_uppercase)-remaining),14)
                                                  +list(remaining),20)

#οι κάρτες με τα γράμματα στις δύο πλευρές
	cards = list(zip(s1,s2))

#εμφάνιση των καρτών     	    
	print("Οι 20 κάρτες με γράμματα είναι:")
	print(*cards,sep='\n')
	return cards
'''
Αν δεν είχαμε τον όρο να περιλαμβάνονται οπώσδηποτε μία φορά όλα τα
γράμματα του αλφάβητου, θα είχαμε απλούστερο κώδικα
cards = list(zip(random.sample(list(string.ascii_uppercase), 20),
                 random.sample(list(string.ascii_uppercase), 20)))
'''

'''#Έλεγχος, αν είναι όλο το αλφάβητο στο cards (είναι, δεν χρειάζεται)
	print(set(list(string.ascii_uppercase)) == 
          set([i for j in cards for i in j]))
'''

def make_word(word, cards):
#Return members of 'cards' that make up the 'word'

    if not word:
        return []
 
    cards_left = cards[:]
    good_cards=[]
    for char in word.upper():
        for card in cards_left:
            if char in card:
                cards_left.remove(card)
                good_cards.append(card)
                break
        else:
            return []
    return good_cards
 
play_on=True
new_batch=True
while play_on:
	while new_batch:
		cards=draw_cards()
		print("Θα αλλάξεις κάρτες; ", end="")
		new_batch=input() in ['Y', 'y']
	print("Δώσε μια λέξη με λατινικούς χαρακτήρες: ", end="")
	word=input()
	print(*make_word(word, cards),sep='\n')
	print("Θα συνεχίσεις; ", end="")
	play_on=input() in ['Y', 'y']
	if play_on:
		print("Θα αλλάξεις κάρτες; ", end="")
		new_batch=input() in ['Y', 'y']
print('Τέλος')
