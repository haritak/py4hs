def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1

    return fibo(n-1) + fibo(n-2)

def fibo_simple(n):
    if n==0:
        return 0
    if n==1:
        return 1

    Fn_1=1
    Fn_2=0
    Fn=Fn_1 + Fn_2
    for i in range(2, n):
        Fn_2 = Fn_1
        Fn_1 = Fn
        Fn = Fn_1 + Fn_2
        
    return Fn

for i in range(1,10):
    print( fibo(i)==fibo_simple(i) )

