import numpy as np

def chebyshev_relation(mu: float, N: int, sig_range: tuple, d_range: tuple) -> str:
    """
    Check if the Chebyshev relation is satisfied given the specified parameters.
    
    Args:
        mu: the mean of the random variable z
        N: the number of samples to draw from the normal distribution
        sig_range: the range of values to use for sig in the sequence
        d_range: the range of values to use for d in the sequence
        
    Returns:
        "Chebyshev relation IS satisfied" if the relation is satisfied, "Chebyshev relation NOT satisfied" otherwise
        
    Example:
        # check if the Chebyshev relation is satisfied with the given parameters
        print(chebyshev_relation(0, 100, (0.1, 1), (0.1, 1)))
    """
    
    P_hat = []
    Bound = []
    for sig in np.arange(*sig_range, 0.1):
        for d in np.arange(*d_range, 0.1):
            z = np.random.normal(mu, sig, N)
            P_hat.append(np.sum(np.abs(z - mu) >= d) / N)
            Bound.append(min(1, (sig ** 2) / (d ** 2)))
            
    if any(P_hat > Bound):
        return "Chebyshev relation NOT satisfied"
    else:
        return "Chebyshev relation IS satisfied"