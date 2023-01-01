import numpy as np

M = 100  # number of alternatives

x = np.random.normal(size=M)

mu = x**2

N = 10  # number of samples
sdw = 0.2
R = 100

mbest = x[np.argmin(mu)]
best = np.min(mu)
BestHat = []
for r in range(R):
    D = np.empty((0, N))
    for m in range(M):
        D = np.vstack((D, np.random.normal(mu[m], sdw, N)))
    mbesthat = np.argmin(np.mean(D, axis=1))
    besthat = np.min(np.mean(D, axis=1))
    BestHat.append(besthat)

print(np.mean(BestHat))  # E[min]
print(np.min(mu))  # min[E]

print(np.mean(BestHat) - np.min(mu))