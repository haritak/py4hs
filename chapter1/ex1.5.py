#WG37 - Ηρακλείου
a=int(input("Δώσε δευτερόλεπτα"))

hours=a//(60*60)
a=a%(60*60)
minutes=a//60
seconds=a%60

print(hours,":",minutes,":",seconds)

