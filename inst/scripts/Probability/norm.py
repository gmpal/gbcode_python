import numpy as np

# Set seed
np.random.seed(0)

# Set parameters
N = 1000000
mu = 1
sigma = 2

# Generate random normal data
DN = np.random.normal(mu, sigma, N)

# Calculate and print probability that DN is within 1 standard deviation of mu
print(np.sum((DN <= (mu + sigma)) & (DN >= (mu - sigma))) / N)

# Calculate and print probability that DN is within 1.645 standard deviations of mu
print(np.sum((DN <= (mu + 1.645 * sigma)) & (DN >= (mu - 1.645 * sigma))) / N)