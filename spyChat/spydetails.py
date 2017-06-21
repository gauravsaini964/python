import datetime
class Spy:

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None


class ChatMessages:

    def __init__(self,message,was_sent_by_me):
        self.message = message
        self.time = datetime.datetime.now()
        self.was_sent_by_me = was_sent_by_me

spy = Spy("Batman",'Mr.',24,5)

frnd1 = Spy('Jason Bourne', 'Mr.', 27, 4.9)
frnd2 = Spy('James Bond', 'Mr.', 21, 4.39)
frnd3 = Spy('Liam Neeson', 'Mr.', 37, 4.95)

friends = [frnd1,frnd2,frnd3]

