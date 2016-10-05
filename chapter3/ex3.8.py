import random

def setTrap(low,high):
    while True:
        print("Δώσε το πρώτο άκρο της παγίδας")
        #print("(κάτι μεγαλύτερο απο ",low,")")
        a=int(input())
        if a>=low:
            break

    while True:
        print("Δώσε το δεύτερο άκρο της παγίδας")
        #print("(κάτι μικρότερο απο ",high,")")
        b=int(input())
        if a<=high:
            break


    return a,b

def insideTrap(a,b,s):
    return s>=a and s<=b

low=1
high=32


secret = random.randint(low, high)
print("Σκέφτηκα έναν αριθμό!")

tries=4
while True:
    a,b=setTrap(low,high)
    if (a==b) and (a==secret):
        print("Μπράβο, τον βρήκες!")
        break

    if insideTrap(a,b,secret):
        print("Είναι μέσα!")
    else:
        print("Είναι απ'έξω")

    tries-=1;
    if tries==0:
        break
    else:
        print("Εχεις ακόμα ", tries, end=" ")
        if tries==1:
            print("προσπάθεια")
        else:
            print("προσπάθειες")


print("Τέλος παιχνιδιού!")



