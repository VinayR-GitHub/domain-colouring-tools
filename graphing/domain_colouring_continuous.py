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
