def getGrade(term):
# διαβάζει και επιστρέφει έγκυρο βαθμό βαθμολογικής περιόδου

	if term==1 or term==2:
		message="Βαθμός "+str(term)+"ου Τετραμήνου (1-20): "
		r=range(1,21)
	elif term==3:
		message="Βαθμός Εξετάσεων     (0-100): "
		r=range(101)

	ok=False
	while not ok:
		grade = int(input(message))
		if grade in r:
			ok = True
		else:
			print("Έδωσες μη επιτρεπτό βαθμό.")
	return grade

def myround(number,digits):
	return(int(number*10**digits+0.5)/10**digits)

t1 = getGrade(1)
t2 = getGrade(2)
finals = getGrade(3)

terms = (t1 + t2) / 2
finals = finals / 5
grade = myround((terms+finals)/2,1)

print("Ετήσιος βαθμός              :", grade)
