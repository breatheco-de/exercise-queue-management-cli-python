# ![alt text](https://assets.breatheco.de/apis/img/images.php?blob&random&cat=icon&tags=breathecode,32) Queue Management System CLI

Lets create a Queue System: Queue system are heavily used in Goverment institutions, airports, banks and many other venues looking to organize the incoming traffic.
Queue systems can also be used to load balancing for different applications like:
- Stablishing priorities in web servers incoming requests.
- Inmigration and visa applicantions that need to be prioritized.
- Network packages.
- etc.

A queue is just a list of elements that must be process an a particular order: FIFO and FILO.

Today we are going to build a Queue system with FIFO approach for restorants: If a new clients arrives to the restorant it gets added into a queue, when it is his time to eat, he gets notified by email.

## 📝 Instructions

1. Clone the [following boilerplate](https://github.com/breatheco-de/exercise-queue-management-cli)
2. Update the app.py file to allow the user to manage a simple Queue: Add a person, Remove person, get current line (queue).
3. The application also needs to be able to export the queue to a file named `queue.json`.
4. The application must integrate with the twilio API to send an SMS every time a phone number is dequeued.
4. Use the following data-structure to implement the queue:

```python
class Queue:

    def __init__(self, mode, current_queue=[]):
        self.queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self.mode = mode
    
    def enqueue(self, item):
        pass
    def dequeue(self):
        pass
    def get_queue(self):
        pass
    def size(self):
        return len(self.queue) 
```

## Example worlflow

1. The CLI show the menu, and the user selects the option to add "Bob" into the queue.
2. The application ads Bob and notifies confirmation on the console and must say how many people are in front of him on the line.
3. The system now shows the menu (starts again) awaiting for the user to pick another option.
4. If the user picks the option to remove from the Queue, the next person on the queue gets eliminated and confirmation message shows.
5. The user must receive an SMS when it is his/her time to eat.
6. If the user picks to see the entire queue state, a list of everyone gets printed with their respective position in the queue.
7. If the user picks to export entire queue, a JSON file with a list of everyone gets created.

## 📖 Fundamentals

This exercise will make you practice the following fundamentals:

1. Executing python files from the command line.
2. Get user input from the command line.
3. Loops, conditionals and functions.
4. Using plain-text files to store data.
5. Complex Data Structures.
6. Queue (FIFO vs FILO)
7. SMS.
