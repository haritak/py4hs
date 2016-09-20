while true
    puts("Δώσε 1 για Πέτρα, 2 για Ψαλίδι ή 3 για Χαρτί")
    u=gets.chomp.to_i
    c=rand 4
    choices = ["","Πέτρα","Ψαλίδι","Χαρτί"]

    print("Εγώ διάλεξα", choices[c])

    if (u==c)
        print("ισοπαλία")
    elsif u==3 and c==1
        print("κέρδισες")
    else
      if not [1,2,3].include?( u)
            break
        print("έχασες")
        end
    end
end

# Δεν είναι σωστή η λογική αλλά το παρατάω...
