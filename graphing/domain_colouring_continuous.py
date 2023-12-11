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

def eval_func(f, dim_Re, dim_Im, A):
    """Where {f} is a function of z, {dim_Re} and {dim_Im} are tuples outlining the rectangular graphing domain, and {A} represents the number of points in each unit interval."""
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

def colour_map(vals, sat):
    """{vals} represents a dataset of values, {sat} represents the colour saturation in the HSV system."""
    h_vals = hue(vals)
    s_vals = s * np.ones(
        h_vals.shape()
    )
    v_vals = absolute_grading(
        np.absolute(vals)
    )
    col_hsv = np.dstack(
        (h_vals, s_vals, v_vals)
    )
    return col_rgb := colorsys.hsv_to_rgb(col_hsv)

def domain_plot(colmap, f, dim_Re, dim_Im, title = "", sat = 1, A = 500):
    """Where {f} is a function over z, {dim_Re} and {dim_Im} outline the dimensions of the rectangular domain, {sat} represents saturation, and {A} represents unit interval acuity."""
    vals = eval_func(f, dim_Re, dim_Im, A)
    cols = colmap(vals, sat)
    mpl.xlabel("$\Re(z)$")
    mpl.ylabel("$\Im(z)$")
    mpl.title(title)
    mpl.imshow(
        cols,
        origin = "lower",
        extent = [
            dim_Re [0],
            dim_Re [1],
            dim_Im [0],
            dim_Im [1]
        ]
    )

