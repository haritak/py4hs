n=int(input("Δώσε το n:"))

lines = []

for l in range(0, n):
    current_line = [1]
    for y in range(1,l+1):
        if y==l:
            current_line.append(1)
        else:
            previous_line = lines[l-1]
            new = previous_line[y-1]+previous_line[y]
            current_line.append( new )

    print(current_line)
    lines.append(current_line)

print("----")
for l in lines:
    for i in l:
        print(i, sep=" ", end=" ")
    print()



        
