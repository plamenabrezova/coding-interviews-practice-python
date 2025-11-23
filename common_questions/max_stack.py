# data structure that efficiently supports the stack operations (push and pop)
# and also a return-the-maximum operation
# (assuming the elements are real numbers so that I can compare them)

class MaxStack:
    def __init__(self):
        self.stack = list()
        # auxiliary stack
        self.max_stack = list()

    def push(self, item):
        self.stack.append(item)

        if not self.max_stack or item > self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        if not self.stack:
            return None
        popped_element = self.stack.pop()
        if popped_element == self.max_stack[-1]:
            self.max_stack.pop()

        return popped_element

    def get_max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]
