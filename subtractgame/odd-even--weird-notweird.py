import random

#n=random.randint(0,100)
#print n
n=raw_input("enter any no")
n=int(n)

if n%2 != 0:
    print ("Oddly Weird")
elif n == 0:
    print("Enter any other value greater than 0")
elif n>20 and n%2 ==0:
    print ("Greater than 20 vala even Not weird")
elif n>=6<=20 and n%2 == 0:
    print ("6 se 20 ke beech wala even Weird")
elif n>=2<6 and n%2 == 0:
    print ("or 6 se neeche vala even Not weird")

