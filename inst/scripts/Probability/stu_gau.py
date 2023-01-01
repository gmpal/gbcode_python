import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, t

x = np.arange(-5, 5.05, 0.05)

plt.plot(x, norm.pdf(x))
plt.plot(x, t.pdf(x, df=10), color='red')
plt.plot(x, t.pdf(x, df=3), color='green')

plt.show()

print(norm.ppf(0.95, loc=0, scale=1))
print(t.ppf(0.95, df=10, loc=0, scale=1))

plt.plot(x, norm.pdf(x))
plt.axvline(x=norm.ppf(0.025, loc=0, scale=1), linestyle=':')
plt.axvline(x=norm.ppf(0.975, loc=0, scale=1), linestyle=':')
plt.show()