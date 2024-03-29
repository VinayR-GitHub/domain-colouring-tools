import sys
sys.dont_write_bytecode = True

import numpy as np
import scipy as sp
import matplotlib.pyplot as mpl
import matplotlib.colors as colsys
import libfile

def colour_map(vals, sat):
    h_vals = libfile.hue(vals)
    m_val = 0.7
    M_val = 1
    n_val = 15 #Optimal isochromatic quantity for analytic and conformal mappings.
    phase_func = lambda a, b, c, d: c + ((d - c) * ((a / b) - np.floor(a / b)))
    v_vals = phase_func(h_vals, (1.0 / n_val), m_val, M_val) * phase_func(
        np.nan_to_num(
            np.log(
                np.absolute(vals)
            )
        ),
        (2 * np.pi / n_val),
        m_val,
        M_val
    )
    s_vals = sat * np.ones(
        h_vals.shape
    )
    col_hsv = np.dstack(
        (h_vals, s_vals, v_vals)
    )
    return colsys.hsv_to_rgb(col_hsv)

def pairview(dim_Re, dim_Im, colmap, f, title = '', z_dim = [-10, 10, -10, 10], sat = 1, A = 500):
    mpl.rcParams['figure.figsize'] = 8, 5
    mpl.subplot(1, 2, 1)
    libfile.domain_plot(
        colmap,
        f,
        dim_Re,
        dim_Im,
        title,
        sat,
        A
    )
    mpl.subplot(1, 2, 2)
    libfile.domain_plot(
        colmap,
        identity := lambda z: z,
        [z_dim [0], z_dim [1]],
        [z_dim [2], z_dim [3]],
        '$f(z)=z$',
        sat,
        A
    )
    mpl.tight_layout()

def file_settings():
    if bool(
        input('Save file: ')
    ) == False:
        return [
            None,
            None
        ]
    else:
        file_name = input('File name: ')
        file_type = '.' + input('File type: ') #Do not use full stop in file type.
    return [
        file_name,
        file_type
    ]

def user_mapping(colmap, input_list):
    func = input_list('func (NP)')
    f = lambda z: eval(
        libfile.processing(func) #Have yet to define.
    )
    title = f'${f'f(z)={func}'.replace('**', '^')}$'
    pairview(
        [
            input_list ['rel'],
            input_list ['reu']
        ],
        [
            input_list ['iml'],
            input_list ['imu']
        ],
        colmap,
        f,
        title,
        [
            input_list ['relid'],
            input_list ['reuid'],
            input_list ['imlid'],
            input_list ['imuid'],
        ],
        input_list ['sat'],
        input_list ['acu']
    )
    settings = file_settings()
    if settings [0] == None:
        mpl.show()
    else:
        mpl.savefig(settings [0] + settings [1])
        mpl.show()
