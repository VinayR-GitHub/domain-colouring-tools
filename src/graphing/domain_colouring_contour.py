import numpy as np
import matplotlib.pyplot as mpl
import matplotlib.colors as colsys

def hue(z):
    return np.mod(
        np.angle(z) / (2 * np.pi) + 1,
        1
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

def domain_plot(colmap, f, dim_Re, dim_Im, title = "", sat = 1, A = 500, power = 2):
    """Where {f} is a function over z, {dim_Re} and {dim_Im} outline the dimensions of the rectangular domain, {sat} represents saturation, and {A} represents unit interval acuity."""
    vals = eval_func(f, dim_Re, dim_Im, A)
    cols = colmap(vals, sat, power)
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

def pairview(dim_Re, dim_Im, colmap, f, title = "", z_dim = [-10, 10, -10, 10], sat = 1, A = 500, power = 2):
    """Where {f} is a function over z, {dim_Re}, {dim_Im}, and {z_dim} outline the dimensions of the rectangular domain, {sat} represents saturation, {A} represents unit interval acuity."""
    mpl.rcParams['figure.figsize'] = 8, 5
    mpl.subplot(1, 2, 1)
    domain_plot(
        colmap,
        f,
        dim_Re,
        dim_Im,
        title,
        sat,
        A,
        power
    )
    mpl.subplot(1, 2, 2)
    domain_plot(
        colmap,
        identity := lambda z: z,
        [z_dim [0], z_dim [1]],
        [z_dim [2], z_dim [3]],
        "$f(z)=z$",
        sat,
        A,
        power
    )
    mpl.tight_layout()

def file_settings():
    if bool(
        input("Save file: ")
    ) == False:
        return [
            None,
            None
        ]
    else:
        file_name = input("File name: ")
        file_type = "." + input("File type: ") #Do not use full stop in file type.
    return [
        file_name,
        file_type
    ]

def user_mapping(colmap):
    """Where {colmap} defines a colour mapping schema."""
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
    pair = bool(
        input("Pair viewing: ") #Takes only True/False.
    )
    if pair == False:
        pass
    elif pair == True:
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
    if pair == False:
        domain_plot(
            colmap,
            f,
            dim_Re,
            dim_Im,
            title,
            sat,
            A,
            power
        )
    elif pair == True:
        pairview(
            dim_Re,
            dim_Im,
            colmap,
            f,
            title,
            z_dim,
            sat,
            A,
            power
        )
    settings = file_settings()
    if settings [0] == None:
        mpl.show()
    else:
        mpl.savefig(settings [0] + settings [1])
        mpl.show()

user_mapping(colour_map_wm)
