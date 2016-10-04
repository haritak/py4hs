import random

def getFeedback():
    print("1...Για μικρότερος")
    print("2...Για μεγαλύτερος")
    print("3...Το πέτυχες")
    a=int(input())
    while a < 1 or a>3:
        print("Δεν υπάρχει τέτοια επιλογή")
        a=int(input())

    return a

low=1
high=32

a=random.randint(low,high)
print("Διάλεξα το ",a)

f=getFeedback()
while f!=3:
    if f==1:
        high=a;
    else:
        low=a

    a=random.randint(low,high)
    print("Διάλεξα το ", a)
    f=getFeedback()

