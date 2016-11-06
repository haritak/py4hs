def dividingPower(n):
    i=0;
    while 2**i < n:
        i+=1

    for j in range(i, -1, -1):
        if (n / 2**j == n//2**j):
            break

    return j

print( dividingPower(4)==2 )
print( dividingPower(16)==4 )
print( dividingPower(3)==0 )
print( dividingPower(7)==0 )
print( dividingPower(256)==8 )


