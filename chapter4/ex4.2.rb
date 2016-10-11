def findNext(p)
    (p%2)+1
end

def maxMatches(m)
  m>3 ? 3 : m
end

def readMatches(p,m)
  limit=maxMatches(m)
  num=0
  if limit>1
    begin
      puts"Παίκτη #{p} πόσα σπίρτα (1 έως #{limit}) θέλεις να βγάλεις;"
      num=gets.chomp.to_i
    end while num<1 or num>limit
  else
        print("Παίκτη", p, "αναγκαστικά πρέπει να παρεις το τελευταίο σπίρτο.")
        num=1
  end

  return num
end

def randomMatches(m)
    return 1+ rand(maxMatches(m)-1)
end

def computeMatches(m)
    mod=(m-1)%4
    if mod==0
        return randomMatches(m)
    else
        return mod
    end
end


matches= 7 + rand(21-7)

computer=1 + rand(1)

puts ("Αρχικό πλήθος σπίρτων: #{matches}")

player=1

while matches>0
    if player==computer
        removed = computeMatches(matches)
        puts "Ο υπολογιστής πήρε #{removed} σπίρτα"
    else
        removed=readMatches(player,matches)
    end

    matches-=removed

    puts "Σπίρτα που απομένουν: #{matches}"
    player=findNext(player)
end

if player==computer
    puts "Κέρδισε ο υπολογιστής"
else
    puts "Παίκτη #{player} κέρδισες"
end
