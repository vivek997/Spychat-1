from steganography.steganography import Steganography
from select_friend import select_a_friend
from spy_details import friends, ChatMessage,spy_1,Spy
from datetime import datetime
import csv
from termcolor import colored

def read_message():
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")
    #decode secret text.
    secret_text = Steganography.decode(output_path)
    print(secret_text)

    words = secret_text.split()
    for i in words:
        if i == "SOS" or i == "sos" or i == "save" or i == "help" or i == "Emergency" or i == "danger":
            # Maintain the average number of words spoken by a spy every time a message is received from a particular spy.
            #friends[sender].count += len(words)
            # Emergency alert

            # Help your friend by sending him a helping message
            print(colored(i + ": IT'S EMMERGENCY!!", "red"))
            print ("Don't panic !!")
            print ("I am coming to rescue.\n\n")

    # add the chat to sender
    chat = ChatMessage(spy_name=spy_1.name, friend_name=sender, time=datetime.now().strftime("%d %B %Y"),
                       message=secret_text)
    friends[sender].chats.append(chat)
    print("Your secret message has been saved.")
    # writing chats in chats.csv
    with open("chats.csv", 'a') as chat_record:
        writer = csv.writer(chat_record)
        writer.writerow([chat.spy_name, chat.friend_name, chat.time, chat.message])
