import numpy as np

## Monte Carlo validation of Jensen's inequality f(E[x))<= E[f(x)]
## with f=x^2-x
## Let X~Unif(-2,5) -> E[X]=(b+a)/2 , Var(X)=1/12*(b-a)^2 =1/3=E[X^2]-E[X]^2

def f(x):
    return -x**2

R = 10000

fx = []
X = []

a = 1
b = 1

for r in range(R):
    x = np.random.normal(a, b)
    fx.append(f(x))
    X.append(x)

mu_x = np.mean(X)
print("E[f(x)]=", np.mean(fx))
print("f(E[x])=", f(mu_x))