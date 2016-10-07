import random

def next(p,q):
    if p==q:
        return 1
    else:
        return p+1
    #return (p%q)+1

def maxMatches(m):
    if m>4:
        return 4
    else:
        return m

def readMatches(p,m):
    limit=maxMatches(m)
    print("Παίκτη", player, "πόσα σπίρτα θέλεις να βγάλεις;")
    num=int(input())
    if num<1 or num>limit:
        while True:
            print("Πάρε από ένα μέχρι",limit,"σπίρτα")
            print("Παίκτη", player, "πόσα σπίρτα θέλεις να βγάλεις;")
            num=int(input())
            if (num>=1 and num<=limit):
                break

    return num

def randomMatches(m):
    return random.randint(1,maxMatches(m))

def computeMatches(m, mym):
    if mym%2==1:
        if m==1 or m==3:
            return m
        elif m==2 or m==4:
            return m-1
        elif m==6:
            return 3
        else:
            return randomMatches(m)
    else:
        if m==1 or m==2:
            return m
        elif m==3:
            return 2
        elif m==4 or m==5:
            return 4
        else:
            return randomMatches(m)

def announceWinner(matchesGathered,computer):
    if matchesGathered[computer]%2 ==0:
        print("Κέρδισε ο υπολογιστής, γιατί μάζεψε", matchesGathered[computer], "σπίρτα")
    else:
        print("Παίκτη",player,"κέρδισες.")

matches=random.randint(7,21)
if matches%2==0:
    matches+=1

computer = random.randint(1,2)

print("Αρχικό πλήθος σπίρτων:",matches)

player=1

matchesGathered = [0,0,0]

while matches>0:
    print("Σπίρτα που απομένουν:", matches)
    if player==computer:
        #removed = randomMatches(matches)
        removed = computeMatches(matches, matchesGathered[computer])
        print("Ο υπολογιστής πήρε", removed, "σπίρτα")
    else:
        removed=readMatches(player,matches)

    matchesGathered[ player ] += removed
    matches-=removed

    player=next(player,2)

announceWinner(matchesGathered, computer)

