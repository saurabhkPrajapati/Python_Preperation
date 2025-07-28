class MyClass:
    def __init__(self):
        self.my_attribute = 42


obj = MyClass()

# Check if the object has the attribute 'my_attribute'
if hasattr(obj, 'my_attribute'):
    print("Object has 'my_attribute':", obj.my_attribute)
else:
    print("Object does not have 'my_attribute'")
