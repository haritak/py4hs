correct="123"
warning=False
while True:
    if not warning:
        print("Δώσε κωδικό")
    else:
        print("Εχεις άλλες δύο προσπάθειες. Δώσε σωστά τον κωδικό.")
    a=input()
    if a!=correct and not warning:
        warning=True
    elif a!=correct and warning:
        print("Τελευταία προσπάθεια! Δώσε τον κωδικό!")
        a=input()
        if a!=correct:
          print("ΣΥΝΑΓΕΡΜΟΣ ΣΥΝΑΓΕΡΜΟΣ")
          break
        else:
            print("Παρακαλώ περάστε, μας σκάσατε...")
            break

    if a==correct:
        print("Περάστε")
        break



