from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix
import numpy as np

"""
Function that find the inverse of non-singular matrix
The function performs elementary row operations to transform it into the identity matrix. 
The resulting identity matrix will be the inverse of the input matrix if it is non-singular.
 If the input matrix is singular (i.e., its diagonal elements become zero during row operations), it raises an error.
"""

def swap_rows(matrix, row1, row2):
    temp_matrix = matrix
    N = len(temp_matrix)
    for i in range(N):
        matrix[row1][i], matrix[row2][i] = matrix[row2][i], matrix[row1][i]
    return temp_matrix

def matrix_inverse(matrix):
    #print( f"=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n {matrix}\n")
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    determinant = np.linalg.det(matrix)
    #print("determinant check: ", determinant)
    if determinant == 0:
        raise ValueError("Matrix is singular (determinant is equal to zero) , cannot find its inverse.")

    n = matrix.shape[0]
    identity = np.identity(n)
    count = 0
    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        if matrix[i, i] == 0:
            j = i + 1
            while matrix[j][i] == 0:
                j += 1
            matrix = swap_rows(matrix, i, j)
            elementary_matrix = swap_rows(np.identity(n), i, j)
            identity = np.dot(elementary_matrix, identity)
            #print(f"swap between row {i} and row {j}\n", matrix)


        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            count += 1
            scalar = 1 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            if count <= 3:
                print(elementary_matrix, "\n")
            #print(f"elementary matrix to make the diagonal element 1 :\n {elementary_matrix} \n")

            matrix = np.dot(elementary_matrix, matrix)
            #print(f"The matrix after elementary operation :\n {matrix}")
            identity = np.dot(elementary_matrix, identity)
            #print(f"current inverse :\n {identity}")
            #print( "------------------------------------------------------------------------------------------------------------------",  )


        # Zero out the elements above and below the diagonal
        for j in range(i, n):
            if i != j:
                count += 1
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                if count <= 3:
                    print(elementary_matrix, "\n")
                #print(f"elementary matrix for R{j+1} = R{j+1} + ({scalar}R{i+1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                #print(f"The matrix after elementary operation :\n {matrix}")
                identity = np.dot(elementary_matrix, identity)
                #print(f"current inverse :\n {identity}")
                #print( "------------------------------------------------------------------------------------------------------------------")
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i > j:
                count += 1
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                if count <= 3:
                    print(elementary_matrix, "\n")
                #print(f"elementary matrix for R{j + 1} = R{j + 1} + ({scalar}R{i + 1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                #print(f"The matrix after elementary operation :\n {matrix}")
                identity = np.dot(elementary_matrix, identity)
                # print(f"current inverse :\n {identity}")
                #print(
                #      "------------------------------------------------------------------------------------------------------------------",
                #      )

    return identity

if __name__ == '__main__':
    np.set_printoptions(suppress=True, precision=4)
    #the input matrix test text
    A = np.array([[0, 2, -2],
                  [5, 0, 19],
                  [0, 0, 0]])
    #the solution vector for matrix A
    B = np.array([0, 0, 0])
    """
         (" Date: 8/08/24\n"
               " Group: Eve Hackmon , 209295914 \n"
               "        Yakov Shtefan , 208060111 \n"
               "        Vladislav Rabinovich , 323602383 \n"
               "        Daniel Houri , 209445071 \n"
               " Git: https://github.com/Aaronha1/analysis_ex3 \n"
               " Name: Aaron Hajaj , 311338198
               " Input: \n")
    """
    try:
        A_inverse = matrix_inverse(A)
        #print( "\nInverse of matrix A: \n", A_inverse)
        #print( "\nThe solution vector of matrix A: \n", np.dot(A_inverse, B))

        #print("=====================================================================================================================")

    except ValueError as e:
        print(str(e))