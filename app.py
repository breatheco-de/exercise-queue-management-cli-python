from DataStructures import Queue

def show_main_menu():
    print('''
        What would you like to do?
            - Type 1: For adding someone to the Queue.
            - Type 2: For removing someone from the Queue.
            - Type 3: For printing the current Queue state.
            - Type 4: To export the queue to a JSON file.
            - Type 5: To quit
    ''');
    response = input()
    return response
    
def print_queue():
    
    return response
    
def start():
    queue = Queue(mode="FIFO")
    
    print("Hello, this is the Command Line Interface for a Queue Managment application.");
    while True:
        
        option = show_main_menu()
        
        try: #converting the user input into an integer
            option = int(option)
        except ValueError:
            print("❌ Invalid option "+str(option))
        
        # now, lets intepret the option
        if option > 5:
            print("❌ Invalid option "+str(option))
        elif option == 5:
            print("Bye bye!")
            return None

    
start()