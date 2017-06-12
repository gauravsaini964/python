import random

number = random.randint(5,24)
print number


if ((number-3) % 4 == 0 or (number-2) % 4 ==0 or (number-3) % 4 ==0):
    print("Shubham wins")
else:
    print("Prince wins")

