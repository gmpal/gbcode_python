import numpy as np
import matplotlib.pyplot as plt

N = 1000

x = np.random.normal(size=N)
y = np.random.uniform(size=N)
y2 = np.random.normal(size=N)

plt.scatter(x, y)
plt.xlim(-4, 4)
plt.ylim(-1, 2)
plt.show()

plt.scatter(x, y2)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.show()

plt.scatter(x, 2 * x + y2)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.show()

plt.scatter(x, 2 * x ** 2 + y2 - 1)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.show()

plt.scatter(x, np.sin(2 * np.pi * x) + y2 / 2)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.show()
