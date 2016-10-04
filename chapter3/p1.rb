s = rand 31  + 1
puts s
found = false
tries = 4
while not found and tries>=0
  puts "Μάντεψε τον αριθμό 1-32"
  n = gets.to_i
  if n!=s then
    puts "Λάθος"
    puts "Απομένουν #{tries} προσπάθειες"
    tries-=1
  else
    puts "Σωστά!"
    found=true
  end
end

if not found 
  puts "Ηταν ο #{s}"
end

