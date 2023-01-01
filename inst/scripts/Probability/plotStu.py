import matplotlib.pyplot as plt
from scipy.stats import t
import numpy as np

def plotStu(N=10):
    x = np.arange(-5, 5, 0.1)
    plt.plot(x, t.pdf(x, N), label='Student density')
    plt.title(f"Student (N={N}) density")
    plt.show()
    plt.plot(x, t.cdf(x, N), label='Student cumulative distribution')
    plt.title(f"Student (N={N}) cumulative distribution")
    plt.show()

plotStu()