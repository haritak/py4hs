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
    print("Παίκτη", player, "πόσα σπίρτα θέλεις να βγάλεις;")
    num=int(input())
    while num<1 or num>limit:
        print("Πάρε από ένα μέχρι",limit,"σπίρτα")
        print("Παίκτη", player, "πόσα σπίρτα θέλεις να βγάλεις;")
        num=int(input())

    return num

def randomMatches(m):
    return random.randint(1,maxMatches(m))


matches=random.randint(7,21)

computer = random.randint(1,2)

print("Αρχικό πλήθος σπίρτων:",matches)

player=1

while matches>0:
    if player==computer:
        removed = randomMatches(matches)
        print("Ο υπολογιστής πήρε", removed, "σπίρτα")
    else:
        removed=readMatches(player,matches)
    matches-=removed

    print("Σπίρτα που απομένουν:", matches)
    player=next(player)


if player==computer:
    print("Κέρδισε ο υπολογιστής")
else:
    print("Παίκτη", player, "κέρδισες")
