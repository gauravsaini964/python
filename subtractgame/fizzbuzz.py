number = raw_input("Enter a number : ")
number = int(number)
flag = 0
if number % 3 == 0 and number % 5 == 0:
     print "fizzbuzz"
elif number % 3 == 0:
    print "fizz"
elif number % 5 == 0:
    print "buzz"
else:
    print int(number)
