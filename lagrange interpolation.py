def multiply(array):  # multiply items in a list (list of terms (monomials) will be given to this function)
    result = 1
    for number in array:
        result = result * number
    return result


def term_generator(index, length, x, given_x_values):  # generating terms of the interpolation function
    term = list()
    for i in range(length):
        if index != i:
            term.append((x - given_x_values[i])/(given_x_values[index] - given_x_values[i]))
    return multiply(term)


def lagrange_interpolation(x, given_x_values, given_y_values):
    if len(given_x_values) == len(given_y_values):
        count_of_points = len(given_x_values)
        result = list()
        for i in range(count_of_points):
            result.append(term_generator(i, count_of_points, x, given_x_values) * given_y_values[i])
        return sum(result)
    else:
        return "The count of Xs and Ys should be equal."


given_point = float(input("please enter the point x at which you want to interpolate value: "))
x_values = eval(input("please enter the x values as a list like [1, 1.1, 1.2, 1.3]: "))
y_values = eval(input("please enter the y values as a list like [0.3413, 0.3643, 0.3843, 0.4032]: "))
print("interpolated values is: ", lagrange_interpolation(given_point, x_values, y_values))
