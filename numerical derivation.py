from sympy import *
from math import comb


def numerical_differentiation(function_expression, order, given_points, x):
    """ Equation can be found on https://en.wikipedia.org/wiki/Numerical_differentiation#Higher-order_methods """
    h = (given_points[-1] - given_points[0]) / len(given_points)
    variable = var("x")
    function = sympify(function_expression)
    terms = list()
    index = given_points.index(x)
    for i in range(order + 1):
        terms.append(pow(-1, i + order) * comb(order, i) * function.subs(variable, given_points[index + i * h]))
    derivative = (1 / pow(h, order)) * sum(terms)
    return "derivative of order " + str(order) + " is: {}".format(derivative)


if __name__ == '__main__':
    given_function = input("please enter a function like 2 * x + 3 * sin(x)")
    differentiation_order = int(input("please enter the order of differentiation: "))
    given_values = eval(input("please enter the values as a list like [1, 1.3413, 1.3863, 1.4032]: "))
    given_point = float(input("please enter the point x at which you want to derive at: "))
    print(numerical_differentiation(given_function, differentiation_order, given_values, given_point))
    

