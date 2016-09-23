require 'time'

puts "name ?"

name = gets

hour = Time.new.hour

if hour<14
    print("Καλημέρα ", name)
else
    print("Καλησπέρα ", name)
end
    
wait = 3
sleep(wait)

answer=42
print("Η απάντηση είναι ...", answer)

