import random

while True:
    card1 = random.randint(1,11)
    card2 = random.randint(card1+2,13)
    d = card2-card1
    mult = 12/d

    bet = int(input("Πόσο στοιχηματίζεις; "))
    c = int(input("Τί επιλέγεις; "))
    price = bet*mult
    if c>card1 and c<card2:
        print("Κέρδισες ", price)
    else:
        print("Εχασες. Οι αριθμοί ήταν ", card1, card2,
                "και θα κέρδιζες ", price)

