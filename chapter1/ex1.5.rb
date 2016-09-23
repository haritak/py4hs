puts "Δώσε δευτερόλεπτα"
a=gets.chomp.to_i

t=[]
3.times do
  t << a%60
  a = a/60
end

t.reverse.each do |i|
  print i,":"
end
puts

