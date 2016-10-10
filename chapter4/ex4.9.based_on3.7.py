import random

low=[0,1,1]
high=[0,32,32]

def getFeedback():
    print("1...Για μικρότερος")
    print("2...Για μεγαλύτερος")
    print("3...Το πέτυχες")
    a=int(input())
    while a < 1 or a>3:
        print("Δεν υπάρχει τέτοια επιλογή")
        a=int(input())

    return a

def readNumber(a,b):
    print('Μάντεψε τον αριθμό', a,"-",b)
    num=int(input())

    while num<a or num>b:
        num=int(input())

    return num

def showMessage(number, secret, low, high):
    if number>secret:
        print("Λάθος, είναι μικρότερος")
        return number-high-1
    elif number<secret:
        print("Λάθος, είναι μεγαλύτερος")
        return number-low+1

def nextPlayer(p, total):
    np = p+1
    if np==total+1:
        np=1
    return np

#o υπολογιστής παίρνει τυχαία σειρά και 
#διαλέγει νούμερο.
computer = random.randint(1,2)
secret = random.randint(low[1], high[2])

player = random.randint(1,2)
finished=[False, False, False]
winner=0
while not finished[1] or not finished[2]:


    if not finished[player]:
        if player==computer:
            print("Ειναι η σειρά μου")
            a=random.randint(low[player],high[player])
            print("Διάλεξα το ",a)
            f=getFeedback()

            if f!=3:
                if winner != 0:
                    print("Εχασα...")
                    break

                if f==1:
                    high[player]=a;
                else:
                    low[player]=a
            else:
                print("Ναι! Το βρήκα!")
                finished[player] = True
                if winner==0:
                    winner=player


        else:
            print("Είναι η δική σου σειρά")
            a=readNumber(low[player], high[player])
            if a != secret:
                if winner != 0:
                    print("Εχασες!")
                    break
                dif = showMessage(a, secret, low[player], high[player])
                if dif<0:
                    high[player]=high[player]+dif
                else:
                    low[player]=low[player]+dif
            else:
                print ("Μπράβο! Το βρήκες!")
                finished[player] = True
                if winner==0:
                    winner=player

    player = nextPlayer(player,2)


print ("Τέλος παιχνιδιού!")
