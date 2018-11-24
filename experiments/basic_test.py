import sys
sys.path.append('../src')

from QuadraticKnapsack01Strategy import QuadraticKnapsack01Strategy
import QKPInstanceReader as QKPreader
from GRASP import GRASP

instance = QKPreader.read('../Data/test/example_input.txt',0.8)
g = GRASP( strategy = instance )
out = g.run(maxIterations = 1000, bestSolutionOF = 1609)
print(out)
