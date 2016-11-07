#
import random

planets = ["Ερμής", "Αφροδίτη", "Γη", "Αρης", "Δίας", "Κρόνος",
        "Ουρανός", "Ποσειδώνας"]

def addPluto():
    '''
    '''
    #
    print("Να θεωρήσουμε τον Πλούτωνα πλανήτη (ν/ο);")
    answer = input()

    return answer in "yYΝν"

def select(nbChoices, possible, correct):
    '''
    nbChoices:πλήθος απαντήσεων που θα επιλεχθούν
    possible:λίστα όλων των πιθανών απαντήσεων 
    correct: σωστή απάντηση
    '''

    answers = random.sample(possible, nbChoices)
    if correct not in answers:
        index = random.randint(0, nbChoices-1)
        answers[index] = correct

    return answers


def showMultiple(answers):
    number=1
    for answer in answers:
        print("(", number, ") ", answer, sep="", end= " ")
        number+=1

def readAnswer(nbChoices):
    while True:
        choice = int(input())
        if choice<1 or choice>nbChoices:
            print("μη επιτρεπτός αριθμός")
        else:
            break

    return choice


def multipleChoice(nbChoices, possible, correct):
    '''
    nbChoices: πλήθος απαντήσεων που θα εμφανιστούν
    possible: λίστα όλων των πιθανών απαντήσεων
    correct: η σωστή απάντηση
    '''
    answers = select(nbChoices, possible, correct)
    showMultiple(answers)
    playerChoice= readAnswer(nbChoices)
    if answers[playerChoice-1] == correct:
        print("Μπράβο το βρήκες")
    else:
        print("Η σωστή απάντηση είναι ", correct, ".")
        


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

def findByPosition(planets):
    nbPlanets = len(planets)
    position = random.randint(0, nbPlanets-1)
    planet = planets[position]

    print("Ποιός είναι ο ", position+1, "ος πλανήτης μετά τον Ηλιο;", 
            sep="")
    multipleChoice(4, planets, planet)

def findByNeighbours(planets):
    nbPlanets = len(planets)
    position = random.randint(0, nbPlanets-1)
    planet = planets[ position ]
    print("Ποιός πλανήτης είναι ", end=" ")
    if position!=0:
        print("μετά τον πλανήτη ", planets[position-1], end=" ")
        if position!=nbPlanets-1:
            print("και", end=" ")

    if position!=nbPlanets-1:
        print("πριν τον πλανήτη ", planets[position+1], end=" ")

    print(";")
    multipleChoice(4, planets, planet)



print("\nΕρώτηση 3")
findByNeighbours(planets)





if addPluto():
    planets.append("Πλούτωνας")

print("Ερώτηση 1:")
findByName(planets)

print("Ερώτηση 2:")
findByPosition(planets)
