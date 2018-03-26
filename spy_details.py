####### Information Of A Default User #######


# default status
current_status_message = None

# list of default status
STATUS_MESSAGES = ['My name is Vivek.', 'Location: New Delhi']


class User:
    # create class
    def __init__(self, uname, age, rating):
        self.uname = uname
        self.age = age
        self.rating = rating


# define user_name, age, rating
user_1 = User('Mr. Vivek', 20, 3.8)
user_2 = User('Mr. Ujjwal', 21, 2.6)
