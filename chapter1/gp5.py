import time

name = input("Πώς σε λένες; ")

hour = time.localtime().tm_hour

if hour<14:
    print("Καλημέρα", name)
else:
    print("Καλησπέρα", name)
    
wait = 3
time.sleep(wait)

answer=42
print("Η απάντηση είναι ...", answer)

