import random
import numpy as np

### Problem 4 Simulation ###
size = 10**6

x = np.array([random.random() for _ in range(size)])
y = np.array([random.random() for _ in range(size)])
z2 = np.array([random.random()**2 for _ in range(size)])

result = sum(z2 > x*y) / size

print(f'P(Z^2 > XY) = {result} for x,y,z all uniformly distributed (0,1) with sample size {size}')

### Problem 5 Simulation ###
size = 10**6

x = np.array([random.random() for _ in range(size)])
y = np.array([random.random() for _ in range(size)])

result = (sum(x**2 + y**2 < 1) * 4) / size

print(f'By calculating P(X^2 + Y^2 < 1), an estimate of pi can be found to be {result} for x,y uniformly distributed (0,1) with sample size {size}')