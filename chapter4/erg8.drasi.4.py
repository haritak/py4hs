import getpass
import time

mikosSkoylikioy=5
mikosDiadromis=15

def printRepeatedChar(char, times):
    c=0
    while c<times:
        print(char, end="")
        c+=1

def printSkouliki():
    printRepeatedChar("*", mikosSkoylikioy)

def printEndFlag(skoulikiPos):
    spaces = mikosDiadromis - skoulikiPos - mikosSkoylikioy - 1
    printRepeatedChar(" ", spaces)
    print("|")

def typwseTaSkoulikia(th1, on1, th2, on2):
    print(on1,end=" ")
    printRepeatedChar(" ", th1)
    printSkouliki()
    printEndFlag(th1)

    print(on2,end=" ")
    printRepeatedChar(" ", th2)
    printSkouliki()
    printEndFlag(th2)

def posoThes(onoma):
    print(onoma, ",πόσο βάζεις; (1-6, απλά βάλε νούμερο και πάτα εντερ, δεν θα φανεί!);")
    while True:
        a=int(getpass.getpass(""))
        if a>=1 and a<=6:
            return a

def isWinner(onoma, thesi, diadromi, skoyliki):
    iswinner = (thesi+skoyliki>=diadromi)
    if iswinner:
        print("Κέρδισε ο ", onoma, ". Έφτασε πρώτος")

    return iswinner


onoma1 = input("αρχικά πρώτου παίκτη:")
onoma2 = input("αρχικά δεύτερου παίκτη:")

thesi1 = 0
thesi2 = 0

typwseTaSkoulikia(thesi1, onoma1, thesi2, onoma2)

while True:

    a=posoThes(onoma1)
    b=posoThes(onoma2)

    if (a==b):
        print("Διαλέξατε το ίδιο, ακυρώνεστε!")

    if (a<b):
        print("Παίζει πρώτα ο ", onoma1, " γιατί διάλεξε το μικρότερο")
        time.sleep(1)
        thesi1 += a
        typwseTaSkoulikia(thesi1, onoma1, thesi2, onoma2)
        if isWinner(onoma1, thesi1, mikosDiadromis, mikosSkoylikioy):
            break
        print("")
        print("Επαιξε, τώρα παίζει ο ", onoma2)
        time.sleep(3)
        thesi2 += b
        typwseTaSkoulikia(thesi1, onoma1, thesi2, onoma2)
        if isWinner(onoma2, thesi2, mikosDiadromis, mikosSkoylikioy):
            break
    else:
        print("Παίζει πρώτα ο ", onoma2, " γιατί διάλεξε το μικρότερο")
        time.sleep(1)
        thesi2 += b
        typwseTaSkoulikia(thesi1, onoma1, thesi2, onoma2)
        if isWinner(onoma2, thesi2, mikosDiadromis, mikosSkoylikioy):
            break
        print("")
        print("Επαιξε, τώρα παίζει ο ", onoma1)
        time.sleep(3)
        thesi1 += a
        typwseTaSkoulikia(thesi1, onoma1, thesi2, onoma2)
        if isWinner(onoma1, thesi1, mikosDiadromis, mikosSkoylikioy):
            break



