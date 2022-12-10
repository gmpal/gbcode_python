import matplotlib.pyplot as plt
import scipy.stats as stats

N = 10
x = list(range(0,50,1))

def plot_chisquared_density():
    """
    This function plots the chi-squared density and cumulative distribution.
    """
    plt.plot(x, stats.dchisq(x, N), label="chi-squared density")
    plt.title("chi-squared (N={}) density".format(N))

def plot_chisquared_cumulative():
    """
    This function plots the chi-squared cumulative distribution.
    """
    plt.plot(x, stats.pchisq(x, N), label="chi-squared cumulative")
    plt.title("chi-squared (N={}) cumulative distribution".format(N))

    plot_chisquared_density()
    plot_chisquared_cumulative()
    plt.show()