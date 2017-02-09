def capitalize(word):
    cap = word.upper()
    cap.replace("Ά","Α").replace("Έ","Ε").replace("Ή","Ή").replace("Ί","Ι").replace("Ϊ","Ι").replace("Ό","Ο").replace("Ύ","Υ").replace("Ϋ","Υ").replace("Ώ","Ω")
    return cap



def emfanisePavles(word, letters):
    for w in word:
        if w in letters:
            print(w, end="")
        else:
            print("_", end="")

    print()

def teleiwsame( word, letters ):
    for w in word:
        if w not in letters:
            return False

    return True

secret = input("Δώσε την μυστική λέξη:")

SECRET = capitalize(secret)
print(SECRET)

foundLetters = set( (SECRET[0], SECRET[-1]) )


while True:
    emfanisePavles( SECRET, foundLetters )
    gramma = input("Δώσε ένα γράμμα")
    gramma = capitalize(gramma)

    foundLetters = foundLetters | set(gramma)

    if teleiwsame( SECRET, foundLetters ):
        break



