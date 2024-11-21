from math import *

a = 0.5
b = 0.7
x1 = 0
xn = 5
dx = 0.5
y = 0
x = 0

for x in range(x1, xn):
    y = sin(a * x) + 3 * pow(cos(b * (x ** 2) + 1), 2)
    x += dx
    if type(x) == float:
        x += dx

print(x)