#validating python version
import sys
if sys.version_info[0] < 3:
    print("Error: You must use Python 3, try running $ python3 app.py or updating the python interpreter")

#their exercise code starts here
import json
from DataStructures import Queue

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")

def show_main_menu():
    print('''
What would you like to do (type a number and press Enter)?
    - Type 1: For adding someone to the Queue.
    - Type 2: For removing someone from the Queue.
    - Type 3: For printing the current Queue state.
    - Type 4: To export the queue to the queue.json file.
    - Type 5: To import the queue from the queue.json file.
    - Type 6: To quit
    ''')
    response = input()
    return response
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())
        
def start():
    
    print("\nHello, this is the Command Line Interface for a Queue Managment application.");
    while True:
        
        option = show_main_menu()
        
        try: #converting the user input into an integer
            option = int(option)
        except ValueError:
            print("Invalid option "+str(option))

        # add your options here using conditionals (if)
        if option == 3:
            print_queue()
        elif option == 6:
            print("Bye bye!")
            return None
        else:
            print("Invalid option "+str(option))

    
start()
