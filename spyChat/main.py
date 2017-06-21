import startchat
from spydetails import spy

question = "Continue as guest Y/N"
existing = raw_input(question)

if existing.upper() == "Y":
    print "Welcome %s.%s of age:%d has rating of %.2f" %(spy['salutation'],spy['name'],
                                                         spy['age'],spy['rating'])
    if spy['is_online'] == True:
        print "you are online"
        startchat.start_chat(spy)
    else:
        print "You are currently offline"

else:
    spy = {'name' : '',
           'salutation' : '',
           'age' : 0,
           'rating' : 0.0,
           'is_online' : False}

    spy['name'] = raw_input("Enter your spy name")
    if len(spy['name']) > 0:
        print 'Welcome ' + spy['name'] + '. Glad to have you here.'
        spy['salutation'] = raw_input("Should I call you Mister or Miss?: ")
        spy['name'] = spy['salutation'] + " " + spy['name']

        print "Alright " + spy['name'] + ". I'd like to know a little bit more about you before we proceed..."

        spy['age'] = raw_input("What is your age?")
        spy['age'] = int(spy['age'])

        if spy['age'] > 12 and spy['age'] < 50:

            spy['rating'] = raw_input("What is your spy rating?")
            spy['rating'] = float(spy['rating'])

            if spy['rating'] > 4.5:
                print 'Great ace!'
            elif spy['rating'] > 3.5 and spy['rating'] <= 4.5:
                print 'You are one of the good ones.'
            elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'

            spy['is_online'] = True
            if spy['is_online']:
                startchat.start_chat(spy)

        else:
            print 'Sorry you are not of the correct age to be a spy'
    else:
        print "A spy needs to have a valid name. Try again please."
