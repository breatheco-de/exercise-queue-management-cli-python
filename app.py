#validating python version
import sys
if sys.version_info[0] < 3:
    raise Exception("You must use Python 3, try running $ python3 app.py or updating the python interpreter")

#there exercise code starts here
from DataStructures import Queue

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")

def show_main_menu():
    print('''
        What would you like to do (type a number and the enter key)?
            - Type 1: For adding someone to the Queue.
            - Type 2: For removing someone from the Queue.
            - Type 3: For printing the current Queue state.
            - Type 4: To export the queue to a JSON file.
            - Type 5: To quit
    ''')
    response = input()
    return response
    
def print_queue():
    # you must print on the console the entire queue list
    pass
    
def start():
    
    print("Hello, this is the Command Line Interface for a Queue Managment application.");
    while True:
        
        option = show_main_menu()
        
        try: #converting the user input into an integer
            option = int(option)
        except ValueError:
            print("Invalid option "+str(option))
        
        # now, lets intepret the option
        if option > 5:
            print("Invalid option "+str(option))
        elif option == 5:
            print("Bye bye!")
            return None

    
start()