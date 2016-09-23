def rollDice
    puts("Πάτα έντερ για να πέσουν τα ζάρια")
    gets

    dice1 = rand(6)
    dice2 = rand(6)

    roll = dice1 + dice2
    puts( "Εριξες", dice1, dice2, "=", roll)

    return roll
end

roll = rollDice

if roll==7 or roll==11
    puts("Κέρδισες με την πρώτη!")
elsif roll<=3 or roll==12
    puts("..έχασες με την πρώτη")
else
    while true do
        puts("Ξαναρίξε! Πρέπει να φέρεις", roll)
        newroll = rollDice()
        if newroll==roll
            puts("Κέρδισες!")
            break
        elsif newroll==7
            puts("Εχασες")
            break
        end
    end
end


