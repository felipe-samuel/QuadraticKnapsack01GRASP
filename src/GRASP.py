from sys import maxsize

class GRASP(object):
    """meta heuristic GRASP implementation"""
    def __init__(self, startingSolution = None, strategy = None):
        super(GRASP, self).__init__()
        self.solution = startingSolution
        self.strategy = strategy
        self.iteration = -1

    def getIteration(self):
        return self.iteration

    def getSolution(self):
        return self.solution

    def setSolution(self, solution):
        self.solution = solution

    def getStrategy(self):
        return self.strategy

    def setStrategy(self, strategy):
        self.strategy = strategy

    def run( max_iterations = maxsize, best_solution = None ):
        self.iteration = 0
        if self.solution == None:
            self.solution = self.strategy.randomSolution()

        while self.iteration < max_iterations and self.strategy.compareSolution(bestSolution, self.solution):
            self.iteration += 1
            self.solution = self.strategy.construction( )
            solutionCadidate = self.strategy.improvement( self.solution )
            if self.strategy.compareSolution(solutionCadidate, self.solution)
                self.solution = solutionCadidate

        return self.solution, self.iteration
