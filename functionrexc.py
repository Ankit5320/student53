def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Args:
        n: The non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of n.
    """
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    else:
        return n * factorial(n - 1)  # Recursive case

try:
    num = int(input("Enter a non-negative integer: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
