def midNumber(a,b)
    puts "Μάντεψε τον αριθμό #{a}-#{b}"
    num = (a+b)/2
    puts "Ο υπολογιστής επιλέγει: #{num}"
    return num
end

def readNumber(a,b)
    puts "Μάντεψε τον αριθμό #{a}-#{b}"
    num=gets.to_i
    num=gets.to_i until num>=a and num<=b
    return num
end


low=1
high=32

secret = rand high + low 
#ΓΙΑ ΕΛΕΓΧΟ : εμφάνιση μυστικού αριθμού
puts(secret)

found = false
tries = 4
while not found and tries>=0
    number=readNumber(low, high)
    #number=midNumber(low, high)
    if number>secret
        puts "Λάθος, είναι μικρότερος"
        high = number-1
        puts "Απομένουν #{tries} προσπάθειες"
        tries-=1
    elsif number<secret
        print("Λάθος, είναι μεγαλύτερος")
        low=number+1
        puts "Απομένουν #{tries} προσπάθειες"
        tries-=1
    else
        puts("Σωστά!")
        #άμεση έξοδος απο την επανάληψη
        found = true
    end
end
if not found
    puts("Ηταν ο", secret)
end
