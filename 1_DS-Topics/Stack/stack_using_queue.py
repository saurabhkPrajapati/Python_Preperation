from queue import LifoQueue


class Stack:
    def __init__(self, maxsize=3):
        self.stack = LifoQueue(maxsize=maxsize)

    def push(self, item):
        if self.stack.full():
            print("The stack is already full with ", self.stack.maxsize, "elements")
        else:
            self.stack.put(item)
            print("Size: ", self.stack.qsize())

    def pop(self):
        if self.stack.empty():
            print("Stack is empty")
        else:
            print('Element popped from the stack is', self.stack.get())
            print("Size: ", self.stack.qsize())

    def get_size(self):
        print(self.stack.qsize())

    def show(self):
        if self.stack.empty():
            print("Stack is empty")
        else:
            print("The stack elements are:")
            # Convert the LifoQueue to a list for display purposes
            temp_stack = self.stack.queue
            for item in reversed(temp_stack):
                print(item)


# Example usage
stack = Stack()
stack.pop()
stack.push(32)
stack.push(56)
stack.push(27)
stack.push(27)
stack.pop()
stack.show()
stack.get_size()
