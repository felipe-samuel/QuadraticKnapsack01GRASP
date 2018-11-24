import numpy as np
from sys import maxsize
from AbstractStrategy import AbstractStrategy


class QuadraticKnapsack01Strategy(AbstractStrategy):
    """docstring for QuadraticKnapsack01Strategy."""

    def __init__(self, weights, profits, maxWeight, alphaConstruction):
        self.weights = weights
        self.profits = profits
        self.maxWeight = maxWeight
        self.alphaConstruction = alphaConstruction

        if len(self.profits.shape) != 2:
            raise ValueError( "Error: profits must have 2 dimensions, but have " + str(len(self.profits.shape)) + " dimension")

        if self.weights.shape[0] != self.profits.shape[0] or self.weights.shape[0] != self.profits.shape[1]:
            raise ValueError("Error: both dimensions of profit must have the same size of weights, expected profits dimensions: "+str([weights.shape[0], weights.shape[0]])+", but got: "+str(self.weights.shape))

    """sum of the profits of selecting itens listed in solution to put on the knapsack"""
    def objectiveFunction(self, solution):
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
        return np.zeros(self.weights.shape, dtype=bool)

    """construct a solution for the quadratic knapsack 01 problem with a random greedy algorithm.
       Uses a Roulette wheel to select itens to add to the knapsack, the probability of an item to be
       selected is given by profit it adds to the knapsack based on the itens already there divided by
       the weight of the item"""
    def construction(self):
        knapsackWeight = 0
        solution = np.zeros(self.weights.size, dtype=bool)
        untestedItens = list(range(self.weights.size))
        while len(untestedItens) > 0:
            ratio = np.zeros(self.weights.size)
            for i in untestedItens:
                for j in range(i, solution.size):
                    if solution[j] == True or i==j:
                        if i <= j:
                            ratio[i] += self.profits[i,j]
                        else:
                            ratio[i] += self.profits[j,i]
                ratio[i] /= self.weights[i]
            maxProfit = np.max(ratio)
            candidate = []
            candidate += (iten for iten in untestedItens if ratio[iten] > self.alphaConstruction * maxProfit)
            if len(candidate) <= 0:
                break 
            j = np.random.choice(candidate)
            if knapsackWeight + self.weights[j] <= self.maxWeight:
                solution[j] = True
                knapsackWeight += self.weights[j]
            untestedItens[:] = (iten for iten in untestedItens if iten != j)
        return solution

    """try to improve a given solution replacing the selected item with the lowest
       profit/weight ratio with the unselect item with the highest one"""
    def improvement(self, solution):
        knapsackWeight = np.sum(solution*self.weights)
        new_solution = np.array(solution)
        ratio = np.zeros(self.weights.size)
        for i in range(0, solution.size):
            for j in range(i, solution.size):
                if solution[j] == True or i==j:
                    if i <= j:
                        ratio[i] += self.profits[i,j]
                    else:
                        ratio[i] += self.profits[j,i]
            ratio[i] /= self.weights[i]
        inItens = []
        inItens += (i for i in range(solution.size) if solution[i] == True )
        while len(inItens) > 0:
            min_i = -1
            min_ratio = maxsize
            for i in inItens:
                if ratio[i] < min_ratio:
                    min_ratio = ratio[i]
                    min_i = i
            outItens = []
            outItens += (i for i in range(solution.size) if solution[i] == False )
            while len(outItens) > 0:
                max_ratio = -1
                max_i = -1
                for i in outItens:
                    if ratio[i] > max_ratio:
                        max_ratio = ratio[i]
                        max_i = i
                if max_ratio > min_ratio and (knapsackWeight+self.weights[max_i]-self.weights[min_i])<=self.maxWeight:
                    new_solution[min_i] = False
                    new_solution[max_i] = True
                    return new_solution
                outItens[:] = (i for i in outItens if i != max_i)
            inItens[:] = (i for i in inItens if i != min_i)
        return new_solution

    """return the problem parameters in a string"""
    def to_string(self):
        output =  'maxWeight: ' + str(self.maxWeight) + '\n'
        output += 'weights: '
        for i in range(self.weights.shape[0]):
            output += str(self.weights[i]) + ' '
        output += '\n'
        output += 'profits:'
        for i in range(self.profits.shape[0]):
            output += '\n'
            for j in range(self.profits.shape[1]):
                output += str(self.profits[i,j]) + ' '
        return output
