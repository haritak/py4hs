for a in range(1,1001,1):
    for b in range(a, 1001, 1):
        for c in range(b, 1001, 1):
            if a**2+b**2==c**2:
                if a+b+c==1000:
                    print(a, b, c)
                    break

print("done")

