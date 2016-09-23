import random

while True:
    u=int(input("Δώσε 1 για Πέτρα, 2 για Ψαλίδι ή 3 για Χαρτί"))
    c=random.randint(1,3)
    choices = ["","Πέτρα","Ψαλίδι","Χαρτί"]

    print("Εγώ διάλεξα", choices[c])

    if (u==c):
        print("ισοπαλία")
    elif u==3 and c==1:
        print("κέρδισες")
    else:
        if u not in [1,2,3]:
            break
        print("έχασες")

""" Δεν είναι σωστή η λογική αλλά το παρατάω...
