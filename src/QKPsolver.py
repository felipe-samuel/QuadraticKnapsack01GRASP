import numpy as np
from scipy.optimize import minimize

class QKPsolver(object):
    """docstriQKPsolver."""

    def __init__(self, weights, profits, maxWeight):
        self.weights = weights
        self.profits = profits
        self.maxWeight = maxWeight

    """sum of the profits of selecting itens listed in solution to put on the knapsack"""
    def objectiveFunction(self, solution):
        print(solution)
        out = 0
        for i in range(0,self.profits.shape[0]):
            out += self.profits[i,i] * solution[i]
        for i in range(0,self.profits.shape[0]-1):
            for j in range(i+1, self.profits.shape[1]):
                out += self.profits[i,j]*solution[i]*solution[j]
        return out

    """return True if solution1 is better than solution2, return False otherwise"""
    def compareSolution(self, solution1, solution2):
        if solution1 is None or solution2 is None:
            return True
        elif self.objectiveFunction(solution1) > self.objectiveFunction(solution2):
            return True
        else:
            return False

    """return a random solution to the knapsack 01 problem"""
    def randomSolution(self):
        for i in range(100):
            solution = np.random.choice([True, False], self.weights.shape)
            solutionWeight = np.sum(solution*self.weights)
            if solutionWeight < self.maxWeight:
                return solution
        out = np.zeros(self.weights.shape, dtype=bool)
        out[0] = 1
        return out

    def constraint1(self, X):
        return self.maxWeight - np.sum(X*self.weights)

    def constraint2(self, X):
        return X[self.c1] - self.c2

    def run(self, constraints):
        self.c1 = []
        self.c2 = []
        for i in constraints:
            print(i)
            self.c1 += [i[0]]
            self.c2 += [i[1]]

        cons =  [{'type':'ineq', 'fun': self.constraint1},
                 {'type':'eq'  , 'fun': self.constraint2}]

        bnds = []
        for i in range(self.weights.size):
            bnds += [(0,1)]
        start = np.zeros(self.weights.size)
        start[0] = 1

        res = minimize(self.objectiveFunction, start , bounds = bnds, constraints=cons)
        return res.x
