import numpy as np

mx_cols = 200
mx_rows = 100

# Create 2d Array filled with Int-Value 32 (32 = ASCII Space)
matrix = np.full((mx_cols, mx_rows), 32, dtype=int)
print(matrix)

print(matrix[2,2])