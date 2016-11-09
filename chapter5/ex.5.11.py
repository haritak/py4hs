import random

TN=6

validNumbers=[]
for i in range(1,50):
    validNumbers.append(str(i))

def checkDistinct(L):
    copy = L.copy()
    for i in copy:
        copy.remove(i)
        if i in copy:
            return False
    return True

def inputNumbers():
    while True:
        print("Δώσε ",TN," διαφορετικούς αριθμούς, διαχωρίζοντάς τους με κενό:",
                sep="",end="")
        numbers=input()
        numbers=numbers.split(" ")
        if len(numbers)==TN:
            if checkDistinct(numbers):
                return numbers

def generateNumbers():
    tsouvali = validNumbers.copy()
    lottary = []
    for i in range(0,6):
        ball = random.sample(tsouvali, 1)
        tsouvali.remove(ball[0])
        lottary.append( ball[0] )

    return lottary


def compare(L1, L2):
    common = []
    for i in L1:
        if i in L2:
            common.append(i)

    return common
    

given = inputNumbers()
lottary = generateNumbers()

found = compare(lottary, given)
print("Κληρώθηκαν οι αριθμοί")
print(lottary)
if len(found)>0:
    print("Πέτυχες ", len(found), "!", sep="")
    print(found)
else:
    print("Δεν πέτυχες τίποτα!")
