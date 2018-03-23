print("THE SPY CHAT!")
# existing user or create a new user
default_user = input("Would you like to continue with the default user or create a new one (Default or Create) ?")
# for existing user
if default_user == "Default" or default_user == "default":
        import spy_details

# for a new user
elif default_user == "Create" or default_user == "create":
        # asking names
        spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")
        # checking length of the name
        if len(spy_name) > 0:
            # asking for salutation
            spy_salutation = input("What would you like us to call you (Mr. or Ms.) ?")

            print("Alright " + spy_salutation + " " + spy_name + " I'd like to know a little bit more about you...")
            # checking age
            spy_age = int(input("What's your age?"))
            if 12 < spy_age < 50:
                # checking rating
                spy_rating = float(input("What is your spy rating?"))
                if spy_rating > 4.5:
                    print("Outstanding!")
                elif 3.5 < spy_rating <= 4.5:
                    print("Amazing!")
                elif 2.5 <= spy_rating <= 3.5:
                    print("You can surely improve!")
                else:
                    print("Don't Worry! We'll help you!")
                # if spy is online
                spy_is_online = True
                # welcome with details
                print("Authentication complete.")
                print("Welcome "+spy_salutation+" "+spy_name+" your age is "+str(spy_age)+" and rating is "+str(spy_rating)+"!")
                print("Proud to have you on board!")
            # age is not eligible
            else:
                print("Sorry you are not of the correct age to be a spy")
        # name not provided
        else:
            print("Please provide us with your name first. Try again please.")
# entry not valid
else:
        print("Please enter default or create.")
