class Queue:

    def __init__(self, mode, current_queue=[]):
        self.queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode = FIFO or LIFO"
        else:
            self.mode = mode
    
    def enqueue(self, item):
        if self.mode == 'FIFO':
            return self.queue.append(item)
    def dequeue(self):
        if self.mode == 'FIFO':
            return self.queue.pop(0)
    def get_queue(self):
        return self.queue
    def size(self):
        return len(self.queue) 