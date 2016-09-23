def flip()
    rand 2
end

while true
    puts("δώσε 0 για κορώνα, 1 για γράμματα ")
    x=gets.chomp.to_i

    if x==flip
        print("Κέρδισες")
    else
        if x!=0 and x!=1
            break
        end
        print("Εχασες")
    end
end
