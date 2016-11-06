def reverse(n):
    s=''
    for c in n:
        s = c+s
    return s

print(reverse('Chess'))
