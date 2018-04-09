from steganography.steganography import Steganography
from select_friend import select_a_friend
from datetime import datetime
from spy_details import friends, ChatMessage, chats, spy_1
import csv
from spy_details import special_words
from termcolor import colored


def send_message():
    friend_choice = friends[select_a_friend()].name

    original_image = raw_input("What is the name of the image?")
    #output.jpg is a output image, with output name
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    if text in special_words:
        text = colored(text + ": IT'S EMMERGENCY!!", "red")
    # encoding the message
    Steganography.encode(original_image, output_path, text)

    # the message will be stored in chat
    new_chat = ChatMessage(spy_name=spy_1.name, friend_name=friend_choice, time=datetime.now().strftime("%d %B %Y"),
                           message=text)
     #append new_chat in chats list.
    chats.append(new_chat)
    print("your secret message is ready.")

    with open('chats.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([new_chat.spy_name, new_chat.friend_name, new_chat.time, new_chat.message])
