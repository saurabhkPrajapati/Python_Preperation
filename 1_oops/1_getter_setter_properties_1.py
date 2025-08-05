
# Getter: A method that allows you to access an attribute in a given class
# @property

# Setter: A method that allows you to set or mutate the value of an attribute in a class
# @setter

from datetime import date


class Employee:
    def __init__(self, name, birth_date):
        self._name = name
        self._birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)


john = Employee("John", "2001-02-07")

print(john.name)

print(john.birth_date)

john.name = "John Doe"
john.birth_date = "2024-11-11"
print(john.name)
print(john.birth_date)
