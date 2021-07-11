from sympy import *


def newton(interval, function_expression, precision=0.001):
    function_variable = var("x")
    function = sympify(function_expression)
    if function.subs(function_variable, interval[0]) * function.subs(function_variable, interval[1]) < 0:
        x = (interval[0] + interval[1]) / 2
        derivative_symbol = Symbol("x")
        derivative = diff(function)
        derivative_value = lambdify(derivative_symbol, derivative)
        term = function.subs(function_variable, x) / derivative_value(x)
        while abs(term) >= precision:
            term = function.subs(function_variable, x) / derivative_value(x)
            x = x - term
        return "The value of the root is : {}".format(x)


if __name__ == '__main__':
    given_function = input("please enter your function: ")
    given_interval = eval(input("please enter an interval like [a, b] where a and b are numbers: ")))
    print(newton(given_interval, given_function))
