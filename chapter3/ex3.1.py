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

found = False
tries = 4
while not found and tries>=0:
    number=readNumber(low, high)
    #number=midNumber(low, high)
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
    else:
        print("Σωστά!")
        #άμεση έξοδος απο την επανάληψη
        found = True
if not found:
    print("Ηταν ο", secret)




