low=[0,1,1]
high=[0,32,32]
tries=[0,4,4]

def getFeedback()
    puts("1...Για μικρότερος")
    puts("2...Για μεγαλύτερος")
    puts("3...Το πέτυχες")
    begin
      puts("Τί επιλέγεις; (1-3)")
      a=gets.chomp.to_i
    end while a < 1 or a>3:

    return a
end

def readNumber(a,b)
    puts("Μάντεψε τον αριθμό #{a}-#{b}")
    begin
      num=gets.chomp.to_i
    end while num<a or num>b

    return num
end

def showMessage(number, secret, low, high)
    if number>secret
        puts("Λάθος, είναι μικρότερος")
        return number-high-1
    elsif number<secret
        puts("Λάθος, είναι μεγαλύτερος")
        return number-low+1
    end
end

def nextPlayer(p, total)
  (p+1)%total + 1
end

#o υπολογιστής παίρνει τυχαία σειρά και 
#διαλέγει νούμερο.
computer = rand(2) + 1
secret = low[1] + rand(high[1]-low[1])

player = 1 + rand(2)
finished=[False, False, False]
winner=0
while not finished[1] or not finished[2]

    if not finished[player]
        tries[player]-=1

        if player==computer
            print("Ειναι η σειρά μου.")
            if tries[player]>0
                print("Εχω άλλες", tries[player], "προσπάθειες.")
            else:
                print("Είναι η τελευταία μου προσπάθεια!")

            a=random.randint(low[player],high[player])
            print("Διάλεξα το ",a)
            f=getFeedback()

            if f!=3:
                if winner != 0 or tries[player]==0:
                    print("Εχασα...")
                    finished[player] = True

                if f==1:
                    high[player]=a;
                else:
                    low[player]=a
            else:
                print("Ναι! Το βρήκα!")
                finished[player] = True
                if winner==0:
                    winner=player
        else
            print("Είναι η δική σου σειρά.")
            if tries[player]>0: 
                print("Εχεις άλλες", tries[player], "προσπάθειες.")
            else:
                print("Είναι η τελευταία σου προσπάθεια!")
            a=readNumber(low[player], high[player])
            if a != secret:
                if winner != 0 or tries[player]==0:
                    print("Εχασες!")
                    finished[player] = True
                dif = showMessage(a, secret, low[player], high[player])
                if dif<0:
                    high[player]=high[player]+dif
                else:
                    low[player]=low[player]+dif
            else
                print ("Μπράβο! Το βρήκες!")
                finished[player] = True
                if winner==0:
                    winner=player

    player = nextPlayer(player,2)


print ("Τέλος παιχνιδιού!")
