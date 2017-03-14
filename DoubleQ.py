import blackjack
import numpy as np
from pylab import *

Q1 = 0.00001*rand(181,2)
Q2 = 0.00001*rand(181,2)

def learn(alpha, eps, numTrainingEpisodes):
    returnSum = 0.0
    for episodeNum in range(numTrainingEpisodes):
        S = blackjack.init()
        G = 0
        A = 0
        R, S = blackjack.sample(S,A)
        G += R # ACCOUNTS FOR THE NATURAL (INSTANT WIN OR DRAW)

        # iterate for each step of the episode
        while S:
            if np.random.random() > eps:
                if Q1[S][0] + Q2[S][0] >= Q1[S][1] + Q2[S][1]:
                    A = 0
                    R, nS = blackjack.sample(S,A)
                elif Q1[S][0] + Q2[S][0] < Q1[S][1] + Q2[S][1]:
                    A = 1
                    R, nS = blackjack.sample(S,A)
            else:
                A = np.random.randint(0,2)
                R, nS = blackjack.sample(S,A)
                
            # 0.5 probability of doing Q1 or Q2
            prob = np.random.randint(0,2)
            if not nS:
                if prob == 1:
                    Q1[S][A] = Q1[S][A] + alpha * (R - Q1[S][A])
                else:
                    Q2[S][A] = Q2[S][A] + alpha * (R - Q2[S][A])
            else:
                if prob == 1:
                    Q1[S][A] = Q1[S][A] + alpha * (R + Q2[nS][np.argmax(Q1,1)[nS]] - Q1[S][A])
                else:
                    Q2[S][A] = Q2[S][A] + alpha * (R + Q1[nS][np.argmax(Q2,1)[nS]] - Q2[S][A])
            S = nS
            G += R
        #print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
        if episodeNum % 10000 == 0 and episodeNum != 0:
            blackjack.printPolicy(policy)
            print("Average return so far: ", returnSum / episodeNum)
 
def evaluate(numEvaluationEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEvaluationEpisodes):
        G = 0
        S = blackjack.init()
        A = 0
        R, S = blackjack.sample(S,A)
        G += R
        while S:
            if Q1[S][0] + Q2[S][0] >= Q1[S][1] + Q2[S][1]:
                A = 0
                R, S = blackjack.sample(S,A)
            else:
                A = 1
                R, S = blackjack.sample(S,A)
            G += R
        # Use deterministic policy from Q1 and Q2 to run a number of
        # episodes without updates. Return average return of episodes.
        returnSum = returnSum + G
    return returnSum / numEvaluationEpisodes

def policy(S):
    if Q1[S][0] + Q2[S][0] >= Q1[S][1] + Q2[S][1]:
        return 0
    else:
        return 1

learn(0.0004,1,1000000000)
#print(evaluate(10000000))
#blackjack.printPolicyToFile(policy)
