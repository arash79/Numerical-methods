from sympy import *


def derivative_maximum_value_calculator(function_expression, interval):
    # find maximum value of derivation function at a given interval
    derivative_symbol = symbols('x')
    derivative_function = sympify(function_expression)
    return calculus.util.maximum(derivative_function, derivative_symbol, Interval(interval[0], interval[1]))


def simpson_integration(interval, function_expression, partitions=6):
    assert partitions % 2 == 0
    h = (interval[1] - interval[0]) / partition
    function_variable = var("x")
    function = sympify(function_expression)
    integration_value = function.subs(function_variable, interval[0]) + function.subs(function_variable, interval[1])  # calculating function value
    for i in range(1, partitions, 2):
        integration_value += 4 * function.subs(function_variable, interval[0] + i * h)  # calculating function value
    for i in range(2, partitions - 1, 2):
        integration_value += 2 * function.subs(function_variable, interval[0] + i * h)  # calculating function value
    integration_value = h * integration_value
    forth_derivative = diff(function, "x", 4)  # differentiate function by sympy
    forth_derivative_maximum_value = derivative_maximum_value_calculator(forth_derivative, interval)
    interval_length = interval[1] - interval[0]
    maximum_integration_error = forth_derivative_maximum_value * (pow(interval_length, 5) / (180 * pow(partitions, 4)))
    return "integration value: {}, integration maximum error: {}".format(integration_value, maximum_integration_error)


if __name__ == '__main__':
    given_interval = eval(input("please enter and interval like [a, b] where a and b are numbers: "))
    given_function = input("please enter a function like 2 * x + 3 * sin(x)")
    print(simpson_integration(given_interval, given_function))
