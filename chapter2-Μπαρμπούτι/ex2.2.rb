puts("Δώσε τον αριθμό εκκίνησης ")
a=gets.chomp.to_i

step=1
m=a
while a!=1
    if a%2==1
        a=a*3+1
    else
        a=a/2
    end

    puts(a)
    if a>m
        m=a
    end
    step = step+1
end

puts("Πλήθος βημάτων", step)
puts("Μέγιστος αριθμός το ", m)
