year=raw_input("Enter year")
year=int(year)


if year % 100 == 00:
    if year % 400 == 00:
            print ("Leap year")
    else:
            print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")

else:
    print("Not a leap year")