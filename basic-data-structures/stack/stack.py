class StackBasicImpl:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            removed_item = self.stack.pop()
            return removed_item
        else:
            return None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self) -> bool:
        return True if len(self.stack) == 0 else False

    def __str__(self):
        return '{}'.format([item for item in self.stack])

if __name__ == '__main__':
    stack = StackBasicImpl()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
    print(stack)


