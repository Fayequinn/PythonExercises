g = 9.81
u = 44
x = 0.5
y = 1
elev = 80
from math import pi, tan, cos
theta = elev*(pi/180)
print(theta)
Y = y+(x*tan(theta))-((g*(x**2))/(2*((u*cos(theta))**2)))
print(Y)

