import random
import matplotlib.pyplot as plt

def fair_coin_tossing_experiment(R: int) -> None:
    """
    Perform a fair coin tossing experiment and plot the evolution of the
    relative frequency and the absolute difference between the number of heads and tails.
    
    Parameters
    ----------
    R : int
        The number of coin tosses to perform.
    """
    random.seed(1)
    tosses = [random.choice(["H", "T"]) for _ in range(R)]

    gap = []
    freq = []
    trials = []
    for r in range(1, R + 1, 5000):
        lH = tosses[:r].count("H")
        lT = tosses[:r].count("T")
        gap.append(abs(lH - lT))
        freq.append(lH / r)
        trials.append(r)

    plt.subplot(1, 2, 1)
    plt.plot(trials, freq, "b-")
    plt.plot(trials, [0.5] * len(freq), "r-")
    plt.xlabel("Number of trials")
    plt.ylabel("Relative frequency")
    plt.ylim(0.2, 0.6)

    plt.subplot(1, 2, 2)
    plt.plot(trials, gap, "b-")
    plt.plot(trials, [0] * len(gap), "r-")
    plt.xlabel("Number of trials")
    plt.ylabel("Absolute difference (no. heads and tails)")

fair_coin_tossing_experiment(1000000)
plt.show()