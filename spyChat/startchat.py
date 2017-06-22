from steganography.steganography import Steganography
from datetime import datetime
from spydetails import Spy, ChatMessages ,friends
from termcolor import colored


STATUS_DEFAULTS = ["Hey there", "Fuck you Donald Trump", 69]


def start_chat (spy):
    print colored("Authentication complete ! Welcome %s of age %d. You have spy rating of %.2f",
                  'yellow', attrs = ['bold']) % (spy.name, spy.age, spy.rating)
    status_rn = None
    show_menu = True
    while show_menu:
        menu_choices =  menu_choices = "What do you want to do? " \
                                       "\n 1. Add a status update " \
                                       "\n 2. Add a friend " \
                                       "\n 3. Send a secret message " \
                                       "\n 4. Read a secret message " \
                                       "\n 5. Read Chats from a user " \
                                       "\n 6. Close Application \n"
        menu_choice = raw_input(menu_choices)
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            print colored("Update Status\n", 'cyan', attrs=['bold'])
            status_rn = update_status(status_rn)
        elif menu_choice == 2:
            print colored("Add friends\n", 'cyan', attrs=['bold'])
            add_friend()
        elif menu_choice == 3:
            print colored("Send a secret message\n", 'cyan', attrs=['bold'])
            send_message()
        elif menu_choice == 4:
            print colored("Read a secret message\n", 'cyan', attrs=['bold'])
            read_message()
        elif menu_choice == 5:
            print colored("Read existing message\n", 'cyan', attrs=['bold'])
            read_existing_chat()
        elif menu_choice == 6:
            show_menu = False


def update_status ( status_rn ):
    updated_status_msg = None
    if status_rn != None:
        print "Your current status message is: " +colored(status_rn , 'yellow', attrs = ['bold'])
    else:
        print 'You don\'t have any status message currently'

    default = raw_input("Do you want to select status from defaults? Y/N")
    if default.upper() == "N":
        new_status_msg = raw_input("Enter your status\n")
        if len(new_status_msg) > 0:
            updated_status_msg = new_status_msg
            STATUS_DEFAULTS.append(new_status_msg)

    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_DEFAULTS:
            print "%d.%s" %(item_position,message)
            item_position = item_position+1

        select_status = int(raw_input("\nSelect number corresponding to the status you want to use\n"))
        if len(STATUS_DEFAULTS) > select_status:
                updated_status_msg = STATUS_DEFAULTS[select_status - 1]

    else:
        print 'Please enter Y or N !'


    return(updated_status_msg)

def add_friend():
    new_friend = Spy('','',0,0.0)
    new_friend.name = raw_input("Enter friends name")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)
    new_friend.chats = []

    if len(new_friend.name) > 0 and new_friend.age > 12:
        friends.append(new_friend)
        print colored('\nFriends Added', 'yellow', attrs = ['bold'])
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

def select_friend():
    item_number = 0

    for avail_friend in friends:
        print colored('%d. %s of %d age has %.2f rating', 'yellow', attrs=['bold']) %(item_number+1,avail_friend.name
                                                                                      ,avail_friend.age,
                                                                                      avail_friend.rating)
        item_number = item_number+1

    friend_choice = int(raw_input('\nSelect number corresponding to friend you want to select'))
    friend_choice_position = friend_choice -1

    return (friend_choice_position)

def send_message():
    friend_chosen = select_friend()

    original_image = raw_input('What is name of the image?')
    output_path = 'output.jpg'
    message_push = raw_input('Enter message you want to encode')
    Steganography.encode(original_image,output_path,message_push)

    new_chat = ChatMessages(message_push,True)

    friends[friend_chosen].chats.append(new_chat)
    print colored("\nChat message saved!\n", 'yellow', attrs = ['bold'])



def read_message():
    sender = select_friend()
    output_path = raw_input('What is name of the file?')
    message_pull = Steganography.decode(output_path)
    if message_pull == "":
        print "Agent must be in hurry,he left no message! What might be the case?"
    else:
        new_chat = ChatMessages(message_pull, False)
        friends[sender].chats.append(new_chat)
        print "\nYour secret message has been saved\n"

    read_msg = raw_input("Do you want to display secret message? Y/N")
    if read_msg.upper() == 'Y':
        print colored("Your secret message is:%s", 'yellow', attrs=['bold']) %message_pull


def read_existing_chat():
    read_for = select_friend()
    print '\n6'
    for chat in friends[read_for].chats:
        if chat.was_sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)
