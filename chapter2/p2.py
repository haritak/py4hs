import random

def rollDice():
    print ("Πάτα έντερ για να πέσουν τα ζάρια", end=" ")
    input()

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    roll = dice1 + dice2
    print( "Εριξες", dice1, dice2, "=", roll)

    return roll

roll = rollDice()

if roll==7 or roll==11:
    print("Κέρδισες με την πρώτη!")
elif roll<=3 or roll==12:
    print("..έχασες με την πρώτη")
else:
    while True:
        print("Ξαναρίξε! Πρέπει να φέρεις", roll)
        newroll = rollDice()
        if newroll==roll:
            print("Κέρδισες!")
            break
        elif newroll==7:
            print("Εχασες")
            break


