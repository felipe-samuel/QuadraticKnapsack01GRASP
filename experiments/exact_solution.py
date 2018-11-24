import sys
import os
sys.path.append('../src')
import numpy as np
from scipy.optimize import minimize
import QKPInstanceReader as QKPreader

instance = QKPreader.read('../Data/test/example_input.txt',0.8)

weights = instance.weights
profits = instance.profits
max_weight = instance.maxWeight
n=weights.size

class ClassName(object):
    """docstring for ."""
    def __init__(self, arg):
        self.arg = arg

    def objective_funtion(self, X):
        value = 0
        print(X)
        for i in range(X.shape[0]):
            for j in range(i,X.shape[0]):
                value  -= profits[i,j]*X[i]*X[j]
        return value

    def constraint(self, X):
        A = max_weight - np.sum(X*weights)
        print(A)
        return A

a = ClassName([])

cons = {'type':'ineq', 'fun': a.constraint }

bnds = []
for i in range(weights.size):
    bnds += [(0,1)]
start = np.zeros(weights.size)
start[0] = 1

res = minimize(a.objective_funtion, start , bounds = bnds, constraints=cons)
print(res)
