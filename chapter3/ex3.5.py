import random

def computeNumber(a,b,tries):
    if tries>1:
        return midNumber(a,b)
    else:
        return random.randint(a, b)

def midNumber(a,b):
    print('Μάντεψε τον αριθμό', a,"-",b)
    num = (a+b)//2
    print("Ο υπολογιστής επιλέγει:", num)
    return num

def readNumber(a,b):
    print('Μάντεψε τον αριθμό', a,"-",b)
    num=int(input())

    while num<a or num>b:
        num=int(input())

    return num

def showMessage(number, secret, low, high):
    if number>secret:
        print("Λάθος, είναι μικρότερος")
    elif number<secret:
        print("Λάθος, είναι μεγαλύτερος")


low=1
high=32

tries = 4
number=readNumber(low, high)
#number=midNumber(low, high)
#number=computeNumber(low, high, tries)
while low!=high and tries>1:
    if (number-low>high-number):
        secret=low
    else:
        secret=high
    showMessage(number, secret, low, high)
    if number>secret:
        high = number-1
        print("Απομένουν", tries, "προσπάθειες")
        tries-=1
    elif number<secret:
        low=number+1
        print("Απομένουν", tries, "προσπάθειες")
        tries-=1
    number=readNumber(low, high)
    #number=midNumber(low, high)
    #number=computeNumber(low, high, tries)

if low!=high:
    if (number-low>high-number):
        secret=low
    else:
        secret=high

    if number>secret:
        high = number-1
    elif number<secret:
        low=number+1
    showMessage(number, secret, low, high)
    print("Τελευταία προσπάθεια!")
    number = readNumber(low, high)
    #number=computeNumber(low, high, tries)

    if (number-low>high-number):
        secret=low
    else:
        secret=high

    if number>secret:
        high = number-1
    elif number<secret:
        low=number+1

if low!=high:
    secret = random.randint(low, high)
    #ΓΙΑ ΕΛΕΓΧΟ : εμφάνιση μυστικού αριθμού
    print(secret)
    print("Ηταν ο", secret)
else:
    print("Σωστά!")
    #άμεση έξοδος απο την επανάληψη




