a=int(input("Δώσε δευτερόλεπτα"))

s=a%60
a=a//60
m=a%60
a=a//60
h=a%60

print(h,":",m,":",s)

