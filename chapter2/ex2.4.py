#WG37 - Ηρακλείου
import random

game = True
while game:
    choice=int(input("Διάλεξε 1-Πέτρα, 2-Ψαλίδι ή 3-Χαρτί"))
    if choice!=1 and choice!=2 and choice!=3:
        game=False
    else:
        mychoice=random.randint(1,3)
        print("Εγώ διάλεξα ", mychoice)
        if (mychoice==1 and choice==2) or (mychoice==2 and choice==3) or (mychoice==3 and choice==1):
            print("Εγώ κερδίζω!")
        elif (choice==1 and mychoice==2) or (choice==2 and mychoice==3) or (choice==3 and mychoice==1):
            print("Εσύ κερδίζεις!")
        else:
            print("Ισοπαλία")
    print("Συνεχίζουμε;...")
