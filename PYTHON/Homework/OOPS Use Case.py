class BankAccount:


    def __init__(self, initial_balance=0, pin=None):

        self.balance = initial_balance
        self._pin = pin
    def verify_pin(self, pin):

        return self._pin == pin if self._pin is not None else False

    def withdraw(self):

        pin = input("Enter your PIN: ")
        amount = float(input("Enter amount to withdraw: "))

        success, message, new_balance = self._perform_transaction(pin, amount, "withdraw")
        if success:
            print(message)
        else:
            print(message)

    def deposit(self):

        pin = input("Enter your PIN: ")
        amount = float(input("Enter amount to deposit: "))

        success, message, new_balance = self._perform_transaction(pin, amount, "deposit")
        if success:
            print(message)
        else:
            print(message)

    def _perform_transaction(self, pin, amount, transaction_type):

        if not self.verify_pin(pin):
            return False, "Invalid PIN", self.balance

        if transaction_type == "withdraw" and amount > self.balance:
            return False, "Insufficient funds", self.balance

        if transaction_type == "withdraw":
            self.balance -= amount
            message = f"Withdrawal successful! Withdrawn amount: {amount}, New balance: {self.balance}"
        else:
            self.balance += amount
            message = f"Deposit successful! Deposited amount: {amount}, New balance: {self.balance}"

        return True, message, self.balance


my_account = BankAccount(100, "1234")

my_account.withdraw()

my_account.deposit()



OUTPUT - 
Enter your PIN: 1234
Enter amount to withdraw: 100
Withdrawal successful! Withdrawn amount: 100.0, New balance: 0.0
Enter your PIN: 1234
Enter amount to deposit: 2000
Deposit successful! Deposited amount: 2000.0, New balance: 2000.0
