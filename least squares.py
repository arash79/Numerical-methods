def linear_least_squares_fit(points, x):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    b_bar_numerator = sum([i * j for i, j in zip(x_values, y_values)]) - (1/len(points)) * sum(x_values) * sum(y_values)
    b_bar_denominator = sum([pow(i, 2) for i in x_values]) - (1/len(points)) * pow(sum(x_values), 2)
    b_bar = b_bar_numerator / b_bar_denominator
    y_values_mean = sum(y_values) / len(points)
    x_values_mean = sum(x_values) / len(points)
    a_bar = y_values_mean - b_bar * x_values_mean
    interpolation_equation = str(a_bar) + " + " + str(b_bar) + " x "
    return "value at given point: {}, interpolation_equation: {}".format(a_bar + b_bar * x, interpolation_equation)


given_point = float(input("please enter the point x at which you want to interpolate value: "))
given_values = eval(input("please enter the values as a list of tuples like [(1, 0.3413), (1.3, 0.4032)]: "))
print("interpolated values is: ", linear_least_squares_fit(given_values, given_point))
