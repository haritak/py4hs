
stations = []
for i in range(0,24):
    stations.append( "station"+str(i))

print(stations)


def getStation(message):
    message+=":"

    station = input(message)
    while not station in stations:
        print("Δεν υπάρχει τέτοιος σταθμός")
        station = input(message)

    return station

start=getStation("Αφετηρία")
term=getStation("Προορισμός")

current_idx = stations.index(start)
term_idx = stations.index(term)
step = 1
if term_idx<=current_idx:
    step=-1

print("Διαδρομή από", end=" ")
while True:
    print(stations[current_idx], end=" ")
    if current_idx==term_idx:
        print("σταθμός αποβίβασης πρός", end=" ")
        break
    print()
    current_idx += step

if step>0:
    print(stations[len(stations)-1])
else:
    print(stations[0])






