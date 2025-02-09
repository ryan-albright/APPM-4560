import random
import numpy as np
import matplotlib.pyplot as plt

### Simulation 1 ###
size = 10**6

x = np.array([np.log(random.random()) for _ in range(size)])
y = np.array([np.log(random.random()) for _ in range(size)])

z = x / y

f = lambda x: 1 / (1 + x)**2
x_val = np.linspace(0,10,500)

plt.hist(z,bins = 300, range = (0, 10), density = True)

plt.plot(x_val, f(x_val))
plt.legend(['Theoretical PDF','Randomly Generated Data'])
plt.show()

### Simulation 2 ###
size = 10**4

x = np.array([random.random() for _ in range(size)])
y = np.array([1.88*random.random() for _ in range(size)])

f = lambda x: (30*x**2)*(1-x)**2

pdf_points = [[x_i, y_i] for x_i, y_i in zip(x,y) if y_i <= f(x_i)]

unzipped = zip(*pdf_points)

x_pdf, y_pdf = map(list, unzipped)

plt.plot(x_pdf, y_pdf, 'o')

print(np.average(x_pdf))
plt.show()

### Simulation 3 ###
size = 10**6

u = np.array([random.random() for _ in range(size)])
w = np.array([random.random() for _ in range(size)])

y = 0.5*(1 + np.tanh(2*u - 1))
lamb = np.sqrt(np.abs(y))
x = -np.log(w) / lamb

print(f'E[x] = {np.average(x)}')








