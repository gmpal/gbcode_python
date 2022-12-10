import numpy as np

def correlated_matrix(N, Sigma):
    """
    Generate a correlated matrix Rc with dimensions Nx3 using a given covariance matrix Sigma.
    
    Parameters
    ----------
    N : int
        The number of rows in the matrix.
    Sigma : numpy array
        The covariance matrix of size 3x3.
    
    Returns
    -------
    Rc : numpy array
        The correlated matrix of size Nx3.
    """
    
    # Cholesky decomposition
    A = np.linalg.cholesky(Sigma)
    
    # Random data in three columns each for X, Y, and Z
    D = np.random.normal(size=(N, 3))
    
    # Correlated matrix Rc
    Rc = D.dot(A)
    
    return Rc

# Test the function
N = 1000
Sigma = np.array([[1, 0.5, 0.3],
                  [0.5, 1, 0.3],
                  [0.3, 0.3, 1]])
Rc = correlated_matrix(N, Sigma)
print(np.cov(Rc))