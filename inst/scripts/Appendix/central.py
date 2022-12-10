import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, uniform

#TODO:check
def plot_average_distributions(n: int, r: int, mn: float, mx: float, var_th: float) -> None:
    """
    Plot the distribution of the average of random variables and their expected distribution.

    This function plots the histogram of the average of N random variables, as well as the expected
    distribution of their mean, for different values of N ranging from 2 to 1000. The random variables
    are uniformly distributed with a minimum value of `mn` and a maximum value of `mx`. The expected
    distribution of the mean is plotted using a normal distribution with variance `var_th` / N.

    Args:
        n: The maximum number of random variables to average.
        r: The number of samples to generate for each average.
        mn: The minimum value of the random variables.
        mx: The maximum value of the random variables.
        var_th: The expected variance of the random variables.

    Returns:
        None
    """

    N = 1
    R = 1000

    I = np.arange(-50, 50, 0.5)

    Mn = -10
    Mx = 10
    var_th = (1 / (Mx - Mn)) * ((Mx ** 3) / 3 - (Mn ** 3) / 3)
    p = uniform.pdf(I, loc=Mn, scale=Mx - Mn)
    plt.plot(I, p, linestyle="-", label="Distribution of r.v. z")
    plt.legend()

    aver = np.zeros(R)

    for N in range(2, 1001):
        for i in range(1, N+1):
            aver = aver + np.random.uniform(Mn, Mx, size=R)
        aver = aver / N
        plt.hist(aver, density=False, label="Average of N={} r.v.s".format(N))
        I2 = np.arange(-5 * np.std(aver), 5 * np.std(aver), 0.5)

        p_var_hat = norm.pdf(I2, loc=0, scale=np.sqrt(var_th / N))
        plt.plot(I2, p_var_hat, linestyle="-", label="p_var_hat")
        plt.legend()

    plt.show()


    return None 