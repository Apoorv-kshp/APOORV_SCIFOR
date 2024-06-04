__init__ Method:

Definition: The __init__ method is a special method in Python classes, also known as a constructor. 
It is automatically called when a new instance (object) of the class is created.
Purpose: It initializes the attributes of the class and allows you to set initial values.

Syntax and Example:

class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

# Creating an instance of MyClass
obj = MyClass("value1", "value2")

print(obj.attribute1)  # Output: value1
print(obj.attribute2)  # Output: value2


In this example, __init__ initializes the attribute1 and attribute2 attributes with the values provided when creating an instance of MyClass.
