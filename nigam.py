Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def factorial(n):
...    
...     if n == 0:
...         return 1
...     else:
...         result = 1
...         for i in range(1, n + 1):
...             result *= i
...         return result
... 
... 
... number = int(input("Enter a Number: "))
... 
... if number < 0:
...     print("Factorial is not defined for negative numbers.")
... else:
...    
...     fact = factorial(number)
