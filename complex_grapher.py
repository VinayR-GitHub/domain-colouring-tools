#References:
#http://www.mi.fu-berlin.de/en/math/groups/ag-geom/publications/db/ieee_article_old_low_v3_1.pdf
#---------------
import numpy as np
import matplotlib as mpl

def domain_colour(a, dim_x, dim_y, f):
    """{f} is the function, {a} is the acuity, {dim_x} is the size in x, and {dim_y} is the size in y."""
    x.s, x.e, x.r, y.s, y.e, y.r = -a, a, dim_x, -a, a, dim_y
    x, y = np.ogrid[x.s : x.e : (1j * x.r), y.s : y.e : (1j * y.r)]
    plt.imshow(np.angle(f((x - (1j * y)).T)))
    plt.show()

def user_function():
    return lambda z: eval(input("f(z) = "))

def user_graph():
    u.a = input("Acuity: ")
    u.dim_x = input("x-Dimension: ")
    u.dim_y = input("y-Dimension: ")
    u.f = user_function()
    domain_colour(u.a, u.dim_x, u.dim_y, u.f)

user_graph()
