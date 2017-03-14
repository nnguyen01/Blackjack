# Blackjack
Blackjack AI
Blackjack AI using Double-Q learning (Reinforcment learning)

How to run:
Alpha = Step-size 
Epsilon = Exploration
numTrainingEpisodes = The number of runs to simulate

1. Run learn with your desired settings. ' learn(alpha, epsilon, numTrainingEpisodes) '
2. Evaluate your policy. ' Evaluate(numRuns) '
3. Print your policy to a file. ' blackjack.printPolicyToFile(policy) '

Currently the 'best' settings are alpha = 0.0004 and epsilon = 1 with an x amount of training episodes. Obviously the more training the better.
