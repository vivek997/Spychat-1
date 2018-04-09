from add_status import status_message
from send_message import send_message
from add_friend import add_friend
from read_message import read_message
from spy_details import friends, Spy, chats, ChatMessage
from select_friend import select_a_friend
import csv
from readchat import readchat
from termcolor import colored


#function start..
def start_chat(name, age, rating):
    current_status_messesge = None
    print("your current status is " + str(current_status_messesge))

    #it is a function to loads all the friends stored in friends.csv
    def load_friends():
        with open('friends.csv', 'rU') as friends_data:
            reader = csv.reader(friends_data)
            for row in reader:
                try:
                    friends.append(Spy(name=row[0], salutation=row[1], age=row[2], rating=row[3]))
                except IndexError:
                    pass
                continue

    # load_chats() is used for loads all the chats of spies stored in chats.csv
    def load_chats():
        with open("chats.csv", 'rU') as chat_data:
            reader = csv.reader(chat_data)
            for row in reader:
                try:
                    chats.append(ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3]))
                except IndexError:
                    pass
                continue

    #functions called, so the chats and list of friends are loaded before its usage
    load_friends()
    load_chats()

    continue_option = "Y"

    while (continue_option == 'Y' or continue_option == 'y'):

        menu_option = int(raw_input(
            "What would you like to do \n 1. Add a status update \n 2. Add a friend \n 3. Send a message \n 4. Read a secret message \n 5. Read chats from a user \n 6. Close the application"))

        # displaying menu for user.
        while (menu_option <= 6):
            if menu_option == 1:
                print("You choose update the status ")

                current_status_messesge = str(status_message(current_status_messesge))
                # calls the add_status_message from the add_status file
                print colored("Your selected status is:" + current_status_messesge,"red")
                # Displays the status chosen or entered by the spy
                break
            elif menu_option == 2:
                print("Adding a friend.")
                # add a new friend
                number_of_friends = add_friend()
                print('You have %d friends' % number_of_friends)  # prints the number of friends
                break
            elif menu_option == 3:
                print("Sending a  message.")
                send_message()
                break
            elif menu_option == 4:
                print("Read a secret message.")
                read_message()
                break
            elif menu_option == 5:
                print("Reading chat from user")
                print "select a friend whose chat you want to see"
                choice = select_a_friend()
                readchat(choice)
                break
            elif menu_option == 6:
                print("Exit.")
                exit()
        continue_option = raw_input("Would you like to perform another operation (Y/N)")
    print("Thank you")