Python Code for all the level of Inharitance

# Single Inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"Parent: {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        return f"Child: {self.name}, Age: {self.age}"

# Multiple Inheritance
class Base1:
    def __init__(self):
        self.str1 = "Base1"

class Base2:
    def __init__(self):
        self.str2 = "Base2"

class DerivedMultiple(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

    def show(self):
        return f"{self.str1} and {self.str2}"

# Multilevel Inheritance
class GrandParent:
    def __init__(self, grandparent_name):
        self.grandparent_name = grandparent_name

class ParentMulti(GrandParent):
    def __init__(self, grandparent_name, parent_name):
        super().__init__(grandparent_name)
        self.parent_name = parent_name

class ChildMulti(ParentMulti):
    def __init__(self, grandparent_name, parent_name, child_name):
        super().__init__(grandparent_name, parent_name)
        self.child_name = child_name

    def show(self):
        return f"Grandparent: {self.grandparent_name}, Parent: {self.parent_name}, Child: {self.child_name}"

# Hierarchical Inheritance
class ParentHierarchical:
    def __init__(self, parent_name):
        self.parent_name = parent_name

class Child1(ParentHierarchical):
    def __init__(self, parent_name, child1_name):
        super().__init__(parent_name)
        self.child1_name = child1_name

    def show(self):
        return f"Parent: {self.parent_name}, Child1: {self.child1_name}"

class Child2(ParentHierarchical):
    def __init__(self, parent_name, child2_name):
        super().__init__(parent_name)
        self.child2_name = child2_name

    def show(self):
        return f"Parent: {self.parent_name}, Child2: {self.child2_name}"

# Hybrid Inheritance
class BaseHybrid:
    def __init__(self, base_name):
        self.base_name = base_name

class Intermediate1(BaseHybrid):
    def __init__(self, base_name, intermediate1_name):
        BaseHybrid.__init__(self, base_name)
        self.intermediate1_name = intermediate1_name

class Intermediate2(BaseHybrid):
    def __init__(self, base_name, intermediate2_name):
        BaseHybrid.__init__(self, base_name)
        self.intermediate2_name = intermediate2_name

class DerivedHybrid(Intermediate1, Intermediate2):
    def __init__(self, base_name, intermediate1_name, intermediate2_name, derived_name):
        Intermediate1.__init__(self, base_name, intermediate1_name)
        Intermediate2.__init__(self, base_name, intermediate2_name)
        self.derived_name = derived_name

    def show(self):
        return f"Base: {self.base_name}, Intermediate1: {self.intermediate1_name}, Intermediate2: {self.intermediate2_name}, Derived: {self.derived_name}"

# Demonstrate all inheritance types
# Single Inheritance
single = Child("John", 10)
print(single.show())

# Multiple Inheritance
multiple = DerivedMultiple()
print(multiple.show())

# Multilevel Inheritance
multi = ChildMulti("Grandpa Joe", "Parent Jim", "Child Jack")
print(multi.show())

# Hierarchical Inheritance
hier1 = Child1("Parent Paul", "Child Charlie")
hier2 = Child2("Parent Paul", "Child Chris")
print(hier1.show())
print(hier2.show())

# Hybrid Inheritance
hybrid = DerivedHybrid("Base Hybrid", "Intermediate1", "Intermediate2", "Derived")
print(hybrid.show())


OUTPUT -
Child: John, Age: 10
Base1 and Base2
Grandparent: Grandpa Joe, Parent: Parent Jim, Child: Child Jack
Parent: Parent Paul, Child1: Child Charlie
Parent: Parent Paul, Child2: Child Chris
Base: Base Hybrid, Intermediate1: Intermediate1, Intermediate2: Intermediate2, Derived: Derived

"""
Explanation

    Single Inheritance:
        Parent class is the base class.
        Child class is the derived class inheriting from Parent.

    Multiple Inheritance:
        Base1 and Base2 are base classes.
        DerivedMultiple class inherits from both Base1 and Base2.

    Multilevel Inheritance:
        GrandParent is the base class.
        ParentMulti class inherits from GrandParent.
        ChildMulti class inherits from ParentMulti.

    Hierarchical Inheritance:
        ParentHierarchical is the base class.
        Child1 and Child2 are derived classes inheriting from ParentHierarchical.

    Hybrid Inheritance:
        BaseHybrid is the base class.
        Intermediate1 and Intermediate2 are derived from BaseHybrid.
        DerivedHybrid inherits from both Intermediate1 and Intermediate2.
        """


Question - 2 : Python code of Method Overriding

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return "Meow!"

# Creating instances of each class
generic_animal = Animal("Generic Animal")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")

# Calling the speak method on each instance
print(generic_animal.speak())  
print(dog.speak())             
print(cat.speak())             

OUTPUT - 
Some generic animal sound
Woof!
Meow!

"""
Explanation

    Base Class (Animal):
        The Animal class has an __init__ method to initialize the name attribute.
        It also has a speak method that returns a generic animal sound.

    Derived Class (Dog):
        The Dog class inherits from the Animal class.
        It has its own __init__ method that calls the __init__ method of the Animal class using super().
        It overrides the speak method to return "Woof!".

    Derived Class (Cat):
        The Cat class also inherits from the Animal class.
        It has its own __init__ method that calls the __init__ method of the Animal class using super().
        It overrides the speak method to return "Meow!".

When you call the speak method on an instance of Dog or Cat, the overridden method in the respective subclass is executed, demonstrating method overriding. 
This allows the Dog and Cat classes to provide their specific implementations of the speak method while still being recognized as Animal objects.
"""



Question - 3 : Python code of Method Overloading 

1 - Using Default Arguments:

class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an instance of MathOperations
math_op = MathOperations()

# Call the add method with different number of arguments
print(math_op.add(5))        # Output: 5
print(math_op.add(5, 10))    # Output: 15
print(math_op.add(5, 10, 15)) # Output: 30

2 - Using Variable-Length Arguments:

class MathOperations:
    def add(self, *args):
        return sum(args)

# Create an instance of MathOperations
math_op = MathOperations()

# Call the add method with different number of arguments
print(math_op.add(5))        # Output: 5
print(math_op.add(5, 10))    # Output: 15
print(math_op.add(5, 10, 15)) # Output: 30

3 - Using Type Checking:

class MathOperations:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
            return a + b + c

# Create an instance of MathOperations
math_op = MathOperations()

# Call the add method with different number of arguments
print(math_op.add(5))        # Output: 5
print(math_op.add(5, 10))    # Output: 15
print(math_op.add(5, 10, 15)) # Output: 30

OUTPUT - 
5
15
30 

"""
Explanation

    Using Default Arguments:
        The add method has default values for the second and third parameters. If fewer arguments are passed, the default values are used.

    Using Variable-Length Arguments:
        The add method uses *args to accept a variable number of arguments and sums them up.

    Using Type Checking:
        The add method checks how many arguments are None and performs the addition accordingly.

These examples demonstrate how to achieve method overloading in Python by using techniques that accommodate varying numbers of parameters within a single method definition.
"""
