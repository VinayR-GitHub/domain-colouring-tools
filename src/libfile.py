import sys
sys.dont_write_bytecode = True

import numpy as np
import scipy as sp

def processing(func_string):
    with open('src/accepted_functions.txt') as func_file:
        acceptance_strings = func_file.readlines()
    accepted_list = [(
        k.split(' ') [-3], k.split(' ') [-1]
    ) for k in acceptance_strings]
    for h in accepted_list:
        func_string = func_string.replace(h [0], h[1])
    func_string = func_string.replace('\n', '')
    return func_string

def hue(z):
    return np.mod(
        np.angle(z) / (2 * np.pi) + 1,
        1
    )

def absolute_grading(z):
    grad = lambda x: (1 - 1 / (1 + x**2))**(1 / (1 + np.pi))
    return grad(
        np.absolute(z)
    )

def eval_func(f, dim_Re, dim_Im, A):
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