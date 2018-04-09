####### Information Of A Default User #######
from datetime import datetime


#default status
current_status_message = None
#status messages
status = ['My name is Vivek Rawal.', 'I love Computer Science', 'Location: New Delhi', 'College: MRIU']
#Emergency words
special_words = ['SAVE ME', 'SOS' , 'HELP']


# creating Spy class
class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name= name
        self.salutation = salutation
        self.age= age
        self.rating= rating
        self.is_online=True
        self.chats=[]
        self.current_status_message= None


# chats
class ChatMessage:
        def __init__(self, spy_name, friend_name, time, message):
            self.spy_name = spy_name
            self.friend_name = friend_name
            self.time = time
            self.message = message


# define spy_name,salutation, age, rating)
spy_1=Spy('Vivek Rawal','Mr',20,4.5)

# lists of friends
friends=[]
# list of chats
chats = []