"""
Encapsulation is a fundamental object-oriented principle in Python. 
It protects your classes from accidental changes or deletions and promotes code reusability and maintainability.
Encapsulation allows you to define controlled access to data stored inside objects of your class. 
This allows you to write clean, readable, and efficient code and prevent accidental changes or deletion of your class data.
"""

Problem 1:
Define a class Person with private attributes name and age. Provide public methods to set and get these attributes.

Code:

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

# Example usage:
person = Person("Alice", 30)

# Accessing private attributes via public methods
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30

# Modifying private attributes via public methods
person.set_name("Bob")
person.set_age(25)

print(person.get_name())  # Output: Bob
print(person.get_age())   # Output: 25

OUTPUT :
Alice
30
Bob
25





Problem 2:
Create a class BankAccount with a private attribute balance. Provide methods to deposit and withdraw money, ensuring the balance cannot become negative.

Code:

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

# Example usage:
account = BankAccount(1000)

# Depositing money
account.deposit(500)  # Output: Deposited 500. New balance is 1500.

# Withdrawing money
account.withdraw(200)  # Output: Withdrew 200. New balance is 1300.

# Attempting to withdraw more money than available
account.withdraw(1500)  # Output: Insufficient balance or invalid amount.

# Checking the balance via getter method
print(account.get_balance())  # Output: 1300



OUTPUT :
Deposited 500. New balance is 1500.
Withdrew 200. New balance is 1300.
Insufficient balance or invalid amount.
1300

