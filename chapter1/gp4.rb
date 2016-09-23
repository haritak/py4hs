puts "ονομα;"

name = gets

require 'time'

hour = Time.new.hour

if hour<14
    print("Καλημέρα ", name)
else
    print("Καλησπέρα ", name)
end


