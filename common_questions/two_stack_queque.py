# use one stack to hold the elements as they are enqueued, and another stack to hold the elements as they are dequeued
# when and element is dequeued the enqueue stack is being popped into the dequeue stack so that the enqueued items
# are in reversed order

class TwoStackQueue:
    enqueue_stack = list()
    dequeue_stack = list()

    def enqueue(self, item) -> None:
        self.enqueue_stack.append(item)

    # dequeue operation takes O(1) time on average, because each element is pushed onto the dequeue_stack at most once,
    # and popped from the dequeue_stack at most once.
    def dequeue(self):
        if not self.enqueue_stack and not self.dequeue_stack:
            return None
        elif len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def peek(self):
        if len(self.dequeue_stack) > 0:
            return self.dequeue_stack[0]
        return self.enqueue_stack[-1]

    def is_empty(self) -> bool:
        return len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0

    def size(self) -> int:
        return len(self.enqueue_stack) + len(self.dequeue_stack)


if __name__ == '__main__':
    two_stacks_queue_test = TwoStackQueue()
    two_stacks_queue_test.enqueue('one')
    two_stacks_queue_test.enqueue('two')
    two_stacks_queue_test.enqueue('three')
    two_stacks_queue_test.enqueue('four')

    print(two_stacks_queue_test.dequeue())
    print(two_stacks_queue_test.dequeue())

    two_stacks_queue_test.enqueue('five')

    print(two_stacks_queue_test.dequeue())
    print(two_stacks_queue_test.dequeue())
    print(two_stacks_queue_test.dequeue())
    print(two_stacks_queue_test.dequeue())
