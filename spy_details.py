####### Information Of A Default User #######


# default status
current_status_message = None

# list of default status
status = ['My name is Vivek.', 'Location: New Delhi']


class User:
    # create class
    def __init__(self, uname, salutation, age, rating):
        self.uname = uname
        self.salutation = salutation
        self.age = age
        self.rating = rating


# define user_name, age, rating
user_1 = User('Vivek', 'Mr.', 20, 4.8)


# details of some existing friends
friend_one = User('Ujjwal', 'Mr.', 21, 4.1)
friend_two = User('Princi', 'Ms.', 20, 3.9)
friend_three = User('Shivam', 'Mr.', 21, 3.7)

# lists of friends
friends = [friend_one, friend_two, friend_three]
