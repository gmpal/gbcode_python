import numpy as np
from numpy.random import multivariate_normal
#TODO:check
def generate_bivariate_data(n=4, rho=0.72, SigmaD=None):
    """
    Generate data from a bivariate normal distribution.
    
    Args:
    - n: int, the number of samples to generate.
    - rho: float, the bivariate correlation.
    - SigmaD: list of floats, the diagonal of the covariance matrix
              (i.e., the marginal variances). If not provided, 
              random values are generated.
              
    Returns:
    - D: array of shape (n, 2), the generated data.
    - Corr2: array of shape (2, 2), the correlation matrix of the generated data.
    """
    
    # Generate random marginal variances if not provided
    if SigmaD is None:
        SigmaD = np.random.uniform(1, 2, size=4)
    
    # Compute the covariance matrix
    Corr = np.array([[1, rho], [rho, 1]])
    Sigma = np.diag(np.sqrt(SigmaD)) @ Corr @ np.diag(np.sqrt(SigmaD))
    
    # Compute the correlation matrix
    Corr2 = np.diag(1/np.sqrt(np.diag(Sigma))) @ Sigma @ np.diag(1/np.sqrt(np.diag(Sigma)))
    
    # Generate the data
    D = multivariate_normal(mean=[0, 0], cov=Sigma, size=n)
    
    return D, Corr2
    
# Generate the data and print the correlation matrix
D, Corr2 = generate_bivariate_data()
print(Corr2)