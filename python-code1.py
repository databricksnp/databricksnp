print("my name is reddy")
name = "reddy"
print(f"my name is {name}")
# Function definition to generate fibonacci numbers
from typing import List
def fibonacci_sequence(n: int) -> List[int]:
    fib_sequence = []  # Create an empty list to store Fibonacci numbers
    a, b = 0, 1        # Initialize the first two numbers in the sequence
    
    for _ in range(n):  # Loop 'n' times
        fib_sequence.append(a)  # Add the current number 'a' to the list
        a, b = b, a + b         # Update 'a' and 'b' to the next Fibonacci numbers
    
    return fib_sequence  # Return the full sequence as a list

result = fibonacci_sequence(10)  # Call the function with 10 as input
print(result)