#WG37 - Ηρακλείου
import random

def flip():
    return random.randint(0,1)

while True:
    x=int(input("δώσε 0 για κορώνα, 1 για γράμματα "))

    if x==flip():
        print("Κέρδισες")
    else:
        if x!=0 and x!=1:
            break
        print("Εχασες")
