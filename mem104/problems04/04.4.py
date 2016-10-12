n = int( input() )

sum = 0
for c in range(1, n+1, 1):
    sum += c

print(sum)

if sum == (1+n)*n/2:
    print("Το αποτέλεσμα είναι εντάξει")
else:
    print("Υπάρχει πρόβλημα!")

sum = 0
for c in range(1, n+1, 1):
    sum += c**2

print(sum)

