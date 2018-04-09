from steganography.steganography import Steganography
from select_friend import select_a_friend
from spy_details import friends, ChatMessage,spy_1,Spy
from datetime import datetime
import csv


def read_message():
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")
    #decode secret text.
    secret_text = Steganography.decode(output_path)
    print(secret_text)

    # add the chat to sender
    chat = ChatMessage(spy_name=spy_1.name, friend_name=sender, time=datetime.now().strftime("%d %B %Y"),
                       message=secret_text)
    friends[sender].chats.append(chat)
    print("Your secret message has been saved.")
    # writing chats in chats.csv
    with open("chats.csv", 'a') as chat_record:
        writer = csv.writer(chat_record)
        writer.writerow([chat.spy_name, chat.friend_name, chat.time, chat.message])
