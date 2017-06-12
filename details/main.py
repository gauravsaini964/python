print("Welcome to acadview")
print("Please enter basic details to complete registration")

fname = raw_input("Enter your first name")
lname = raw_input("Enter your last name")
gender = raw_input("Enter gender")
phone_no = raw_input("Enter phone no")
email = raw_input("Enter your Email Address")
fee = raw_input("enter fee paid")
fee = int(fee)

if(gender=="male"):
    salutation="Mr."
elif(gender=="Male"):
    salutation="Mr."
elif(gender=="female"):
    salutation="Mrs"
elif(gender=="Female"):
    salutation="Mrs."


print "To : " +email
print "Mobile No: " +phone_no
print "Hi " +salutation +fname + " " + lname

if (fee==2499):
    print "Welcome to AcadView. We have recieved your payment successfully of Rs.2499"
elif (fee<2499):
    fee=2499-fee
    print "Welcome to AcadView, You have remaining balance :" ,fee ,"Please pay at earliest."
