import numpy as np


def gram_schmidt_factorization(matrix):
    matrix = np.array(matrix)
    m, n = matrix.shape
    q = np.zeros((m, n))
    r = np.zeros((n, n))
    matrix = np.transpose(matrix)
    r[0][0] = np.linalg.norm(matrix[0], 2)
    q[:, 0] = matrix[0]/r[0][0]
    for i in range(1, n):
        q[:, i] = matrix[i]
        for j in range(0, i):
            r[j][i] = np.matmul(q[:, j], q[:, i])
            q[:, i] = q[:, i] - (r[j][i] * q[:, j])
        r[i][i] = np.linalg.norm(q[:, i], 2)
        q[:, i] = q[:, i] / r[i][i]
    return q, r


def system_solver(matrix, vector):
    qr_decomposition = gram_schmidt_factorization(matrix)
    q_matrix = qr_decomposition[0]
    r_matrix = qr_decomposition[1]
    redacted_vector = np.matmul(q_matrix.transpose(), np.array(vector).transpose())
    r_matrix_inverse = np.linalg.inv(r_matrix)
    x_vector = np.matmul(r_matrix_inverse, redacted_vector)
    return x_vector


if __name__ == '__main__':
    coefficients_matrix = eval(input("enter A matrix like: [[1, 1, 1], [2, 2, 2], [3, 3, 3]\n"))
    right_hand_side_vector = eval(input("enter b vector like: [1, 1, 1]\n"))
    print(system_solver(coefficients_matrix, right_hand_side_vector))

