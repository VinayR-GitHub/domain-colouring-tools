#References:
#https://notebook.community/empet/Math/DomainColoring
#---------------
import numpy as np
import matplotlib.pyplot as mpl
import matplotlib.colors as colsys

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
    """Where {f} is a function of z, {dim_Re} and {dim_Im} are lists outlining the rectangular graphing domain, and {A} represents the number of points in each unit interval."""
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

def colour_map_co(vals, sat):
    """{vals} represents a dataset of values, {sat} represents the colour saturation in the HSV system."""
    h_vals = hue(vals)
    s_vals = sat * np.ones(
        h_vals.shape
    )
    v_vals = absolute_grading(
        np.absolute(vals)
    )
    col_hsv = np.dstack(
        (h_vals, s_vals, v_vals)
    )
    return colsys.hsv_to_rgb(col_hsv)

def colour_map_wm(vals, sat, power = 2):
    """{vals} represents a dataset of values, {sat} represents the colour saturation in the HSV system, and {power} represents the base of the contour plot schema."""
    h_vals = hue(vals)
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
    """{vals} represents a dataset of values, {sat} represents the colour saturation in the HSV system."""
    h_vals = hue(vals)
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

def domain_plot(colmap, f, dim_Re, dim_Im, title = "", sat = 1, A = 500, contour = False, power = 2):
    """Where {f} is a function over z, {dim_Re} and {dim_Im} outline the dimensions of the rectangular domain, {sat} represents saturation, and {A} represents unit interval acuity."""
    vals = eval_func(f, dim_Re, dim_Im, A)
    if contour == True:
        cols = colmap(vals, sat, power)
    else:
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

def file_settings():
    file_name = input("File name: ")
    file_type = "." + input("File type: ") #Do not use full stop in file type.
    return [
        file_name,
        file_type
    ]

def user_mapping(colmap_co, colmap_wm, colmap_ph):
    """Where {colmap} variants define a colour mapping schema."""
    func = input("f(z) = ")
    f = lambda z: eval(
        func
    )
    title = f"${f'f(z)={func}'.replace('**', '^')}$"
    sat = float(
        input("Saturation: ")
    )
    A = int(
        input("Resolution/acuity: ")
    )
    power = float(
        input("Contour gradation power: ")
    )
    dim_Re = [
        float(
            input("Lower real boundary: ")
        ),
        float(
            input("Upper real boundary: ")
        )
    ]
    dim_Im = [
        float(
            input("Lower imaginary boundary: ")
        ),
        float(
            input("Upper imaginary boundary: ")
        )
    ]
    z_dim = [
        float(
            input("Lower real boundary for identity: ")
        ),
        float(
            input("Upper real boundary for identity: ")
        ),
        float(
            input("Lower imaginary boundary for identity: ")
        ),
        float(
            input("Upper imaginary boundary for identity: ")
        )
    ]
    mpl.rcParams['figure.figsize'] = 18, 11
    mpl.subplot(2, 3, 1)
    domain_plot(
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
    domain_plot(
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
    domain_plot(
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
    domain_plot(
        colmap_co,
        identity := lambda z: z,
        [z_dim [0], z_dim [1]],
        [z_dim [2], z_dim [3]],
        "$f(z)=z$",
        sat,
        A,
        False
    )
    mpl.subplot(2, 3, 5)
    domain_plot(
        colmap_wm,
        identity := lambda z: z,
        [z_dim [0], z_dim [1]],
        [z_dim [2], z_dim [3]],
        "$f(z)=z$",
        sat,
        A,
        True,
        power
    )
    mpl.subplot(2, 3, 6)
    domain_plot(
        colmap_ph,
        identity := lambda z: z,
        [z_dim [0], z_dim [1]],
        [z_dim [2], z_dim [3]],
        "$f(z)=z$",
        sat,
        A,
        False
    )
    mpl.tight_layout()
    settings = file_settings()
    mpl.savefig(settings [0] + settings [1])
    mpl.show()

user_mapping(
    colour_map_co,
    colour_map_wm,
    colour_map_ph
)
