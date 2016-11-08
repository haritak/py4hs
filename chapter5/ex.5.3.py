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

    answers = []
    while correct not in answers:
        random.shuffle( possible )
        answers = possible[0:3]

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
    answers = planets.copy()
    print("Ποιός πλανήτης είναι ", end=" ")
    if position!=0:
        print("μετά τον πλανήτη ", planets[position-1], end=" ")
        answers.remove(planets[position-1])
        if position!=nbPlanets-1:
            print("και", end=" ")

    if position!=nbPlanets-1:
        print("πριν τον πλανήτη ", planets[position+1], end=" ")
        answers.remove(planets[position+1])

    print(";")
    multipleChoice(4, answers, planet)


def closestSun(planets):
    nbPlanets = len(planets)
    position = random.randint(0, nbPlanets-4)
    planet = planets[position]
    following = planets[position:len(planets)] # ή following=planets[position:]

    print("Ποιός πλανήτης είναι πιο κοντά στον Ήλιο;")
    multipleChoice(4, following, planet)



def between(planets):
    nbPlanets=len(planets)
    start = random.randint(0, nbPlanets-5)
    stop = start+4

    between = planets[start+1:stop]
    out = planets[:start] + planets[stop+1:]
    correct = random.choice(out)

    print("Ποιόν πλανήτη δε θα συναντήσουμε",
            "ταξιδεύοντας απο τον πλανήτη",
            planets[start], "και φτάνοντας",
            "στον πλανήτη", planets[stop],";", sep=" ")
    multipleChoice(4, between+[correct], correct)


def outOfOrder(planets):
    nbPlanets=len(planets)
    start = random.randint(0, nbPlanets-5)
    fourPlanets = planets[start:start+4]
    shuffled = fourPlanets.copy()
    random.shuffle( shuffled )

    print("Βάλε τους πλανήτες με την σωστή σειρά:")
    showMultiple(shuffled)
    print("")
    print("Δώσε τέσσερεις αριθμούς με κενά ανάμεσά τους")
    answer=input().split()

    correct=[]
    for planet in fourPlanets:
        position = shuffled.index(planet) + 1
        correct.append( str(position) )

    if answer==correct:
        print( "Μπράβο η σειρά είναι σωστή")
    else:
        print("Η σωστή σειρά είναι :")
        print(correct)



if addPluto():
    planets.append("Πλούτωνας")

print("Ερώτηση 1:")
findByName(planets)

print("Ερώτηση 2:")
findByPosition(planets)
print("\nΕρώτηση 3")
findByNeighbours(planets)
print("\nΕρώτηση 4")
closestSun(planets)


print("\nΕρώτηση 5")
between(planets)

print("\nΕρώτηση 6")
outOfOrder(planets)

