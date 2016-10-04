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

def showMessage(number, secret, low, high)
    if number>secret
        puts "Λάθος, είναι μικρότερος"
        return number-1
    elsif number<secret
        puts("Λάθος, είναι μεγαλύτερος")
        return number+1
    end
end


low=1
high=32

secret = rand high + low 
#ΓΙΑ ΕΛΕΓΧΟ : εμφάνιση μυστικού αριθμού
puts(secret)

tries = 4
number=readNumber(low, high)
#number=midNumber(low, high)
while number!=secret and tries>1
  tries-=1
  if number>secret
    high = showMessage(number, secret, low, high)
  elsif number<secret
    low=showMessage(number, secret, low, high)
  end
  puts "Απομένουν #{tries} προσπάθειες"
  number=readNumber(low, high)
  #number=midNumber(low, high)
end

if number!=secret
  puts "Τελευταία προσπάθεια!"
  number=readNumber(low, high)
end

if number!=secret
  puts("Ηταν ο", secret)
else
  puts("Σωστά!")
  #άμεση έξοδος απο την επανάληψη
end
