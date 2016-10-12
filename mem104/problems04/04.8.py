k=int(input())

print(k)

an_1 = k
n=1
while True:
    if an_1%2==0: an = an_1//2
    else: an = 3*an_1+1
    n+=1
    an_1 = an
    print(an)
    if an==1: break
    



