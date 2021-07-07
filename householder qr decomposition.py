import numpy as np


def householder_qr_decomposition(matrix):
    matrix = np.array(matrix)
    m, n = matrix.shape
    matrix_copy = matrix.copy()
    q = np.identity(m)

    def householder_transformation(column_vector):
        vector = column_vector / (column_vector[0] + np.copysign(np.linalg.norm(column_vector), column_vector[0]))
        vector[0] = 1
        tau_value = 2 / np.matmul(np.transpose(vector), vector)
        return vector, tau_value

    for j in range(n):
        v, tau = householder_transformation(matrix_copy[j:, j, np.newaxis])
        householder = np.identity(m)
        householder[j:, j:] -= tau * (np.matmul(v, np.transpose(v)))
        matrix_copy = np.matmul(householder, matrix_copy)
        q = np.matmul(householder, q)
    q = np.transpose(q)
    r = np.triu(matrix_copy[:n])
    return q, r


'''a linear system of equation is solved by Householder QR decomposition with Complete Pivoting method by following
   these steps: 
        1) given system: AX = b
        2) decompose A matrix to A = QR
        3) update system to: QRX = b (hence Q is orthogonal its inverse is equal to its transpose)
        4) solve system: RX = Q⁻¹b 
        5) X = R⁻¹Q⁻¹b'''


def system_solver(matrix, vector):
    qr_decomposition = householder_qr_decomposition(matrix)  # decomposing matrix to Q and R
    q_matrix = qr_decomposition[0]
    r_matrix = qr_decomposition[1]
    redacted_vector = np.matmul(q_matrix.transpose(), np.array(vector).transpose())  # fourth step
    r_matrix_inverse = np.linalg.inv(r_matrix)
    x_vector = np.matmul(r_matrix_inverse, redacted_vector)  # fifth step
    return x_vector


if __name__ == '__main__':
    coefficients_matrix = eval(input("enter A matrix like: [[1, 1, 1], [2, 2, 2], [3, 3, 3]\n"))
    right_hand_side_vector = eval(input("enter b vector like: [1, 1, 1]\n"))
    print(system_solver(coefficients_matrix, right_hand_side_vector))
