import numpy as np
from numpy.linalg import norm
from inverse_matrix import swap_rows
from matrix_utility import is_diagonally_dominant

def gauss_seidel(A, b, X0, TOL=1e-16, N=300):
    n = len(A)
    for k in range(n):
        # Partial Pivoting: Find the pivot row with the largest absolute value in the current column
        pivot_row = k
        v_max = A[pivot_row][k]
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(v_max):
                v_max = A[i][k]
                pivot_row = i

        # if a principal diagonal element is zero,it denotes that matrix is singular,
        # and will lead to a division-by-zero later.
        if not A[pivot_row][k]:
            return k  # Matrix is singular

        # Swap the current row with the pivot row
        if pivot_row != k:
            swap_rows(A, k, pivot_row)
        # End Partial Pivoting

    if not is_diagonally_dominant(A):
        print('Matrix is NOT diagonally dominant - preforming gauss seidel algorithm\n')
    else:
        print('Matrix is diagonally dominant - preforming gauss seidel algorithm\n')
    k = 1
    print( "Iteration" + "\t\t\t".join([" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(A) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")
    x = np.zeros(n, dtype=np.double)
    while k <= N:
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]
            x[i] = (b[i] - sigma) / A[i][i]

        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        if norm(x - X0, np.inf) < TOL:
            return tuple(x)
        k += 1
        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return tuple(x)


if __name__ == '__main__':

    A = np.array([[3, -1, 1],
                  [0, 2, -1],
                  [0, 1, -2]])

    b = np.array([4, -1, -3])
    X0 = np.zeros_like(b)

    solution =gauss_seidel(A, b, X0)
    print("\nApproximate solution:", solution)