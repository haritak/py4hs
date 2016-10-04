import random

secret = random.randint(1,32)
#ΓΙΑ ΕΛΕΓΧΟ : εμφάνιση μυστικού αριθμού
print(secret)

found = False
tries = 4
while not found and tries>=0:
    print('Μάντεψε τον αριθμό 1 εως 32')
    number=int(input())
    if number>secret:
        print("Λάθος, είναι μικρότερος")
        print("Απομένουν", tries, "προσπάθειες")
        tries-=1
    elif number<secret:
        print("Λάθος, είναι μεγαλύτερος")
        print("Απομένουν", tries, "προσπάθειες")
        tries-=1
    else:
        print("Σωστά!")
        #άμεση έξοδος απο την επανάληψη
        found = True
if not found:
    print("Ηταν ο", secret)




