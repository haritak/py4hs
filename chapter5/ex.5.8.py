import random


def showList(L):
    for i in L:
        print(i, end=" ")
    print("")

def getInput():
    i = int(input())
    while i<0 and i>9:
        i = int(input())

    return i

def reverse(L, hm):
    L1 = L[:hm]
    L2 = L[hm:]
    L1.reverse()
    L=L1+L2
    return L

def inOrder(L):
    j=1
    for i in L:
        if i!=j:
            return False
        j+=1
    return True


L = [1,2,3,4,5,6,7,8,9]

random.shuffle( L )

rounds = 0
while not inOrder(L):
    showList(L)
    how_many = getInput()
    if how_many==0:
        break


    if how_many>1:
        rounds += 1
        L = reverse(L, how_many)

if inOrder(L):
    print("Μπράβο! Τα κατάφερες!")

print("Σύνολο γύρων :", rounds, sep=" ")
