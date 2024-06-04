 # Function to Calculate Factorial of a Number

def factorial(n):
    """Function to calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}.")

# OUTPUT - 
The factorial of 5 is 120.
