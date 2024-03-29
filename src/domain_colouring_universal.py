import numpy as np
import scipy as sp
import matplotlib.pyplot as mpl
import matplotlib.colors as colsys
import libfile

def colour_map_co(vals, sat):
    h_vals = libfile.hue(vals)
    s_vals = sat * np.ones(
        h_vals.shape
    )
    v_vals = libfile.absolute_grading(
        np.absolute(vals)
    )
    col_hsv = np.dstack(
        (h_vals, s_vals, v_vals)
    )
    return colsys.hsv_to_rgb(col_hsv)

def colour_map_wm(vals, sat, power = 2):
    h_vals = libfile.hue(vals)
    s_vals = sat * np.ones(
        h_vals.shape
    )
    frac = lambda x: x - np.floor(x)
    v_vals = frac(
        np.nan_to_num(
            np.log(
                np.absolute(vals)
            ) / np.log(power)
        )
    )
    col_hsv = np.dstack(
        (h_vals, s_vals, v_vals**0.2)
    )
    return colsys.hsv_to_rgb(col_hsv)

def colour_map_ph(vals, sat):
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

def file_settings():
    file_name = input('File name: ')
    file_type = '.' + input('File type: ') #Do not use full stop in file type.
    return [
        file_name,
        file_type
    ]

def user_mapping(colmap_co, colmap_wm, colmap_ph, input_list):
    func = input('f(z) = ')
    f = lambda z: eval(
        func
    )
    title = f'${f'f(z)={func}'.replace('**', '^')}$'
    sat = float(
        input('Saturation: ')
    )
    A = int(
        input('Resolution/acuity: ')
    )
    power = float(
        input('Contour gradation power: ')
    )
    dim_Re = [
        float(
            input('Lower real boundary: ')
        ),
        float(
            input('Upper real boundary: ')
        )
    ]
    dim_Im = [
        float(
            input('Lower imaginary boundary: ')
        ),
        float(
            input('Upper imaginary boundary: ')
        )
    ]
    z_dim = [
        float(
            input('Lower real boundary for identity: ')
        ),
        float(
            input('Upper real boundary for identity: ')
        ),
        float(
            input('Lower imaginary boundary for identity: ')
        ),
        float(
            input('Upper imaginary boundary for identity: ')
        )
    ]
    mpl.rcParams['figure.figsize'] = 18, 11
    identity = lambda z: z
    mpl.subplot(2, 3, 1)
    libfile.domain_plot(
        colmap_co,
        f,
        dim_Re,
        dim_Im,
        title,
        sat,
        A,
        False
    )
    mpl.subplot(2, 3, 2)
    libfile.domain_plot(
        colmap_wm,
        f,
        dim_Re,
        dim_Im,
        title,
        sat,
        A,
        True,
        power
    )
    mpl.subplot(2, 3, 3)
    libfile.domain_plot(
        colmap_ph,
        f,
        dim_Re,
        dim_Im,
        title,
        sat,
        A,
        False
    )
    mpl.subplot(2, 3, 4)
    libfile.domain_plot(
        colmap_co,
        identity,
        [z_dim [0], z_dim [1]],
        [z_dim [2], z_dim [3]],
        '$f(z)=z$',
        sat,
        A,
        False
    )
    mpl.subplot(2, 3, 5)
    libfile.domain_plot(
        colmap_wm,
        identity,
        [z_dim [0], z_dim [1]],
        [z_dim [2], z_dim [3]],
        '$f(z)=z$',
        sat,
        A,
        True,
        power
    )
    mpl.subplot(2, 3, 6)
    libfile.domain_plot(
        colmap_ph,
        identity,
        [z_dim [0], z_dim [1]],
        [z_dim [2], z_dim [3]],
        '$f(z)=z$',
        sat,
        A,
        False
    )
    mpl.tight_layout()
    settings = file_settings()
    mpl.savefig(settings [0] + settings [1])
    mpl.show()
