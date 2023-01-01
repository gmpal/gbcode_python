import numpy as np

## Monte Carlo approximation of covariance
## COV(X,Y)=E[XY]-E[X]E[Y]

## Let X~Unif(a,b) -> E[X]=(b+a)/2 , Var(X)=1/12*(b-a)^2 =1/3=E[X^2]-E[X]^2
## Let Y=K*X
## COV(X,Y)=E[XY]-K*E[X]E[X]=E[K*X^2]-K(E[X]^2)=K(Var(X)+E[X]^2)-K (E[X])^2= K*Var(X)
R=50000
# number of MC trials 

distr="uniform"

XY=[]
X=[]

K=2
if (distr=="uniform"):
  a=1
  b=20
  VX=1/12*(b-a)**2
else:
  mu=1
  sigma=1
  VX=sigma**2
  
for r in range(R):
  if (distr=="uniform"):
    x=np.random.uniform(a, b)
  else:
    x=np.random.normal(mu, sigma)
  y=K*x
  XY.append(x*y)
  X.append(x)  
  
print("Analytical covariance=",K*VX)
print("MonteCarlo covariance=",(np.mean(XY)-K*np.mean(X)**2))