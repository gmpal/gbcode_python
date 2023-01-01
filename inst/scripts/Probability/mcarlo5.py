import numpy as np



## Monte Carlo estimation of E[max(X,Y)]


np.random.seed(0)

R = 10000
theta = []
X = []
Y = []

for _ in range(R):
    x = np.random.normal(0, 2)
    y = np.random.uniform(-1, 1)
    theta.append(max(x, y))
    X.append(x)
    Y.append(y)

mu_x = np.mean(X)
sd_x = np.std(X)
sd_y = np.std(Y)

print("Est=", np.mean(theta))
plt.hist(theta)
