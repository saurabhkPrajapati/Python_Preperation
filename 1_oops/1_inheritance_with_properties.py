class Person(object):
    def __init__(self, name: str = "Wakanda", age: int = 500) -> None:
        self.name = name
        self.age = age

    def display(self) -> None:
        print(self.name, self.age)


# child class
class Student(Person):
    def __init__(self, name: str = "", age: int = 0, dob: str = "") -> None:
        super().__init__(name="Rahul", age=age) # This is assigming the "Rahul" to name
        # super().__init__(name, age)
        self.name_1 = name
        self.age_1 = age
        self.dob_1 = dob

    def display_info(self) -> None:
        print(self.name_1, self.age_1, self.dob_1)


obj = Person(age=54675786)
obj.display()
print("\n")

obj_1 = Person(name="test1")
obj_1.display()
print("\n")

obj_3 = Student("Mayank", 23, "16-03-2000")
obj_3.display()
obj_3.display_info()

