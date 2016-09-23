require 'time'
puts "Πότε γεννήθηκες"

a=gets.chomp.to_i
y=Time.new.year


a=y-a
puts a

if a<15
    print("You ain't allowed to use this machine")
else
    print("Ok")
end
    

