#!/usr/bin/python3

""" Rotate 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """ Function for rotating 2D Matrix 90 degrees clockwise
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    - Do not return anything. The matrix must be edited in-place.
    - You can assume the matrix will have 2 dimensions and will not be empty.
    """

    n = len(matrix)

    # Create an empty matrix to store the rotated result
    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]

    # Update the original matrix with the rotated result
    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated_matrix[i][j]

# Test case

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
