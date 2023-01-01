import numpy as np
from scipy.stats import norm

## Monte Carlo estimation of P(x \in [a,b])

np.random.seed(0)
R = 100000
a = 1
b = 1.2
Y = []

for _ in range(R):
    x = np.random.normal(0, 2)
    y = 1 if a < x < b else 0
    Y.append(y)
    
print(f"Est={np.mean(Y)}:{norm.cdf(b, 0, 2) - norm.cdf(a, 0, 2)}")