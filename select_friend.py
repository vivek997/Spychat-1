from spy_details import friends


# select friend from friend list.
def select_a_friend():
    item_position = 1
    # showing the all friends from friends
    for friend in friends:
        print("%d. %s age: %s with ratting %s is online" % (item_position, friend.name, friend.age, friend.rating))
        #all friend list is generate
        item_position = item_position + 1
    friend_choice = int(raw_input("choose your friend"))
    friend_choice_position = friend_choice - 1
    return friend_choice_position
