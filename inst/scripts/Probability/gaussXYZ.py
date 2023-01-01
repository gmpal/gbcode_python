import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import scipy.stats as st

def plot_bivariate_gaussians(th: float, ax1: float, ax2: float) -> None:
    """
    Plot a bivariate gaussian with a given orientation and axis lengths.
    
    Parameters
    ----------
    th : float
        The rotation angle of the first principal axis in radians.
    ax1 : float
        The length of the first principal axis.
    ax2 : float
        The length of the second principal axis.
    """
    x = np.arange(-10, 10.5, 0.5)
    y = x
    z = np.zeros((len(x), len(y)))

    rot = np.array([[math.cos(th), -math.sin(th)],
                    [math.sin(th), math.cos(th)]])
    a = np.array([[ax1, 0],
                  [0, ax2]])
    sigma = rot @ a @ rot.T
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            z[i, j] = st.multivariate_normal.pdf([xi, yj], mean=[0, 0], cov=sigma)

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.plot_surface(x, y, z, cmap="Reds")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("p(x, y)")
    plt.title(f"Bivariate Gaussian; Rotation={th:.3f}; Axis 1={ax1}; Axis 2={ax2}")
    plt.show()

for th in np.arange(0, math.pi + 0.125 * math.pi, 0.125 * math.pi):
    for ax2 in [1, 2, 4, 8, 16]:
        plot_bivariate_gaussians(th, 1, ax2)