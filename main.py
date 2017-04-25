from math import exp
from math import pow
import matplotlib.pyplot as plt

temp = 780
v_nagrz = 0.5
Q = 140000
R = 8.3144
temp_K = temp + 273
d0 = 0.000041
D = d0 * exp(-Q/(R * temp_K)) * 1e10
dx = 0.1
dt = 0.001
C_ALFA = (temp - 912)/-240
last = 6
while (D*dt)/pow(dx, 2) > 0.5:
    dt -= 0.001

c1 = []
c2 = []

for i in range(0, 100):
    if i < 6:
        c1.append(0.67)
        c2.append(0)
    else:
        c1.append(0.02)
        c2.append(0.02)

steps = 1000
for i in range(0, steps):
    for j in range(0, last+1):
        if j == 0:
            c2[j] = (1 - 2 * (D * dt / pow(dx, 2))) * c1[j] + (D * dt / pow(dx, 2)) * (c1[j] + c1[j + 1])
        elif j == len(c2) - 1:
            c2[j] = (1 - 2 * (D * dt / pow(dx, 2))) * c1[j] + (D * dt / pow(dx, 2)) * (c1[j - 1] + c1[j])
        else:
            c2[j] = (1 - 2 * (D * dt / pow(dx, 2))) * c1[j] + (D * dt / pow(dx, 2)) * (c1[j - 1] + c1[j + 1])
    for k in range(0, last):
        c1[k] = c2[k]
    if c1[last] >= C_ALFA:
        last += 1
        print(last)

for element in c1:
    print(element)

x = []
total_length = 0
for i in range(0, len(c1)):
    x.append(total_length)
    total_length += dx

plt.plot(x, c1, 'ro')
plt.show()
