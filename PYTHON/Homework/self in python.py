self Keyword

Definition: self is a conventional name used to refer to the instance of the class within its methods. 
It is the first parameter of any method in the class (including __init__) and allows access to the attributes and methods of the instance.
Purpose: It differentiates between instance attributes/methods and local variables/methods within the class.

Example:

class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1  # self.attribute1 refers to the instance attribute
        self.attribute2 = attribute2

    def display_attributes(self):
        print(f"attribute1: {self.attribute1}")
        print(f"attribute2: {self.attribute2}")

# Creating an instance of MyClass
obj = MyClass("value1", "value2")

# Accessing the method
obj.display_attributes()
# Output:
# attribute1: value1
# attribute2: value2

In this example, self.attribute1 and self.attribute2 refer to the instance attributes, which are initialized in the __init__ method.
display_attributes is a method that uses self to access and print the instance attributes.
