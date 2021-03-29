#!/usr/bin/env python
import numpy as np
from numpy import random


def hw_2():
    # Create matrix A with size (3,5) containing random numbers
    A = random.randint(0, 99, size=(3, 5))
    print(f'A =\n{A}')

    # Find the size and length of matrix A
    print(f'A.shape =\n{A.shape}')

    # Resize (crop/slice) matrix A to size (3,4)
    A = A[0:3, 0:4]
    print(f'Resize A =\n{A}\nA.shape =\n{A.shape}')

    # Find the transpose of matrix A and assign it to B
    B = A.T
    print(f'B =\n{B}\nB.shape =\n{B.shape}')

    # Find the minimum value in column 1 of matrix B
    print(f'Minimum of column 1 of B =\n{B[:, 0].min()}')

    # Find the minimum and maximum values for the entire matrix A
    print(f'max of A = {A.max()}\nmin of A = {A.min()}')

    # Create vector X (an array) with 4 random numbers
    X = random.randint(0, 100, size=(1, 4))[0]
    print(f'Vector X = {X}')

    # Create a function and pass vector X and matrix A in it,
    # in the new function multiply vector X with matrix A and assign the result to D
    D = vector_matrix_multiply(A, X)
    print(f'Output of vector_matrix_multiply = {D}')

    # Create a complex number Z with absolute and real parts != 0
    Z = 1.2 + 1j
    print(f'Z = {Z}')
    # Show its real and imaginary parts as well as it’s absolute value
    print(f'real = {Z.real}, imag = {Z.imag}, abs = {np.abs(Z)}')

    # Multiply result D with the absolute value of Z and record it to C
    C = Z.real * D
    print(f'Z.real * D, = {C}')

    # Convert matrix B from a matrix to a string and overwrite B
    B = np.array_str(B)
    print(f'array_str(B) =\n{B}')
    # Display a text on the screen: `Name is done with HW2`, but pass your `Name` as a string variable
    Name = 'Rashmi'
    print(f'{Name} is done with HW2')


# Create a function and pass vector X and matrix A in it
def vector_matrix_multiply(A, X):
    return np.matmul(A, X)


if __name__ == '__main__':
    hw_2()
