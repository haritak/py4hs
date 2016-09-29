#WG37 - Ηρακλείου
import random

while True:
    load=True
    while load:
        card1 = random.randint(1,13)
        card2 = random.randint(1,13)
        d = card2-card1
        if d>1 or d<-1:
            load=False
    if d<0:
        d=d*-1    
    mult = 12/d
    print("Οι αριθμοί είναι ", card1, card2)
    bet = int(input("Πόσο στοιχηματίζεις; "))
    c=random.randint(1,13)
    print("Ο αριθμός σου είναι ", c)
    price = bet*mult
    if ((c>card1 and c<card2) or (c>card2 and c<card1)):
        print("Κέρδισες ", price)
    else:
        print("Εχασες. Οι αριθμοί ήταν ", card1, card2, "και θα κέρδιζες ", price)
