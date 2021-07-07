from sympy import *


def runge_method(function_expression, x_0, y_0, x, h):
    first_variable = var("x")
    second_variable = var("y")
    function = sympify(function_expression)
    iteration_count = int((x - x_0) / h)
    y = y_0
    for i in range(1, iteration_count + 1):
        k1 = h * function.subs([(first_variable, x_0), (second_variable, y)])
        k2 = h * function.subs([(first_variable, x_0 + 0.5 * h), (second_variable, y + 0.5 + k1)])
        k3 = h * function.subs([(first_variable, x_0 + 0.5 * h), (second_variable, y + 0.5 + k2)])
        k4 = h * function.subs([(first_variable, x_0 + h), (second_variable, y + k3)])
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        x_0 = x_0 + h
    return y


'''standardized differential equation means that the derivative section stands on the left side of the equation and the
   other terms of the equation stands on the right side of the equation. for example: dy/dx = 2 * x ** 3 + 4 * y'''
''' REMARK: just enter the right side of the equation as an input. as in the example above you just need to enter 
    2 * x ** 3 + 4 * y to the input.'''
given_equation = input("please enter right side of an standardized differential equation: ")
step_length = float(input("please enter the step length(h): "))
initial_x_value = float(input("please enter an initial x value:"))
initial_y_value = float(input("please enter an initial value y at initial x value: "))
given_x = float(input("please enter a value x at which you want to evaluate y: "))
print("evaluated value of y is: ", runge_method(given_equation, initial_x_value, initial_y_value, given_x, step_length))
