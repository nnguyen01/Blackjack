import blackjack
import numpy
from pylab import *

def run(numEvaluationEpisodes):
    returnSum = 0.0

    for episodeNum in range(numEvaluationEpisodes):
        G = 0 #reward
        R = 0 #return
        S = blackjack.init()
        A = numpy.random.randint(0,2)
        R, S = blackjack.sample(S,0)
        G += R

        # loops until terminal state
        while S != False:
            A = numpy.random.randint(0,2)
            R, S = blackjack.sample(S,A)
            # adds to the return
            G += R
        #print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
    return returnSum / numEvaluationEpisodes
