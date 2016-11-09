import random

#0 Terminates
#1 Gives a hint

#playAlone = False
playAlone = True

def suggestMove(L):

    #Start from the right side
    #and spot the first out of order number
    i=9
    while i>1 and L[i-1] == i:
        i-=1

    if i==0:
        return 0

    target = i
    #debugging : 
    #print("Out of order is number ", target)

    #locate target in the list
    target_index = L.index( target )+1
    #debugging : 
    #print("Which is at place ", target_index)

    #if it's on the first position
    #just flip the list
    if target_index==1:
        return target

    #bring it to the first
    return target_index

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
    if playAlone:
        how_many = suggestMove(L)
    else:
        how_many = getInput()
    if how_many==0:
        break
    if how_many==1:
        print(suggestMove(L))


    if how_many>1:
        rounds += 1
        L = reverse(L, how_many)

if inOrder(L):
    print("Μπράβο! Τα κατάφερες!")

print("Σύνολο γύρων :", rounds, sep=" ")
