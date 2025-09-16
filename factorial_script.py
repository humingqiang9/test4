import random
import string

def factorial(n):
    """Calculate the factorial of a number"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def generate_random_filename():
    """Generate a random filename"""
    return ''.join(random.choices(string.ascii_lowercase, k=10)) + '.py'

if __name__ == "__main__":
    # Test the factorial function
    test_number = 5
    print(f"Factorial of {test_number} is {factorial(test_number)}")
    
    # Generate and print a random filename
    filename = generate_random_filename()
    print(f"Random filename: {filename}")