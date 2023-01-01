import numpy as np

np.random.seed(0)
R = 10000

XY = []
X = []
Y = []
for r in range(R):
    x = np.random.normal(0, 1)
    y = 2 * x ** 2
    XY.append(x * y)
    X.append(x)
    Y.append(y)

muX = np.mean(X)
sdX = np.std(X)
sdY = np.std(Y)
print(f"rho[xy]={np.mean(XY) / (sdX * sdY)}")