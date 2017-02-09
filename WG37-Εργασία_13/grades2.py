ok=False
while not ok:
	t1 = int(input("Βαθμός 1ου Τετραμήνου (1-20): "))
	if t1 in range(1,21):
		ok = True
	else:
		print("Έδωσες μη επιτρεπτό βαθμό.")

ok=False
while not ok:
	t2 = int(input("Βαθμός 2ου Τετραμήνου (1-20): "))
	if t2 in range(1,21):
		ok = True
	else:
		print("Έδωσες μη επιτρεπτό βαθμό.")

ok=False
while not ok:
	finals = int(input("Βαθμός Εξετάσεων     (0-100):"))
	if finals in range(101):
		ok = True
	else:
		print("Έδωσες μη επιτρεπτό βαθμό.")

terms = (t1 + t2) / 2
finals = finals / 5
grade = (terms+finals)/2

print("Ετήσιος βαθμός              :", grade)
