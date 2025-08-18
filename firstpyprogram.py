def print_alphabet_pattern(rows):
    """
    Prints an alphabet pattern similar to the one shown in the image.

    Args:
        rows (int): The number of rows for the pattern (e.g., 5 for A-E).
    """
    for i in range(rows, 0, -1):
        # Print the ascending part of the pattern
        for j in range(i):
            print(chr(65 + j), end="")
        
        # Print spaces for the gap
        num_spaces = 2 * (rows - i)
        print(" " * num_spaces, end="")
        
        # Print the descending part of the pattern
        # Handle the middle 'E' for the first row separately if needed,
        # otherwise, just print in reverse.
        if i == rows:
            for j in range(i - 2, -1, -1): # Skip the middle 'E' and start from D
                print(chr(65 + j), end="")
        else:
            for j in range(i - 1, -1, -1):
                print(chr(65 + j), end="")
        print()

# Call the function to print the pattern
print_alphabet_pattern(5)
