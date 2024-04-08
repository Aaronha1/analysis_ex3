from matrix_utility import *
from gaussian_elimination import gaussianElimination

def polynomialInterpolation(table_points, x):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points] # Makes the initial matrix
    b = [[point[1]] for point in table_points]
    for i in range(len(matrix)):
        matrix[i].append(b[i][0])

    print( "The matrix obtained from the points: ", '\n', np.array(matrix))
    matrixSol = gaussianElimination(matrix)
    print( "\nMat solve:" , matrixSol )

    result = sum([matrixSol[i] * (x ** i) for i in range(len(matrixSol))])
    print( "\nThe polynom:")
    print('P(X) = '+'+'.join([ '('+str(matrixSol[i])+') * x^' + str(i) + ' ' for i in range(len(matrixSol))]))
    print( f"\nThe Result of P(X={x}) is:")
    print(result)
    return result

if __name__ == '__main__':
    table_points = [(-3.27, -2), (-1.52, 30.2), (4.2, 2.9093), (10.156, -40)]
    x = 0.2
    print( "----------------- Interpolation & Extrapolation Methods -----------------\n")
    print( "Table Points: ", table_points)
    print( "Finding an approximation to the point: ", x,'\n')
    polynomialInterpolation(table_points, x)
    print( "\n---------------------------------------------------------------------------\n")