import requests
import json
from termcolor import colored
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

BASE_URL = 'https://api.instagram.com/v1/'
ACCESS_TOKEN = 'fill it'

CURRENT_ID = []
CURRENT_MEDIA = []



def start_bot():
    show_menu = True
    while show_menu:
        menu_choices =  menu_choices = "What do you want to do? " \
                                       "\n 1. Read account details" \
                                       "\n 2. Get recent media " \
                                       "\n 3. Like it or not " \
                                       "\n 4. Comment service " \
                                       "\n 5. Read Chats from a user " \
                                       "\n 6. Close Application \n"
        menu_choice = raw_input(menu_choices)
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            print colored("Read details\n", 'cyan', attrs=['bold'])
            get_info()
        elif menu_choice == 2:
            print colored("Get recent media\n", 'cyan', attrs=['bold'])
            get_recent()
        elif menu_choice == 3:
            print colored("Like it or not\n", 'cyan', attrs=['bold'])
            like_it_or_not()
        elif menu_choice == 4:
            print colored("Post or delete a comment\n", 'cyan', attrs=['bold'])
            post_del_comment()
        elif menu_choice == 5:
            print colored("Read existing message\n", 'cyan', attrs=['bold'])
            read_existing_chat()
        elif menu_choice == 6:
            show_menu = False



def get_info():
    select = int(raw_input("Select user for which you want info \n"
                           "1. Info of Access Token Owner\n"
                           "2. Info of other user"))
    if select ==1:
        print colored("Read own details\n", 'cyan', attrs=['bold'])
        request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
        user_info = requests.get(request_url).json()
        if user_info:
            with open('user_info.json', 'w') as outfile:
                json.dump(user_info, outfile)
                f1 = open('user_info.json')

            user_info = json.load(f1)
            for item in user_info:
                if item == 'data':
                    user_id = user_info['data']['id']
                    user_name = user_info['data']['username']
                    user = [user_id , user_name]
                    CURRENT_ID.append(user)



    elif select == 2:
        print colored("Get details of user using username\n", 'cyan', attrs=['bold'])
        id = get_userID()
        request_url = (BASE_URL + 'users/%s/?access_token=%s') % (id, ACCESS_TOKEN)
        user_info = requests.get(request_url).json()

    else:
        print 'Please select a valid option.'

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username:' +colored('%s', 'yellow', attrs=['bold']) %(user_info['data']['username'])
            print 'Followers:' + colored('%s', 'yellow', attrs=['bold']) % (user_info['data']['counts']['followed_by'])
            print 'Following:' + colored('%s', 'yellow', attrs=['bold']) % (user_info['data']['counts']['follows'])
            print 'Posts:' + colored('%s', 'yellow', attrs=['bold']) % (user_info['data']['counts']['media'])

        else:
            print colored('User has no data','red',attrs=['bold'])
    else:
        print colored('Data not found', 'red', attrs=['bold'])

#    quest = raw_input('Do you want to continue with this user? Y/N')
#    if quest.upper() == 'Y':
#        select = int(raw_input("Select no. corresponding to action you want to perform \n"
#                               "1. Like a post\n"
#                               "2. Comment on a post\n"))



def get_userID():
    username = raw_input("Enter instagram username of person you want to search")
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') %(username,ACCESS_TOKEN)
    user_info = requests.get(request_url).json()
    if user_info:
        with open('user_info.json', 'w') as outfile:
            json.dump(user_info, outfile)
            f1 = open('user_info.json')

        user_info = json.load(f1)
        for item in user_info:
            if item == 'data':
                user_id = user_info['data'][0]['id']
                user_name = user_info['data'][0]['username']
                user = [user_id , user_name]
                CURRENT_ID.append(user)
                return user_id
        else:
            print colored('Add user to sandbox','red',attrs=['bold'])


def get_recent():
    if CURRENT_ID == []:
        print "Select user first"
        get_info()
    id = CURRENT_ID[0][0]

    request_url = (BASE_URL + "users/%s/media/recent?access_token=%s") %(id,ACCESS_TOKEN)
    media = requests.get(request_url).json()
    if media:
        with open('recent_media.json', 'w') as outfile2:
            json.dump(media, outfile2)
            f1 = open('recent_media.json')
        media = json.load(f1)
        for item in range (0,1):
            media_ID = media['data'][item]['id']
            media_link = media ['data'][item]['link']
            media_type = media ['data'][item]['type']
            media_likes = media ['data'][item]['likes']['count']
            media_user_like = media['data'][item]['user_has_liked']
            media_info = [media_ID , media_link , media_type , media_likes , media_user_like]

            CURRENT_MEDIA.append(media_info)
            id = CURRENT_MEDIA [0][0]

    return id

def like_it_or_not():

    if CURRENT_ID == []:
        print "Select user first"
        media_id = get_recent()
        print media_id

    quest = int(raw_input('Select what do you want to do:\n'
                          '1. Get no of likes on recent post.\n'
                          '2. Like a post.\n'
                          '3. Delete like from a post\n'))
    if quest == 1:
        print "Post by: %s has: %s likes" %(CURRENT_ID[0][1],CURRENT_MEDIA[0][3])
    if quest == 2:
        request_url = (BASE_URL + 'media/%s/likes') % (media_id)
        payload = {"access_token": ACCESS_TOKEN}
        post_a_like = requests.post(request_url, payload).json()
        if post_a_like['meta']['code'] == 200:
            print colored('Successfully liked media','yellow',attrs=['bold'])
    if quest ==3:
        request_url = (BASE_URL + 'media/%s/likes') % (media_id)
        payload = {"access_token": ACCESS_TOKEN}
        delete_a_like = requests.delete(request_url)
        #if delete_a_like['meta']['code'] == 200:
            #print colored('Successfully deleted like on media', 'yellow', attrs=['bold'])

def post_del_comment():
    if CURRENT_ID == []:
        print "Select user first"
        media_id = get_recent()

    quest = int(raw_input('Select what do you want to do:\n'
                          '1. Comment on recent media.\n'
                          '2. Delete a negative comment.\n'))

    if quest == 1:
        comment = raw_input("Enter 'comment' you want to post")
        payload = {"access_token": ACCESS_TOKEN , 'text': comment}
        request_url = (BASE_URL + 'media/%s/comments') % (media_id)
        print media_id
        post_comment = requests.post(request_url,payload).json()
        if post_comment['meta']['code'] == 200:
            print colored('Successfully commented on media', 'yellow', attrs=['bold'])
        else:
            print colored('Unable to comment: Try again', 'red', attrs=['bold'])

    if quest == 2:
        print media_id
        print 'looped'
        request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id,ACCESS_TOKEN)
        get_comment = requests.get(request_url).json()
        print get_comment
        if get_comment['meta']['code'] == 200:
            if get_comment['meta']['code'] == 200:
                if len(get_comment['data']):
                    for x in range(0, len(get_comment['data'])):

                        comment_id = get_comment['data'][x]['id']
                        comment_text = get_comment['data'][x]['text']
                        print comment_id
                        blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                        if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                            print 'Negative comment : %s' % (comment_text)
                            delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id,
                                                                                                 ACCESS_TOKEN)
                            delete_info = requests.delete(delete_url).json()

                            if delete_info['meta']['code'] == 200:
                                print 'Negative comment successfully deleted'
                            else:
                                print 'Unable to delete comment'
                        else:
                            print 'No negative comment'
                else:
                    print 'There are no existing comments on the post'
            else:
                print 'Status code other than 200 recieved'


start_bot()