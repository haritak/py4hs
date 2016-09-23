while true
    card1 = rand 12
    card2 = card1 + rand(2)+1
    d = card2-card1
    mult = 12/d

    puts("Πόσο στοιχηματίζεις; ")
    bet = gets.chomp.to_i
    puts("Τί επιλέγεις; ")
    c = gets.chomp.to_i
    price = bet*mult
    if c>card1 and c<card2
        puts("Κέρδισες ", price)
    else
        puts("Εχασες. Οι αριθμοί ήταν ", card1, card2,
                "και θα κέρδιζες ", price)
    end
end

