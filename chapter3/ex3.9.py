import random

def flipBiased(p):
    l = random.randint(1,100)
    if (l<p):
        return 0
    else:
        return 1

def flipFair():
    return random.randint(0,1)

print("Δώσε την τιμή του p (πιθανότητα στα 100 να έχει 0)")
p=int(input())

print("Δώσε αριθμό επαναλήψεων")
e=int(input())

total=e

countZeros_fair=0
countZeros_biased=0
while e>0:
    if flipBiased(p)==0:
        countZeros_biased+=1
    if flipFair()==0:
        countZeros_fair+=1
    e-=1

probFair = countZeros_fair/total
probBiased = countZeros_biased/total

print("Πιθανότητα να φέρει 0 το δίκαιο νόμισμα : ", probFair*100, "%")
print("Πιθανότητα να φέρει 0 το biased νόμισμα : ", probBiased*100, "%")

if abs(probBiased*100-p) < 1.5:
    print("Μου φαίνεται εντάξει η flipBiased")
else:
    print("Κάτι δεν πάει καλά με την flipBiased")


if abs(probFair*100-50) < 1.5:
    print("Μου φαίνεται εντάξει η flipFair")
else:
    print("Κάτι δεν πάει καλά με την flipFair")

