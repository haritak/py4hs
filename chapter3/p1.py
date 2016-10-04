import random

secret = random.randint(1,32)
#ΓΙΑ ΕΛΕΓΧΟ : εμφάνιση μυστικού αριθμού
print(secret)
while True:
    print('Μάντεψε τον αριθμό 1 εως 32')
    number=int(input())
    if number!=secret:
        print("Λάθος")
    else:
        print("Σωστά!")
        #άμεση έξοδος απο την επανάληψη
        break



