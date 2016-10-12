n = int( input() )

s = 0
fi_1=0
for fi in range(1, n+1, 1):
    s = s + fi+fi_1
    fi_1 = fi

print(s)
    
