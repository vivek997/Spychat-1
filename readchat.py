from spy_details import friends, ChatMessage, spy_1
import csv
from termcolor import colored


def readchat(choice):
    name_friend = friends[choice].name
    with open('Chats.csv', 'rU') as chats_data:
        reader = csv.reader(chats_data)
        for row in reader:
            try:
                c = ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3])
                #the chats of the current spy with selected friend
                if c.spy_name == spy_1.name and c.friend_name == name_friend:
                    print colored("You sent message to the Spy name: %s " % name_friend, "red")
                    print colored("On Time: [%s]" % c.time, "blue")
                    print("Message: %s" % c.message)
                    return 1
            except IndexError:
                pass
            continue
