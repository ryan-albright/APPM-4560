import numpy as np
import pandas as pd
import scipy.sparse.linalg as sla
import random 
import matplotlib.pyplot as plt

# Part (b)

alpha = 0.1
p = lambda i: i*0 + alpha
q = lambda i: 2*alpha*(i/10)**3

# Creating p matrix
p1 = np.diag([1 - p(1)] + [1- p(i) - q(i) for i in range(2, 10)] + [1 - q(10)])
p2 = np.diag([p(i) for i in range(1,10)], 1)
p3 = np.diag([q(i) for i in range(2,11)], -1)

p_m = p1 + p2 + p3

# Finding eigenvector corresponding to an eigenvalue of  1
D, V = sla.eigs(p_m.T, 1)

# Normalized V and redefined it to be pi
pi = V / sum(V)

print(f'The eigenvector corresponding to an eigenvalue of 1 is \n {pi}')

# Part (c) Simulation of the Markov Chain

# Selecting starting state
x = random.randint(1, 10)

state_count = np.zeros(10)
state_count[x - 1] += 1

for i in range(10**6):

    y = random.random()

    if x == 1: # State 1 case has only 2 possibilities
        if y < alpha:
            x = 2
    elif x == 10: # State 10 case has only 2 possibilities
        if y < 2*alpha:
            x = 9
    else: # Middle case has 3 possibilities
        p_x = p(x)
        q_x = q(x)
        if y < q_x:
            x -= 1
        elif y < q_x + p_x:
            x += 1
    state_count[x - 1] += 1

# Plotting the results
x = [i for i in range(1,11)]
plt.bar(x,state_count/ 10**6, label = 'Simulated Distribution')
plt.plot(x, pi, 'or', label = 'Theoretical Distribution')
plt.legend()
plt.show()
    

