import numpy as np


def jacobi(iteration, coefficient_matrix, right_hand_side_vector, precision=1e-20):
    """Algorithm can be found on this wikipedia page: https://en.wikipedia.org/wiki/Jacobi_method"""
    solution = np.array([0] * len(right_hand_side_vector))
    for iteration_step in range(iteration):
        iteration_solution = np.array([0] * len(solution))
        for i in range(len(coefficient_matrix[0])):
            s1 = np.dot(np.array(coefficient_matrix)[i, :i], solution[:i])
            s2 = np.dot(np.array(coefficient_matrix)[i, i + 1:], solution[i + 1:])
            numerator = np.array(right_hand_side_vector)[i] - s1 - s2
            denominator = np.array(coefficient_matrix)[i, i]
            iteration_solution[i] = numerator / denominator
        if np.allclose(solution, iteration_solution, rtol=precision) is True:
            break
        solution = iteration_solution
    return solution


if __name__ == '__main__':
    given_matrix = eval(input("enter A matrix like: [[1, 1, 1], [2, 2, 2], [3, 3, 3]\n"))
    vector = eval(input("enter b vector like: [1, 1, 1]\n"))
    iteration_count = int(input("enter the count of iterations: "))
    print("solution is: ", jacobi(iteration_count, given_matrix, vector))
