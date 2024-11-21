from math import *

a = 0.5
b = 0.7
x1 = 0
xn = 5
dx = 0.5
y = 0
x = 0

while x <= xn:
    print(x)
    y = sin(a * x) + 3 * pow(cos(b * (x ** 2) + 1), 2)
    print(y)
    x += dx

print(y)
