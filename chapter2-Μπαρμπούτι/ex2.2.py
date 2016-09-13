a=int(input("Δώσε τον αριθμό εκκίνησης "))

step=1
m=a
while a!=1:
    if a%2==1:
        a=a*3+1
    else:
        a=a/2

    print(a)
    if a>m:
        m=a
    step = step+1

print("Πλήθος βημάτων", step)
print("Μέγιστος αριθμός το ", m)
