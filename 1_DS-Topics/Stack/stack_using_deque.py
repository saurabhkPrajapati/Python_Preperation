from collections import deque, Counter


class Stack:
    def __init__(self, max_len=4):
        self.stack = deque(maxlen=max_len)  # Creating an empty deque

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.stack.maxlen

    def push(self, item):
        if self.is_full():
            print('Stack is full, cannot push more items')
        else:
            self.stack.append(item)  # PUSH operation using append()

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            print('Element popped from stack:')
            print(self.stack.pop())  # POP operation

    def show(self):
        print('Stack elements are:')
        print(self.stack)  # Displaying Stack


# Example usage
stack = Stack()
stack.push(25)
stack.push(56)
stack.push(32)
stack.push(38)
stack.show()

stack.pop()
stack.show()
