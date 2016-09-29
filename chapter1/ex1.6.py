#WG37 - Ηρακλείου
swros1=48/3
swros2=48/3
swros3=48/3
print(swros1, " ", swros2, " ", swros3,"\n")


gia_metafora=swros1/2
swros3=swros3+gia_metafora
swros1=swros1-gia_metafora

gia_metafora=swros3/2
swros3=swros3-gia_metafora
swros2=swros2+gia_metafora

gia_metafora=swros2/2
swros2=swros2-gia_metafora
swros1=swros1+gia_metafora


print(swros1, " ", swros2, " ", swros3)
print("\n")

gia_metafora=swros2
swros1=swros1-gia_metafora
swros2=swros2+gia_metafora
gia_metafora=swros3
swros2=swros2-gia_metafora
swros3=swros3+gia_metafora
gia_metafora=swros1
swros3=swros3-gia_metafora
swros1=swros1+gia_metafora

print(swros1, " ", swros2, " ", swros3)
print("\n")

