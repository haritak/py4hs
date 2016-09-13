a=input("Δώσε μου ένα αριθμό")
b=input("Δώσε άλλο έναν αριθμό")

a=int(a)
b=int(b)

while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a


print("Ο μέγιστος κοινός διαιρέτης είναι το ", a)
