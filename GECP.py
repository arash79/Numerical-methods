import numpy as np
import scipy


'''Gaussian Elimination with Complete Pivoting. it will result in a decomposition of form: PAQ = LU.'''


def gaussian_elimination_complete_pivoting(matrix):
    matrix = np.array(matrix)
    m, n = matrix.shape
    multipliers = np.zeros((n, n))
    p_matrix = np.identity(n)
    q_matrix = np.identity(n)
    assert m == n
    absolute_matrix = np.absolute(matrix)
    for k in range(n - 1):
        '''finding the maximum absolute value indices (row & column) of the given matrix.'''
        r, s = np.unravel_index(absolute_matrix.argmax(), absolute_matrix.shape)
        if matrix[r, s] == 0:
            break
        for j in range(k, n):
            matrix[[k, r]] = matrix[[r, k]]  # swapping rows
        p_matrix[[k, r]] = p_matrix[[r, k]]  # generating this step P matrix
        for i in range(n):
            matrix[:, [s, k]] = matrix[:, [k, s]]  # swapping columns
        q_matrix[:, [s, k]] = q_matrix[:, [k, s]]  # generating this step Q matrix
        for t in range(k + 1, n):
            multipliers[t, k] = - (matrix[t, k] / matrix[k, k])  # generating m_i_j multipliers
        for q in range(k, n):
            for e in range(k, n):
                matrix[q, e] += (multipliers[q, k] * matrix[k, e])  # updating matrix entries to form U matrix
        u_matrix = matrix
        l_matrix = np.identity(n)  # creating an identity matrix to form L matrix.
        for row in range(n):
            for column in range(row):
                l_matrix[row, column] = - multipliers[row, column]  # updating identity matrix entries to form L matrix
        return l_matrix, u_matrix, p_matrix, q_matrix


'''a linear system of equation is solved by Gaussian Elimination with Complete Pivoting method by following these steps: 
        1) given system: AX = b
        2) decompose A matrix to PAQ = LU
        3) solve system: LZ = Pb
        4) solve system: UY = z
        5) X = QY'''


def solver(coefficient_matrix, right_hand_side_vector):
    l, u, p, q = gaussian_elimination_complete_pivoting(coefficient_matrix)  # decomposing matrix A
    z = scipy.linalg.solve_triangular(l, np.matmul(p, right_hand_side_vector))  # third step
    y = scipy.linalg.solve_triangular(u, z)  # forth step
    solution = np.matmul(q, y)  # fifth step
    return solution


if __name__ == '__main__':
    given_matrix = eval(input("enter A matrix like: [[1, 1, 1], [2, 2, 2], [3, 3, 3]\n"))
    vector = eval(input("enter b vector like: [1, 1, 1]\n"))
    print("solution is: ", solver(given_matrix, vector))
