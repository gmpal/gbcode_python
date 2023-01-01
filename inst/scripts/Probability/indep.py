import numpy as np
import matplotlib.pyplot as plt

N = 1000
Dx = np.random.normal(scale=4, size=N)
Dy = np.random.normal(size=N)
indep = 1  # put it to 1 to see a dependency effect

plt.scatter(Dx, indep * Dx + Dy)
plt.xlim(-10, 10)
plt.ylim(-2, 2)
plt.show()