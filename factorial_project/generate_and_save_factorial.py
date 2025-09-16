import random
import string


def generate_random_filename(extension='.py'):
    """Generates a random filename with the given extension."""
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"factorial_{random_chars}{extension}"


def calculate_factorial(n):
    """
    Calculates the factorial of a non-negative integer n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)


def main():
    """Main function to demonstrate the factorial calculation and save it to a random file."""
    filename = generate_random_filename()
    print(f"Generating code in file: {filename}")

    with open(filename, 'w') as f:
        f.write("def factorial(n):\n")
        f.write("    if n < 0:\n")
        f.write("        raise ValueError('Factorial is not defined for negative numbers.')\n")
        f.write("    if n == 0 or n == 1:\n")
        f.write("        return 1\n")
        f.write("    result = 1\n")
        f.write("    for i in range(2, n + 1):\n")
        f.write("        result *= i\n")
        f.write("    return result\n")
        f.write("\n")
        f.write("# Example usage:\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    number = 5\n")
        f.write("    print(f'The factorial of {number} is {factorial(number)}')\n")

    print(f"Code successfully written to {filename}")


if __name__ == "__main__":
    main()