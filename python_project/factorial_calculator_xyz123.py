import random
import string


def generate_random_filename(extension=".py"):
    """Generates a random filename with the given extension."""
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"factorial_calculator_{random_str}{extension}"


def calculate_factorial(n):
    """Calculates the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python <filename>.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        factorial_result = calculate_factorial(number)
        print(f"The factorial of {number} is {factorial_result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)