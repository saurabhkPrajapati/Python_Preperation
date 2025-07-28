# Not all objects can be copied that way because some of the object’s fields may be private and not visible from outside of the object itself.
# Private fields cannot be accessed and modified outside the class without using name mangling

import copy


class Document:
    def __init__(self, title, content):
        self.__title = title  # Private field
        self.__content = content  # Private field

    def get_info(self):
        return f"Document(title={self.__title}, content={self.__content})"


# Attempting to clone outside the class
original_doc = Document("Confidential", "Top secret content")

# Shallow copy without access to private fields
cloned_doc = copy.copy(original_doc)
cloned_doc.__title = "Cloned Document"  # This will create a new attribute, not modify the original private field

print("Original Document:", original_doc.get_info())
print("Cloned Document:", cloned_doc.get_info())

# ______________________________________________________________________________________________________________________________________________________________________

# If we redefine Document with protected fields (using a single underscore),
# then the shallow copy would work as intended because protected fields can be accessed and modified outside the class.

import copy


class Document:
    def __init__(self, title, content):
        self._title = title  # Protected field
        self._content = content  # Protected field

    def get_info(self):
        return f"Document(title={self._title}, content={self._content})"


# Attempting to clone outside the class
original_doc = Document("Confidential", "Top secret content")

# Shallow copy with access to protected fields
cloned_doc = copy.copy(original_doc)
cloned_doc._title = "Cloned Document"  # This directly modifies the protected field

print("Original Document:", original_doc.get_info())
print("Cloned Document:", cloned_doc.get_info())
