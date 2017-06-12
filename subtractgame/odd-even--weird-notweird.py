import random

#n=random.randint(0,100)
#print n
n=raw_input("enter any no")
n=int(n)

if n == 0:
    print("Enter any other value greater than 0..Pss 0 is EVEN")
elif n%2 == 0:
    if n>20:
        print ("Greater than 20 | EVEN | Not weird")
    elif n>=6<=20:
        print ("Between 6 & 20 | EVEN |  Weird")
    elif n>=2<6 :
        print ("Between 2 & 5 | EVEN | Not weird")
else:
    print ("Oddly weird")

