n = 5  

for i in range(n):
    
    for j in range(n - i):
        print(chr(65 + j), end=" ")

   
    print("  " * (2 * i - 1), end="")

  
    if i != 0:
        for j in range(n - i - 1, -1, -1):
            print(chr(65 + j), end=" ")
    else:
        for j in range(n - i - 2, -1, -1):
            print(chr(65 + j), end=" ")

    print()
