#References:
#http://www.mi.fu-berlin.de/en/math/groups/ag-geom/publications/db/ieee_article_old_low_v3_1.pdf
#---------------
import numpy as np
import matplotlib as mpl

def colour_domain(a, dim_x, dim_y, f):
  """{f} is the function, {a} is the acuity, {dim_x} is the size in x, and {dim_y} is the size in y."""
  x.s, x.e, x.r, y.s, y.e, y.r = -a, a, dim_x, -a, a, dim_y
  x, y = np.ogrid[x.s : x.e : (1j * x.r), y.s : y.e : (1j * y.r)]
  plt.imshow(np.angle(f((x - (1j * y)).T)))
  plt.show()
