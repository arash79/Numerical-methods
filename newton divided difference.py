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


p = divided_diff([(-1, -2), (1, 0), (2, 7), (3, 26)], 0.5)
print(p)
