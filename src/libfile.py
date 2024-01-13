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