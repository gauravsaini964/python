import requests
from termcolor import colored

BASE_URL = 'https://api.instagram.com/v1/'
ACCESS_TOKEN = '229742593.0635911.5037291b10384da59a7f622e4a0e68ed'



def start_bot():
    show_menu = True
    while show_menu:
        menu_choices =  menu_choices = "What do you want to do? " \
                                       "\n 1. Read your own details" \
                                       "\n 2. Get details of an user" \
                                       "\n 3. Send a secret message " \
                                       "\n 4. Read a secret message " \
                                       "\n 5. Read Chats from a user " \
                                       "\n 6. Close Application \n"
        menu_choice = raw_input(menu_choices)
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            print colored("Read own details\n", 'cyan', attrs=['bold'])
            self_info()
        elif menu_choice == 2:
            print colored("Get details of user using username\n", 'cyan', attrs=['bold'])
            get_userID()
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



def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET Access Token Owner Info : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username:' +colored('%s', 'yellow', attrs=['bold']) %(user_info['data']['username'])
            print 'Followers:' + colored('%s', 'yellow', attrs=['bold']) % (user_info['data']['counts']['followed_by'])
            print 'Following:' + colored('%s', 'yellow', attrs=['bold']) % (user_info['data']['counts']['follows'])
            print 'Posts:' + colored('%s', 'yellow', attrs=['bold']) % (user_info['data']['counts']['media'])
        else:
            print colored('User has no data','red',attrs=['bold'])
    else:
        print colored('Server 200 ni maar rha', 'red', attrs=['bold'])


def get_userID():
    request_url = (BASE_URL + 'users/search?q=jack&access_token=%s') %(ACCESS_TOKEN)
    user_info = requests.get(request_url).json()
    print user_info
# Waiting for sandbox invite



start_bot()