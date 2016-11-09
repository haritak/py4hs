n=int(input("Δώσε το n:"))

lines = []

for l in range(0, n):
    current_line = [1]
    for y in range(1,l):
        if y==l-1:
            current_line.append(1)
        else:
            previous_line = lines[l-1]
            current_line.append( 
                    previous_line[y-1]+
                    previous_line[y])

    lines.append(current_line)

for l in lines:
    for i in l:
        print(i, sep=" ", end=" ")
    print()



        
