import numpy as np

# Problem 3
p = np.array([[0.75, 0.25], [0.08, 0.92]])
q = np.array([0.7, 0.3])

print(f'In 1998, the percent of smokers was {(q @ np.linalg.matrix_power(p, 3))[0]:3f}%')
print(f'In 2005, the percent of smokers was {(q @ np.linalg.matrix_power(p, 10))[0]:3f}%')
print(f'In the long term, the percent of smokers is {(q @ np.linalg.matrix_power(p, 30))[0]:3f}%')

# Problem 4
p = np.array([[0.98, 0.02, 0], [0, 0.95, 0.05], [1, 0, 0]])
q = np.array([1, 0, 0])

print(f'In the long term, the percent of time that only one light bulb functions is {(q @ np.linalg.matrix_power(p, 250))[1]:2f}%')

