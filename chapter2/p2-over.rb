puts"Πάτα έντερ για να πέσουν τα ζάρια"
gets

dice1 = rand 6
dice2 = rand 6

roll = dice1 + dice2
puts( "Εριξες", dice1, dice2, "=", roll)

if roll==7 or roll==11
    print("Κέρδισες με την πρώτη!")
elsif roll<=3 or roll==12
    print("..έχασες με την πρώτη")
else
    over=false
    while not over
      puts("Ξαναρίξε! Πρέπει να φέρεις", roll)
      puts ("Πάτα έντερ για να πέσουν τα ζάρια")
      gets

      dice1 = rand 6
      dice2 = rand 6

      newroll = dice1 + dice2
      puts( "Εριξες", dice1, dice2, "=", roll)
      if newroll==roll
        print("Κέρδισες!")
        over = true
      elsif newroll==7
        print("Εχασες")
        over = true
      end
    end
end


