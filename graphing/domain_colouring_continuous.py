#References:
#https://notebook.community/empet/Math/DomainColoring
#---------------
import numpy as np
import matplotlib.pyplot as mpl
import colorsys

def hue(z):
    return np.mod(
        np.angle(z) / (2 * np.pi) + 1,
        1
    )

def absolute_grading(z):
    grad = lambda x: (1 - 1 / (1 + x**2))**0.5
    return grad(
        np.absolute(z)
    )

def eval_func(f, dim_Re, dim_Im, a):
    """Where f is a function of z, dim_Re and dim_Im are tuples outlining the rectangular graphing domain, and A represents the number of points in each unit interval."""
    hei = dim_Im [1] - dim_Im [0]
    len = dim_Re [1] - dim_Re [0]
    h_res = A * hei
    l_res = A * len
    x = np.linspace(
        dim_Re [0],
        dim_Re [1],
        int(l_res)
    )
    y = np.linspace(
        dim_Im [0],
        dim_Im [1],
        int(h_res)
    )
    x, y = np.meshgrid(x, y)
    z = x + (1j * y)
    return f(z)
