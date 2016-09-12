import time
a=input("Πότε γεννήθηκες; ")
y=time.localtime().tm_year

a=y-int(a)
if a<15:
    print("You ain't allowed to use this machine")
else:
    print("Ok")
    

print(a)
