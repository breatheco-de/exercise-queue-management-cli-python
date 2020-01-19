#validating python version
import sys
if sys.version_info[0] < 3:
    print("Error: You must use Python 3, try running $ python3 app.py or updating the python interpreter")

#there exercise code starts here
import json
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
    - Type 4: To export the queue to the queue.json file.
    - Type 5: To import the queue from the queue.json file.
    - Type 6: To quit
    ''')
    response = input()
    return response
    
def add_to_queue():
    print("Type the name you want to add into the list")
    name = input()
    queue.enqueue(name)
    print(name+" was added to the list")

def remove_from_queue():
    name = queue.dequeue()
    print("It is "+name+" turn, therefore he was removed from the list")

def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())


def export_queue():
    # you must print on the console the entire queue list
    file = open('queue.json', 'w+') # open the file for writing 'w', create if it doesn't exists
    file.write(json.dumps(queue.get_queue())) # write the content
    file.close() # close the file
    print("List exported successfully, open the queue.json file to review it.")

def import_queue():
    # you must print on the console the entire queue list
    print("Importing the entire list...")
    filePointer = open("queue.json", "r") 
    data = json.load(filePointer)
    
    global queue # <-- we have to tell python we are referring to the global variable queue
    queue = Queue(mode="FIFO", current_queue=data)
    print("List import successfully, print the list to review the updates.")
        
def start():
    
    print("Hello, this is the Command Line Interface for a Queue Managment application.");
    while True:
        
        option = show_main_menu()
        
        try: #converting the user input into an integer
            option = int(option)
        except ValueError:
            print("Invalid option "+str(option))

        # add your options here using conditionals (if)
        if option == 1:
            add_to_queue()
        elif option == 2:
            remove_from_queue()
        elif option == 3:
            print_queue()
        elif option == 4:
            export_queue()
        elif option == 5:
            import_queue()
        
        # now, lets intepret the option
        if option > 6:
            print("Invalid option "+str(option))
        elif option == 6:
            print("Bye bye!")
            return None

    
start()