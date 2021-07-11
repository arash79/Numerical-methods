def term_generator(given_points, x, k):  # generating terms of the interpolation function
    term = 1
    for i in range(k):
        term = term * (x - given_points[i][0])
    return term


def divided_diff(given_points, x):
    term_count = len(given_points)
    divided_differences = [[0 for i in range(term_count)] for j in range(term_count)]
    for row_index in range(len(divided_differences)):
        divided_differences[row_index][0] = given_points[row_index][1]
    for i in range(1, term_count):
        for j in range(term_count - i):
            numerator = divided_differences[j + 1][i - 1] - divided_differences[j][i - 1]
            denominator = given_points[j + i][0] - given_points[j][0]
            divided_differences[j][i] = numerator / denominator
    result = divided_differences[0][0]
    for t in range(1, term_count):
        result += term_generator(given_points, x, t) * divided_differences[0][t]
    return result


if __name__ == '__main__':
    given_values = eval(input("please enter the values as a list of tuples like [(1, 0.3413), (1.3, 0.4032)]: "))
    given_point = float(input("please enter the point x at which you want to interpolate value: "))
    print(divided_diff(given_values, given_point))
