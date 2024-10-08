# def rotate_matrix_90_clockwise(matrix):
#     # Step 1: Transpose the matrix
#     transposed_matrix = list(zip(*matrix))
    
#     # Step 2: Reverse each row of the transposed matrix
#     rotated_matrix = [list(row[::-1]) for row in transposed_matrix]
    
#     return rotated_matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# rotated_matrix = rotate_matrix_90_clockwise(matrix)

# for row in rotated_matrix:
#     print(row)

# matrix2 = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# print(list(zip(*matrix2)))

# numbers = [1, 2, 3, 4]
# print(list(reversed(numbers)))
