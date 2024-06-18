"""
Encapsulation in Python:
Overview
Encapsulation is one of the fundamental principles of object-oriented programming (OOP). 
It refers to the bundling of data and the methods that operate on that data into a single unit called a class.
Encapsulation restricts direct access to some of an object's components, which can prevent the accidental modification of data. It is achieved using private and protected access modifiers.
Key Concepts
•	Public Members: Accessible from outside the class.
•	Protected Members: Indicated by a single underscore (_), accessible within the class and its subclasses.
•	Private Members: Indicated by a double underscore (__), accessible only within the class.
Real-Life Example: Bank Account
Consider a real-life example of a bank account. The bank account should encapsulate details such as the account balance and account holder's information. 
Direct access to these details should be restricted to prevent unauthorized or accidental changes.
"""
Implementation
Step 1: Defining the Class
We define a BankAccount class that encapsulates the details of a bank account.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

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
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.__balance}"


Step 2: Using the Class
Here’s how we can create and interact with a BankAccount object:

# Creating an instance of BankAccount
account = BankAccount("Alice", 1000)

# Accessing public method
account.deposit(500)  # Deposited 500. New balance is 1500.
account.withdraw(200)  # Withdrew 200. New balance is 1300.

# Trying to access the private attribute directly (will raise an AttributeError)
try:
    print(account.__balance)
except AttributeError as e:
    print(e)  # 'BankAccount' object has no attribute '__balance'

# Accessing the private attribute through a public method
print(account.get_balance())  # 1300

# Printing the account details
print(account)  # Account owner: Alice, Balance: 1300


Explanation
•	The __balance attribute is private, meaning it cannot be accessed directly from outside the class.
•	Methods like deposit and withdraw provide controlled access to modify the balance.
•	The get_balance method allows read-only access to the balance.
•	The __str__ method provides a string representation of the account details, which includes the owner's name and the balance.
By encapsulating the balance attribute, we ensure that it can only be modified through the defined methods, thereby maintaining the integrity of the bank account.
Benefits of Encapsulation
1.	Data Protection: Encapsulation helps protect an object's internal state from unintended or harmful modifications.
2.	Modularity: By encapsulating related data and methods within a class, code is more modular and easier to maintain.
3.	Flexibility: Encapsulated code can be modified independently without affecting other parts of the program.
4.	Abstraction: Encapsulation allows objects to hide their internal implementation details and only expose what is necessary through public methods.
Encapsulation is a crucial concept in OOP that promotes data security, modularity, and maintainability in software development.

