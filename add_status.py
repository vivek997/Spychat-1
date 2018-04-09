from spy_details import current_status_message
from spy_details import status


def status_message(current_status_message):
    #current status message
    if current_status_message != None:
        print('Your current status message is %s \n' % current_status_message)
    else:
        print('You don\'t have any status message currently \n')
        question = raw_input("do you want to select status from old status? y/n")
        # if user want to add new status
        if question.upper() == "N":
            new_status_message = raw_input("What status message do you want to set?: ")

            # validating users input.
            if len(new_status_message) > 0:
                # adding new status
                status.append(new_status_message)
                # updated status
                updated_status_message = new_status_message
                print('Your updated status message is: %s' % updated_status_message)
            else:
                print("You did not provided any status message. Try again.")

        # user wants to select from older status.
        elif question.upper() == 'Y':

            # counter
            item_position = 1

            # printing all older status
            for message in status:
                print('%d. %s' % (item_position, message))
                item_position = item_position + 1

            # select the index of the status
            message_selection = int(raw_input("\nChoose from the Index of status: "))

            # validating user input and set status.
            if len(status) >= message_selection:

                updated_status_message = status[message_selection - 1]
                print('Your updated status message is: %s' % updated_status_message)
            # when user has wrong choice
            else:
                print("Invalid choice. Try again.")
        # when user has diffrent choice
        else:
            print('The option you choose is not valid! Press either y or n.')
        # updated message
        return updated_status_message
