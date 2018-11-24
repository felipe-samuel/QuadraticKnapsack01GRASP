import sys
import os
sys.path.append('../src')

from branchAndBound import branchAndBound
from QKPsolver import QKPsolver
import QKPInstanceReader as QKPreader

input_dir = '../Data/dataset'
bestSolutionsOF = {'jeu_100_25_1.txt':18558,
                   'jeu_100_25_2.txt':56525,
                   'jeu_100_25_3.txt':3752,
                   'jeu_100_25_4.txt':50382,
                   'jeu_100_25_5.txt':61494,
                   'jeu_100_25_6.txt':36360,
                   'jeu_100_25_7.txt':14657,
                   'jeu_100_25_8.txt':20452,
                   'jeu_100_25_9.txt':35438,
                   'jeu_100_25_10.txt':24930,
                   'jeu_200_100_1.txt':937149,
                   'jeu_200_100_2.txt':303058,
                   'jeu_200_100_3.txt':29367,
                   'jeu_200_100_4.txt':100838,
                   'jeu_200_100_5.txt':786635,
                   'jeu_200_100_6.txt':41171,
                   'jeu_200_100_7.txt':701094,
                   'jeu_200_100_8.txt':782443,
                   'jeu_200_100_9.txt':628992,
                   'jeu_200_100_10.txt':378442,
                   'jeu_300_25_1.txt':29140,
                   'jeu_300_25_2.txt':281990,
                   'jeu_300_25_3.txt':231075,
                   'jeu_300_25_4.txt':444759,
                   'jeu_300_25_5.txt':14988,
                   'jeu_300_25_6.txt':269782,
                   'jeu_300_25_7.txt':485263,
                   'jeu_300_25_8.txt':9343,
                   'jeu_300_25_9.txt':250761,
                   'jeu_300_25_10.txt':383377,
                   'jeu_300_50_1.txt':513379,
                   'jeu_300_50_2.txt':105543,
                   'jeu_300_50_3.txt':875788,
                   'jeu_300_50_4.txt':307124,
                   'jeu_300_50_5.txt':727820,
                   'jeu_300_50_6.txt':734053,
                   'jeu_300_50_7.txt':43595,
                   'jeu_300_50_8.txt':767977,
                   'jeu_300_50_9.txt':761351,
                   'jeu_300_50_10.txt':996070}

matching = '100_25'

if len(sys.argv)>1:
    matching  = sys.argv[1]

instances = os.listdir(input_dir)

qpk_instance = QKPreader.read('../Data/test/example_input.txt',0)
b = branchAndBound(solver = QKPsolver(qpk_instance.weights, qpk_instance.profits, qpk_instance.maxWeight) )
out = b.run( )
print('../Data/test/example_input.txt' + ', '+ str(out))
