import random

#n=random.randint(0,100)
#print n
n=raw_input("enter any no")
n=int(n)

if n == 0:
    print("Enter any other value greater than 0..Pss 0 is EVEN")
elif n % 2 == 0:
    if 2 <= n <= 5 or n > 20:
        print ("Between 2 & 5 or greater than 20 | EVEN | Not weird")
    elif 6 <= n <= 20:
        print ("Between 6 & 20 | EVEN |  Weird")

else:
    print ("Oddly weird")

