t1 = int(input("Βαθμός 1ου Τετραμήνου (1-20): "))
t2 = int(input("Βαθμός 2ου Τετραμήνου (1-20): "))
finals = int(input("Βαθμός Εξετάσεων     (0-100): "))

terms = (t1 + t2) / 2
finals = finals / 5
grade = (terms+finals)/2

print("Ετήσιος βαθμός              :", grade)
