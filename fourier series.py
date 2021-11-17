from sympy import *
from math import pi

function = sympify(input("Enter a function: "))
lower_bound, upper_bound = tuple(eval(input("Enter an interval: ")))
evaluation_point = float(input("Enter the point that you want to evaluate the function in: "))
order = int(input("Enter the order of series: "))
assert lower_bound == - upper_bound
period = (abs(lower_bound) + abs(upper_bound)) / 2
x = symbols("x")
a_0 = (1 / period) * integrate(function, (x, lower_bound, upper_bound)).doit(simplify=True)


def power_series(i):

    def a_n(n):
        n = n * pi / period
        return (1 / period) * integrate(Mul(function, sympify("cos({} * x)".format(n))), (x, lower_bound, upper_bound))

    def b_n(n):
        n = n * pi / period
        return (1 / period) * integrate(Mul(function, sympify("sin({} * x)".format(n))), (x, lower_bound, upper_bound))

    freq = i * pi / period
    return Add(Mul(a_n(i), sympify("cos({}*x)".format(freq))), Mul(b_n(i),  sympify("sin({}*x)".format(freq))))


fourier_series = (1 / 2) * a_0 + sum([power_series(i) for i in range(1, order + 1)])
print("\nfourier series of f(x) = {}:\n".format(function), fourier_series,
      "\nevaluated value at x = {} is: ".format(evaluation_point), fourier_series.subs(x, evaluation_point).evalf())
