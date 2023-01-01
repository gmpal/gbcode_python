import random
import numpy as np
import matplotlib.pyplot as plt

R = 10000 # number of realizations of each variable
N = 100 # number of summed variables
sdev = 1
mu = 1

# Generate R normally distributed random variables with mean mu and standard deviation sdev
z = np.random.normal(mu, sdev, R)

# Print the variance of z and plot its histogram
print(f"Var[z] = {np.var(z)}")
plt.hist(z, label=f"single r.v.: mean={mu}, variance={sdev**2}")
plt.legend()
plt.show()

# Generate N normally distributed random variables with mean mu and standard deviation sdev, and sum them
SN = np.zeros(R)
for n in range(N):
  SN += np.random.normal(mu, sdev, R)

# Print the ratio of the variance of the sum of the random variables to the variance of a single random variable, and plot the histogram of the sum
print(f"Var[Sum(z)]/Var[z] = {np.var(SN)/np.var(z)}")
plt.hist(SN, label=f"Sum of {N} r.v.s (mu={mu},var={sdev**2}): variance ~ {round(np.var(SN))}")
plt.legend()
plt.show()

# Calculate the average of the sum of the random variables, and plot its histogram
zbar = SN/N
plt.hist(zbar, label=f"Average of {N} r.v.s (mu={mu},var={sdev**2}): variance ~ {round(np.var(zbar),4)}")
plt.legend()
plt.show()