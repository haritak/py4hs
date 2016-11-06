#
planets = ["Ερμής", "Αφροδίτη", "Γη", "Αρης", "Δίας", "Κρόνος",
        "Ουρανός", "Ποσειδώνας"]

def addPluto():
    '''
    '''
    #
    print("Να θεωρήσουμε τον Πλούτωνα πλανήτη (ν/ο);")
    answer = input()

    return answer in "yYΝν"

if addPluto():
    planets.append("Πλούτωνας")


import random

def findByName(planets):
    nbPlanets = len(planets)
    position = random.randint(0, nbPlanets-1)
    planet = planets[position]

    print("Σε ποιά σειρά βρίσκεται ο πλανήτης ",planet, 
            " σε σχέση με τον Ηλιο;", sep="")
    answer = int(input())

    if answer==position+1:
        print("Μπράβο, το βρήκες!")
    else:
        print ("Ο πλανήτης ", planet, " είναι ο ", position+1,
                "ος πλανήτης.", sep="")


print("Ερώτηση 1:")
findByName(planets)

def findByPosition(planets):
    nbPlanets = len(planets)
    position = random.randint(0, nbPlanets-1)
    planet = planets[position]

    print("Ποιός είναι ο ", position+1, "ος πλανήτης μετά τον Ηλιο;", 
            sep="")
    answer = input()
    if answer.lower().strip() == planet.lower():
        print( "Μπράβο!" )
    else:
        print( "Είναι ο πλανήτης ", planet, ".", sep="")



print("Ερώτηση 2:")
findByPosition(planets)


