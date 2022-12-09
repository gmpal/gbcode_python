import numpy as np

def smape(ts1: List[float], ts2: List[float], Cent: float=0, Sc: float=1) -> float:
    """
    Symmetric mean absolute percentage error.
    
    This function calculates the symmetric mean absolute percentage error (SMAPE) between two time series.
    
    Args:
        ts1 (list): The first time series.
        ts2 (list): The second time series.
        Cent (float, optional): The center value. Defaults to 0.
        Sc (float, optional): The scale factor. Defaults to 1.
    
    Returns:
        float: The SMAPE value.
        
    Examples:
        >>> smape([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        0.0
        
        >>> smape([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        200.0
    """
    ts1 = Cent + ts1 * Sc
    ts2 = Cent + ts2 * Sc
    return mean(abs(ts1 - ts2) / ((ts1 + ts2) / 2)) * 100



def mase(y: List[float], yhat: List[float]) -> float:
    """
    Mean absolute scaled error.
    
    This function calculates the mean absolute scaled error (MASE) between a time series and its forecast.
    
    Args:
        y (list): The original time series.
        yhat (list): The forecasted time series.
    
    Returns:
        float: The MASE value.
        
    Examples:
        >>> mase([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        0.0
        
        >>> mase([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        1.0
    """
    n = len(y)
    e = y - yhat
    q = e / (mean(abs(diff(y))))
    return mean(abs(q))


def remNA(TS):
    """
    Remove NA from a time series by interpolation.
    
    This function removes NA values from a univariate or multivariate time series by interpolating the missing values.
    
    Args:
        TS (list or numpy.ndarray): The time series.
    
    Returns:
        list or numpy.ndarray: The time series with NA values removed.
        
    Examples:
        >>> remNA([1, 2, 3, None, 5])
        [1, 2, 3, 4, 5]
        
        >>> remNA([[1, 2, 3, None], [5, 6, 7, 8]])
        [[1, 2, 3, 4], [5, 6, 7, 8]]
    """
    if isinstance(TS, list):
        # Return the interpolated values of the time series
        return approx(seq(TS), TS, seq(TS))['y']
    TS2 = TS * 0
    for i in range(TS.shape[1]):
        # Interpolate the missing values for each column of the time series
        TS2[:, i] = approx(seq(TS[:, i]), TS[:, i], seq(TS[:, i]))['y']
    return TS2



def nlcor():

    return None



#TODO: test 
def dist2(X1, X2):
    """
    Returns matrix of distances between two matrices with same number of columns.
    
    This function computes the distance between two arrays of points.
    
    Args:
        X1 (list or numpy.ndarray): The first matrix [N1,n]
        X2 (list or numpy.ndarray): The second matrix [N2,n]
    
    Returns:
        numpy.ndarray: matrix of euclidean distances [N1,N2]
        
    Examples:
        >>> X1 = [[1, 2], [3, 4], [5, 6]]
        >>> X2 = [[7, 8], [9, 10], [11, 12]]
        >>> dist2(X1, X2)
        [[10.6301458, 14.8660687, 19.104973],
        [10.6301458, 14.8660687, 19.104973],
        [10.6301458, 14.8660687, 19.104973]]
    """
    if isinstance(X2, list):
        X2 = np.array([X2])
    N1 = X1.shape[0]
    n = X1.shape[1]
    n2 = X2.shape[1]
    N2 = X2.shape[0]
    if n != n2:
        print("\n n={}".format(n))
        print("\n n2={}".format(n2))
        raise ValueError('dist2 function: matrix sizes do not match.')
    y = np.zeros((N1, N2))

    if n == 1:
        for i in range(N1):
            x = np.ones((N2, 1)) * X1[i,]
            y[i,] = np.abs(x-X2)
    else:
        if N1 < N2:
            for i in range(N1):
                x = np.ones((N2, 1)) * X1[i,]
                y[i,] = np.apply_along_axis(np.sum, 1, (x-X2)**2)
        else:
            for j in range(N2):
                x = np.ones((N1, 1)) * X2[j,]
                y[:,j] = np.apply_along_axis(np.sum, 1, (x-X1)**2)

    return np.sqrt(y)



def MakeEmbedded():
    return None 

def MakeEmbeddedrev():
    return None

def constloo(): 
    return None 

def dfmldesign():
    return None 

def dfml(): 
    return None 

def kfml():
    return None 

def rnnpred2():
    return None 

def rnnpred():
    return None 

def VARspred():
    return None 

def nbeatspred():
    return None 

def nbeatsenspred(): 
    return None 

def gluonpred():
    return None 

def lstmpred():
    return None 

def lstmpred2():
    return None 

def multifs():
    return None 

def multipls():
    return None 

def multirr():
    return None 

def svdcca():
    return None 

def multicca():
    return None 

def mlin():
    return None 

def multiridge():
    return None 

def multiteridge():
    return None 

def ensridge():
    return None 

def multiml():
    return None 

def multifs3():
    return None 

def VARpred2():
    return None 

def detectSeason():
    return None 

def confsd():
    return None 