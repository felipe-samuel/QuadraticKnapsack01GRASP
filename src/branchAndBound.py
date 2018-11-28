from sys import maxsize

class branchAndBound(object):
    """BranchAndBound for the Quadratic Knapsack 01 problem."""
    def __init__(self, startingSolution = None, solver = None):
        self.solution = startingSolution
        self.solver = solver
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

    def run( self, bestSolutionOF = maxsize ):
        bestSolution = None
        branchs = [[]]

        while len(branchs) > 0:
            print('branch: ', branchs[0])
            solution = self.solver.run(branchs[0])
            print('solution: ', solution)
            otimal = True
            constraints = []
            for i in range(solution.size):
                if solution[i] != 1 and solution[i] != 0:
                    otimal = False
                    add = True
                    for c in branchs[0][:]:
                        if c[0] == i:
                            add = False
                    if add:
                        constraints += [ branchs[0][:] + [(i,1)] ]
                        constraints += [ branchs[0][:] + [(i,0)] ]

            if self.solver.compareSolution(solution, bestSolution):
                if otimal:
                    bestSolution = solution
                else:
                    branchs += constraints
            branchs.pop(0)

        return bestSolution
