import numpy as np
import matplotlib.pyplot as pyplot

def domain_colour(a, dim_x, dim_y, f):
    """{f} is the function, {a} is the acuity, {dim_x} is the size in x, and {dim_y} is the size in y."""
    xs, xe, xr, ys, ye, yr = -a, a, dim_x, -a, a, dim_y
    x, y = np.ogrid[xs : xe : (1j * xr), ys : ye : (1j * yr)]
    pyplot.imshow(np.angle(f((x - (1j * y)).T)))
    pyplot.show()

def user_function():
    return lambda z: eval(input("f(z) = "))

def user_graph():
    a = int(input("Acuity: "))
    dim_x = int(input("x-Dimension: "))
    dim_y = int(input("y-Dimension: "))
    f = user_function()
    domain_colour(a, dim_x, dim_y, f)

user_graph()
