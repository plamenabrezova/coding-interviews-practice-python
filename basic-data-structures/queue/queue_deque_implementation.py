from collections import deque

class QueueBasicImpl:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue:
            removed_item = self.queue.popleft()
            return removed_item
        return 'Queue is empty.'

    def peek(self):
        return self.queue[0] if self.queue else 'Queue is empty.'

    def __str__(self):
        return '{}'.format([item for item in self.queue])


# this line allows me to execute code when the file runs as a script, but not when it’s imported as a module
if __name__ == '__main__':
    first_queue = QueueBasicImpl()
    first_queue.enqueue(1)
    first_queue.enqueue(2)
    first_queue.enqueue(3)
    first_queue.enqueue(4)
    first_queue.enqueue(5)
    first_queue.enqueue(6)
    print(first_queue)
    first_queue.dequeue()
    print(first_queue)




