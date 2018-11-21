import numpy as np
import csv
from QuadraticKnapsack01Strategy import QuadraticKnapsack01Strategy as QK
def read(file_name, max_iterations):
    i = 0
    n = -1
    maxWeight = -1
    profits = None
    weights = None
    with open( file_name ) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=(' '), quotechar='|')
        for row in spamreader:
            if i == 0:
                pass
            elif i==1:
                n = int(row[0])
                profits = np.zeros([n,n], dtype = int)
                weights = np.zeros([n],   dtype = int)
            elif i == 2:
                for j in range(len(row)):
                    profits[j,j] = int(row[j])
            elif i >= 3 and i < n+2:
                for j in range(len(row)):
                    profits[ i-3, j+i-2 ] = int(row[j])
            elif i >= n+2 and i < n+4:
                pass
            elif i == n+4:
                maxWeight = int(row[0])
            elif i == n+5:
                for j in range(len(row)):
                    weights[j] = int(row[j])
            i+=1
    return QK(weights, profits, maxWeight, max_iterations)

if __name__ == "__main__":
    a = read('Data/test/example_input.txt',10)
    print(a.to_string())
