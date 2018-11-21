import numpy as np
from AbstractStrategy import AbstractStrategy

class QuadraticKnapsack01Strategy(AbstractStrategy):
    """docstring for QuadraticKnapsack01Strategy."""

    def __init__(self, weights, profits, maxWeight, hillClimbingMaxIterations):
        self.weights = weights
        self.profits = profits
        self.maxWeight = maxWeight
        self.hillClimbingMaxIterations = hillClimbingMaxIterations

        if len(self.profits.shape) != 2:
            raise ValueError( "Error: profits must have 2 dimensions, but have " + str(len(self.profits.shape)) + " dimension")

        if self.weights.shape[0] != self.profits.shape[0] or self.weights.shape[0] != self.profits.shape[1]:
            raise ValueError("Error: both dimensions of profit must have the same size of weights, expected profits dimensions: "+str([weights.shape[0], weights.shape[0]])+", but got: "+str(self.weights.shape))

    """sum of the profits of selecting itens listed in solution to put on the knapsack"""
    def objectiveFunction(self, solution):
        out = 0
        for i in range(self.profits.shape[0]):
            for j in range(self.profits.shape[1]):
                out += self.profits[i,j]*solution[i]*solution[j]
        return out

    """return True if solution1 is better than solution2, return False otherwise"""
    def compareSolution(self, solution1, solution2):
        if self.objectiveFunction(solution1) > self.objectiveFunction(solution2):
            return True
        else:
            return False

    """return a random solution to the knapsack 01 problem"""
    def randomSolution(self):
        return np.random.choice([True, False], self.weights.shape)

    """construct a solution for the quadratic knapsack 01 problem with a greedy algorithm"""
    def construction(self):
        knapsackWeight = 0
        solution = np.zeros(self.weights.size, dtype=bool)

        for i in range(self.weights.size):
            ratio = np.zeros(self.weights.size)
            for j in range(self.weights.size):
                ratio[j] = (self.profits[j,j] + np.sum(self.profits[j]*solution))/self.weights[j]
            selectionPriority = np.flip( ratio.argsort(), axis=0 )

            for j in range(self.weights.size):
                if (solution[ selectionPriority[j] ] == False) and ((knapsackWeight + self.weights[ selectionPriority[j] ]) <= self.maxWeight):
                    solution[ selectionPriority[j] ] = True
                    knapsackWeight += self.weights[ selectionPriority[j] ]
                    break

        return solution

    """try to improve a given solution through local search using hill climbing"""
    def improvement(self, solution):
        bestSolution  = solution
        bestOF  = self.objectiveFunction(solution)

        changes = True
        while i < self.hillClimbingMaxIterations and changes == True:
            changes = False
            atualSolution = bestSolution
            for j in range(solution.size):
                solutionCadidate    = np.array(atualSolution)
                solutionCadidate[j] = not solutionCadidate[j]
                candidateOF         = self.objectiveFunction(solutionCadidate)

                if candidateOF > bestOF:
                    changes = True
                    bestOF  = candidateOF
                    bestSolution = solutionCadidate

        return bestSolution

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
