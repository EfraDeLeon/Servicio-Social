#integral
from sympy import symbols, integrate, sin, exp
from sympy.plotting import plot
x=symbols('x')
integ=integrate(sin(x), x, (x,-10,10))
print(integ)

plot(sin(x),(x,-10,10))
