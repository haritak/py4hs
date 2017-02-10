import getpass as g
def capitalized(word):
	return word.upper().translate(str.maketrans("ΆΈΉΊΪΌΎΫΏ", "ΑΕΗΙΙΟΥΥΩ"))

#secret = capitalized(input("Δώσε τη λέξη της κρεμάλας: "))
secret = capitalized(g.getpass("Δώσε τη λέξη της κρεμάλας: "))
guess = secret[0]+(len(secret)-2)*"_"+secret[-1]
pastLetters = set()
attempts=7
over = False
while not over:
	print("\nΈχεις ακόμη",attempts,"προσπάθειες.", end="   ")
	print("Έδωσες ως τώρα:", "".join(sorted(list(pastLetters))), end="\n")
	print(guess)
	letter = capitalized(input("\nΔώσε ένα γράμμα: "))
	if not letter in pastLetters:
		badguess=True
		for i in range(1,len(secret)-1):
			if letter==secret[i]:
				badguess=False
				guess=guess[:i]+letter+guess[i+1:]
		pastLetters = pastLetters | set(letter)
		attempts-=badguess
	found = not "_" in guess
	failed = attempts==0 and not found
	over = found or failed
print(found*"Μπράβο!"+failed*"Ατύχησες...") 
print(secret)
