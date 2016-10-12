a=input()

i=0
e=-1
itsnot=False
while i < len(a)//2:
    if a[i]!=a[e]:
        itsnot=True
        break
    i+=1
    e-=1

if itsnot:
    print("It's not")
else:
    print("It is")

