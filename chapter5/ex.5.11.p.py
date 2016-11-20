import random

def inputNumbers():
	numbers=[]
	count=1
	while count<7:
		print("Δώσε τον "+str(count)+"ο αριθμό σου: ",end="") 
		x=int(input())
		if x in set(range(1,50))-set(numbers):
			numbers=numbers+[x]
			count+=1
	return numbers

def generateNumbers():
	return random.sample(range(1,50), 6)

def compare(L1, L2):
    return list(set(L1) & set(L2))

given = inputNumbers()
lottery = generateNumbers()
found = compare(lottery, given)

print("Κληρώθηκαν οι αριθμοί:", lottery)
if found:
    print("Πέτυχες "+str(len(found))+": ", found)
else:
    print("Δεν πέτυχες τίποτα!")

