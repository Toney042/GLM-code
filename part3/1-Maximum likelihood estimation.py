import numpy as np
from scipy.special import comb
from scipy.optimize import minimize

def likelihood(phi, n, k):
    """
    Calculate the likelihood of a binomial distribution with parameters phi, n, and k.
    """
    return -(comb(n, k) * (phi**k) * ((1-phi)**(n-k)))  

def mle(n, k):
    """
    Calculate the maximum likelihood estimate of phi for a binomial distribution given n and k.
    """
    result = minimize(likelihood, 0.5, args=(n, k), bounds=[(0.01, 0.99)])  
    return result.x[0] 
 
# Suppose we observe 10 trials, 7 of which are successful
n = 10
k = 7

# Calculate the  maximum likelihood estimation
phi_hat = mle(n, k)
print(f"phi_hat = {phi_hat}")  