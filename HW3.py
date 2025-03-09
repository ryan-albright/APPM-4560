import random
import numpy as np
import matplotlib.pyplot as plt

### Simulation 1 ###
size = 10**6

# Simulation of Cauchy
u1 = np.array([random.random() for _ in range(size)])
y = np.tan(np.pi*(u1 - 0.5))

# Simulation of Normal
c = np.sqrt(2*np.pi / np.e)
f = lambda x: (1 / np.sqrt(2* np.pi))*np.exp(-0.5*x**2)
g = lambda x: 1 / (np.pi*(1 + x**2))
u2 = np.array([random.random() for _ in range(size)])

pdf_points = [y_i for y_i, u_i in zip(y, u2) if u_i <= f(y_i) / (c*g(y_i))]
plt.hist(pdf_points, bins=500, range = (-5,5), density=True, label="Simulated Normal")

x_vals = np.linspace(-5, 5, 1000)
plt.plot(x_vals, f(x_vals), 'r', label="Standard Normal PDF")
plt.legend()

plt.show()

### Question 7 ###
p = np.array([[1, 0, 0, 0, 0],
              [0.25, 0, 0.75, 0, 0],
              [0, 0.25, 0, 0.75, 0],
              [0, 0, 0.25, 0, 0.75],
              [0, 0, 0, 0, 1]])

print(f'P(Xn = 1 | X0 = 3) = p[3,1] = {np.linalg.matrix_power(p, 40)[2,0]:2f}')



