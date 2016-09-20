puts "Ποιά είναι η απάντηση;"
a = gets.chomp

if a=="42"
    puts("πολύ σωστά...")
else
  puts("θέλεις διάβασμα")
  puts("άντε άλλη μία προσπάθεια:")
  puts "Ποιά είναι η απάντηση;"
  a = gets.chomp

  if a=="42"
    print("πολύ σωστά...")
  else
    print("θέλεις διάβασμα")
  end
end



