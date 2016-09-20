puts("Δώσε μου ένα αριθμό")
a=gets.chomp.to_i
puts("Δώσε άλλο έναν αριθμό")
b=gets.chomp.to_i

while a!=b
    if a>b
        a=a-b
    else
        b=b-a
    end
end


puts("Ο μέγιστος κοινός διαιρέτης είναι το ", a)
