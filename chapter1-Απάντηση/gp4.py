
name = input("Πώς σε λένε;")

import time
hour = time.localtime().tm_hour

if hour<14:
    print("Καλημέρα", name)
else:
    print("Καλησπέρα", name)


