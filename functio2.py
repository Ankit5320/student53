def print_numbers_recursive(n):
  """
  Prints numbers from 1 up to n using recursion.

  Args:
    n: The current number to print.
  """
  
  if n == 0:
    return
  else:
    
    print_numbers_recursive(n - 1)
    
    print(n)
print_numbers_recursive(5)
