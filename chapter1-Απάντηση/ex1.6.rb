h1=h2=h3=48/3
print(h1, " ", h2, " ", h3,"\n")


m=h1/2
h3=h3+m
h1=h1-m

m=h3/2
h3=h3-m
h2=h2+m

m=h2/2
h2=h2-m
h1=h1+m


print(h1, " ", h2, " ", h3)
print("\n")

m=h2
h1=h1-m
h2=h2+m
m=h3
h2=h2-m
h3=h3+m
m=h1
h3=h3-m
h1=h1+m

print(h1, " ", h2, " ", h3)
print("\n")

