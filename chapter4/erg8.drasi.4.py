import getpass
import time

mikosSkoylikioy=5
mikosDiadromis=70



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

onoma1 = input("αρχικά πρώτου παίκτη:")
onoma2 = input("αρχικά δεύτερου παίκτη:")

thesi1 = 0
thesi2 = 0

typwseTaSkoulikia(thesi1, onoma1, thesi2, onoma2)

while True:

    print(onoma1)
    a=int(getpass.getpass("Πόσο βάζεις (δεν θα φανεί στην οθόνη);"))
    print(onoma2)
    b=int(getpass.getpass("Πόσο βάζεις (δεν θα φανεί στην οθόνη);"))

    if (a==b):
        print("Διαλέξατε το ίδιο, ακυρώνεστε!")

    if (a<b):
        print("Παίζει πρώτα ο ", onoma1, " γιατί διάλεξε το μικρότερο")
        time.sleep(1)
        thesi1 += a
        typwseTaSkoulikia(thesi1, onoma1, thesi2, onoma2)
        print("")
        print("Επαιξε, τώρα παίζει ο ", onoma2)
        time.sleep(3)
        thesi2 += b
        typwseTaSkoulikia(thesi1, onoma1, thesi2, onoma2)
    else:
        print("Παίζει πρώτα ο ", onoma2, " γιατί διάλεξε το μικρότερο")
        time.sleep(1)
        thesi2 += b
        typwseTaSkoulikia(thesi1, onoma1, thesi2, onoma2)
        print("")
        print("Επαιξε, τώρα παίζει ο ", onoma1)
        time.sleep(3)
        thesi1 += a
        typwseTaSkoulikia(thesi1, onoma1, thesi2, onoma2)



