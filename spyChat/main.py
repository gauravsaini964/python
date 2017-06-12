spy_name=raw_input("What's your name?: ")
string_length=len(spy_name)

if(string_length<=0):
    print("name cant be blank")
    exit()
else:
    print()


gender = raw_input("Mister or Mistress")
phone_no = raw_input("What's your encrypted Phone No?")


#Check Salutation
if(gender=="mister"):
    salutation="Mr."
elif(gender=="Mr"):
    salutation="Mr."
elif(gender=="mis"):
    salutation="Mrs"
elif(gender=="mrs"):
    salutation="Mrs."

#Process Age eligibilty

spy_age = raw_input("enter your age")
if spy_age is " ":
    print("Please enter valid age")
    exit()
elif 1 > 0:
    spy_age = int(spy_age)
    if spy_age <=12 and spy_age >= 50:
        print("you are not eligible")
        exit()
else:
    print("You are eligible"
          "Please Continue")


print 'Welcome' +spy_name +'Glad you are here with us'
print "Mobile No: " +phone_no
print "Hi " +salutation +spy_name