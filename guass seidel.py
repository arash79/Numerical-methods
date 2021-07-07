def gauss_seidel(iteration, coefficient_matrix, right_hand_side_vector, initial_solution=None):
    """ Algorithm can be found on this wikipedia page: https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method """
    assert len(coefficient_matrix[0]) == len(right_hand_side_vector)
    dimension = len(coefficient_matrix)
    if initial_solution is None:
        initial_solution = [0] * dimension
    for iteration_step in range(iteration):
        for i in range(dimension):
            b_i_i = right_hand_side_vector[i]
            for j in range(dimension):
                if i != j:
                    b_i_i -= coefficient_matrix[i][j] * initial_solution[j]
            initial_solution[i] = b_i_i / coefficient_matrix[i][i]
    return initial_solution


if __name__ == '__main__':
    given_matrix = eval(input("enter A matrix like: [[1, 1, 1], [2, 2, 2], [3, 3, 3]\n"))
    vector = eval(input("enter b vector like: [1, 1, 1]\n"))
    iteration_count = int(input("enter the count of iterations: "))
    print("solution is: ", gauss_seidel(iteration_count, given_matrix, vector))
