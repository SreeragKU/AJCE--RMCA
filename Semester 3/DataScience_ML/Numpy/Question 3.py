import numpy as np
from scipy.linalg import svd

matrix_A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
matrix_B = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])

matrix_sum = matrix_A + matrix_B
print("Sum of matrices: \n", matrix_sum)
matrix_product = matrix_A * matrix_B

print("Product of matrices: \n", matrix_product)
matrix_dot = np.dot(matrix_A, matrix_B)

print("Dot Product of matrices: \n", matrix_dot)
matrix_A_transpose = np.transpose(matrix_A)

print("Transpose of matrix A: \n", matrix_A_transpose)
determinant_B = np.linalg.det(matrix_B)

print("Determinant of matrix B: ", determinant_B)
eigenvalues_A, eigenvectors_A = np.linalg.eig(matrix_A)

print("Eigenvalues of matrix A: \n", eigenvalues_A)
print("Eigenvectors of matrix A: \n", eigenvectors_A)

U, s, VT = svd(matrix_A)
print("SVD of Martrix A: ")
print("U: ",U)
print("s: ",s)
print("VT: ",VT)