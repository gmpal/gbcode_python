import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

#TODO: check 

def mixture_density(x1: float, x2: float, w: np.ndarray, centers: np.ndarray, sds: np.ndarray) -> float:
    """
    Evaluate the density of a mixture of gaussians at the given point.
    
    Parameters
    ----------
    x1 : float
        The x1 coordinate.
    x2 : float
        The x2 coordinate.
    w : np.ndarray
        The mixture weights.
    centers : np.ndarray
        The centers of the gaussian components.
    sds : np.ndarray
        The standard deviations of the gaussian components.
        
    Returns
    -------
    float
        The density at the given point.
    """
    m = len(w)
    dens = 0
    for i in range(m):
        dens += w[i] * multivariate_normal.pdf([x1, x2], mean=centers[i], cov=np.diag(sds[i]))
    return dens

def gmm(n: int, w: np.ndarray, centers: np.ndarray, sds: np.ndarray) -> tuple:
    """
    Generate random samples from a mixture of gaussians.
    
    Parameters
    ----------
    n : int
        The number of samples to generate.
    w : np.ndarray
        The mixture weights.
    centers : np.ndarray
        The centers of the gaussian components.
    sds : np.ndarray
        The standard deviations of the gaussian components.
        
    Returns
    -------
    tuple
        A tuple containing the samples, the component indices of each sample, the component centers, and the component standard deviations.
    """
    m = len(w)
    x = np.empty((n, centers.shape[1]))
    w = np.empty(n, dtype=int)
    for i in range(n):
        component = np.random.choice(m, p=w)
        w[i] = component
        x[i] = np.random.multivariate_normal(mean=centers[component], cov=np.diag(sds[component]))
    return x, w, centers, sds

np.random.seed(0)
cols = np.tile(["red", "green", "blue", "magenta", "black", "yellow"], 3)
n = 2000
m = 3
w = np.random.uniform(size=m)
w /= w.sum()
centers = np.random.normal(scale=1.5, size=(m, 2))
sds = np.random.uniform(size=(m, 2))

x1 = np.arange(-3, 3.1, 0.1)
x2 = np.arange(-3, 3.1, 0.1)

d = np.empty((len(x1), len(x2)))
for i, x1_ in enumerate(x1):
    for j, x2_ in enumerate(x2):
        d[i, j] = mixture_density(x1_, x2_, w, centers, sds)

x, w, centers, sds = gmm(n, w, centers, sds)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot_surface(x1, x2, d, cmap="coolwarm")
ax1.set_title(f"Mixture of gaussians with {m} components")

ax2.scatter(x[:, 0], x[:, 1])
for class_ in range(m):
    mask = w == class_
    ax2.scatter(x[mask, 0], x[mask, 1], c=cols[class_ + 2])
ax2.set_xlabel("x1")
ax2.set_ylabel("x2")
ax2.set_title("Samples")

plt.show()