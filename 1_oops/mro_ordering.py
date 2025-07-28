class A:
    def greet(self):
        return "Hello from class A"


class B(A):
    def greet(self):
        return "Hello from class B"


class C(A):
    def greet(self):
        return "Hello from class C"


class D(B, C):
    def __int__(self):
        super().__init__()
    pass


# Method Resolution Order (MRO) for class D
print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# Create an instance of class D
d_instance = D()

# When we call the greet() method on the instance, Python follows the MRO to find the method.
print(d_instance.greet())  # Output: Hello from class B
