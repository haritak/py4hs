import random
def next(p):
    if p==1:
        return 2
    else:
        return 1
    #return (p%2)+1

def maxMatches(m):
    if m>3:
        return 3
    else:
        return m

def readMatches(p,m):
    limit=maxMatches(m)
    if limit>1:
        print("Παίκτη", player, "πόσα σπίρτα θέλεις να βγάλεις;")
        num=int(input())
        if num<1 or num>limit:
            while True:
                print("Πάρε από ένα μέχρι",limit,"σπίρτα")
                print("Παίκτη", player, "πόσα σπίρτα θέλεις να βγάλεις;")
                num=int(input())
                if (num>=1 and num<=limit):
                    break
    else:
        print("Παίκτη", player, "αναγκαστικά πρέπει να παρεις το τελευταίο σπίρτο.")
        num=1

    return num

def randomMatches(m):
    return random.randint(1,maxMatches(m))

def computeMatches(m):
    mod=m%4
    if mod==0:
        return 1
    else:
        return mod

def announceWinner(player, computer):
    if player==computer:
        print("Παίκτη", player, "κέρδισες")
    else:
        print("Κέρδισε ο υπολογιστής")

matches=random.randint(7,21)

computer = random.randint(1,2)

print("Αρχικό πλήθος σπίρτων:",matches)

player=1

while matches>0:
    print("Σπίρτα που απομένουν:", matches)
    if player==computer:
        #removed = randomMatches(matches)
        removed = computeMatches(matches)
        print("Ο υπολογιστής πήρε", removed, "σπίρτα")
    else:
        removed=readMatches(player,matches)
    matches-=removed

    player=next(player)

announceWinner(player,computer)

