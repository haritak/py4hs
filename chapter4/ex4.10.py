import random

def generatePair(level):
    if level==1:
        while True:
            x=random.randint(0,9)
            y=random.randint(0,9)
            if x+y<9:
                return x,y
    elif level==2:
        while True:
            x=random.randint(0,9)
            y=random.randint(0,9)
            if x+y>10:
                return x,y
    elif level==3:
        while True:
            x=random.randint(0,98)
            y=random.randint(0,9)
            if x+y<100:
                return x,y
    elif level==4:
        while True:
            x=random.randint(0,99)
            y=random.randint(0,99)
            if x>10 and y>10:
                return x,y
    else:
        return random.randint(0,99), random.randint(0,99)

def correctAnswer(a,b,op):
    if op=="+":
        return a+b
    if op=="-":
        return a-b
    if op=="*":
        return a*b
    if op=="/":
        return a/b

def giveHint(a,b,op,tries):
    if tries==0:
        if op=="+":
            print("Η απάντηση είναι :", a+b)
        if op=="-":
            print("Η απάντηση είναι :", a-b)
        if op=="*":
            print("Η απάντηση είναι :", a*b)
        if op=="/":
            print("Η απάντηση είναι :", a/b)
    elif tries==1:
        if op=="+":
            addition_hint1_breakNumbers(a,b)
        if op=="-":
            print("Σκέψου πιο προσεκτικά")
        if op=="*":
            print("Σκέψου πιο προσεκτικά")
        if op=="/":
            print("Σκέψου πιο προσεκτικά")


def breakNumber(a):
    if a==0:
        print("",end="")
    elif a<5:
        print(a, end=" ")
    elif a<9:
        print("5+",a-5,end=" ")
    else:
        print( (a//10)*10, end=" ")
        if a%10!=0:
            print("+",end=" ")
            breakNumber(a%10)
        else:
            print("",end="")

def addition_hint1_breakNumbers(a,b):
    if a<5 and b<5:
        return
    print("Παρατήρησε:")
    print(a,"+",b,"=",end=" ")
    breakNumber(a)
    print(" + ", end="")
    breakNumber(b)
    print("=?")



        

while True:
    level=int(input("Δώσε επιθυμητό επίπεδο (1-4)"))
    op=input("Δώσε επιθυμητή πράξη (+, -, *, /)")

    for c in range(1,5):
        a,b = generatePair(level)
        solution=correctAnswer(a,b,op)
        tries=2
        while tries>=0:
            print("Πόσο κάνει", a,op,b,";")
            x=int(input())
            if x!=solution:
                tries-=1
                giveHint(a,b,op,tries)
            else:
                print("Μπράβο, το βρήκες!")
                break


