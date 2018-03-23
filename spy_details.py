####### Information Of A Default User #######

print("For default user")


class User:
# create class
    def __init__(self, name, age, rating):
        self.name = name
        self.age = age
        self.rating = rating

# define name, age and rating


user_1 = User('Mr. Vivek', 20, 3.8)
user_2 = User('Mr. Ujjwal', 21, 2.6)


name = input("Select your default user name: Vivek or Ujjwal")
if name == "Vivek" or name == "vivek":
    print("Welcome "+user_1.name+" your age is "+str(user_1.age)+" and rating is "+str(user_1.rating)+"!")
    print("Proud to have you on board!")
elif name == "Ujjwal" or name == "ujjwal":
    print("Welcome "+user_2.name+" your age is "+str(user_2.age)+" and rating is "+str(user_2.rating)+"!")
    print("Proud to have you on board!")
else:
    print("Please provide valid name.")

