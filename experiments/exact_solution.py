# knapsack-pulp.py

from pulp import *

v = [[8, 3],[6, 11]]
w = [5, 7]
limit = 17
items  = [0,1]
items2 = [[0,0],[0,1],[1,0],[1,1]]

# Create model
m = LpProblem("QKP", LpMaximize)

# Variables
x = LpVariable.dicts('x', items, lowBound=0, upBound=1, cat=LpInteger)

# Objective
m += sum(v[i[0]][i[1]]*x[i[0]]*x[i[1]] for i in items2)

# Constraint
m += sum(w[i]*x[i] for i in items) <= limit

# Optimize
m.solve()

# Print the status of the solved LP
print("Status = %s" % LpStatus[m.status])

# Print the value of the variables at the optimum
for i in items:
    print("%s = %f" % (x[i].name, x[i].varValue))

# Print the value of the objective
print("Objective = %f" % value(m.objective))
