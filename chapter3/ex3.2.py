import random
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

low=1
high=32

secret = random.randint(low, high)
#ΓΙΑ ΕΛΕΓΧΟ : εμφάνιση μυστικού αριθμού
print(secret)

tries = 4
number=readNumber(low, high)
#number=midNumber(low, high)
while number!=secret and tries>=0:
    if number>secret:
        print("Λάθος, είναι μικρότερος")
        high = number-1
        print("Απομένουν", tries, "προσπάθειες")
        tries-=1
    elif number<secret:
        print("Λάθος, είναι μεγαλύτερος")
        low=number+1
        print("Απομένουν", tries, "προσπάθειες")
        tries-=1
    number=readNumber(low, high)
    #number=midNumber(low, high)

if number!=secret:
    print("Ηταν ο", secret)
else:
    print("Σωστά!")
    #άμεση έξοδος απο την επανάληψη




