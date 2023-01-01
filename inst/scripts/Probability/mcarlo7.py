from scipy.stats import norm
import numpy as np

R = 50000
# number of MC trials

Z2 = []
a = -1
b = 1
muz = (b+a)/2
for r in range(R):
    z = np.random.uniform(a, b)
    Z2.append((z-muz)**2)

print(f"Var. th= {(b-a)**2/12} MC approximation= {np.mean(Z2)}")