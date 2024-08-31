#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])  
        return
    elif length == 1:
        print([0])  
        return
    fibonacci_sequence = [0, 1]
    for i in range(2, length):
        next_value = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_value)
    print(fibonacci_sequence[:length])
print_fibonacci(9)