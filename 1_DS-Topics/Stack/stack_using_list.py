# push(n)– This is a user-defined stack method used for inserting an element into the stack.
# The element to be pushed is passed in its argument.

# pop()– We need this method to remove the topmost element from the stack.

# is_empty()– We need this method to check whether the stack is empty or not.

# size()– We need this method to get the size of the stack.

# top()– This stacking method will be used for returning the reference to the topmost element or,
# lastly pushed element in a stack.


# creating stack using list
class Stack:
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, n):
        self.stack.append(n)
        print("Pushed item: " + n)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack.pop()

    def show(self):
        print("The stack elements are:")
        # for i in self.stack:
        #     print(i)
        print(self.stack)


# Example usage
stack = Stack()
stack.push(str(10))
stack.push(str(20))
stack.push(str(30))
stack.push(str(40))
print(stack.is_empty())
print("Popped item: " + stack.pop())
stack.show()
