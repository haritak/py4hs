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

tries = 4
number=readNumber(low, high)
#number=midNumber(low, high)
while number!=secret and tries>=0
    if number>secret
        puts "Λάθος, είναι μικρότερος"
        high = number-1
        puts "Απομένουν #{tries} προσπάθειες"
        tries-=1
    elsif number<secret
        puts("Λάθος, είναι μεγαλύτερος")
        low=number+1
        puts "Απομένουν #{tries} προσπάθειες"
        tries-=1
    end
    number=readNumber(low, high)
    #number=midNumber(low, high)
end
if number!=secret
  puts("Ηταν ο", secret)
else
  puts("Σωστά!")
  #άμεση έξοδος απο την επανάληψη
end
