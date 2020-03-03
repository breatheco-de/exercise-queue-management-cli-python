import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add():
    phone = input("Enter a phone number:")
    queue.enqueue(phone)
    print("Adding")

def dequeue():
    phone = queue.dequeue()
    send(body='It is your turn on the queue', to=phone)
    print("Removing and sending sms to "+phone)

def save():
    _queue = queue.get_queue()
    file = open('queue.json', 'w+') # open the file for writing 'w', create if it doesn't exists
    file.write(json.dumps(_queue)) # write the content
    file.close() # close the file

def load():
    global queue
    file = open("queue.json", "r") 
    imported_queue = json.load(file)
    file.close()
    queue = Queue(mode="FIFO", current_queue=imported_queue)
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 1:
        add()
    elif option == 2:
        dequeue()
    elif option == 3:
        print_queue()
    elif option == 4:
        save()
    elif option == 5:
        load()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Invalid option "+str(option))
