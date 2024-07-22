#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        sequence = [0, 1]  # Initialize with the first two numbers of the Fibonacci sequence
        while len(sequence) < length:
            next_num = sequence[-1] + sequence[-2]  # Calculate the next number by adding the last two numbers
            sequence.append(next_num)  # Append the next number to the sequence
        print(sequence)