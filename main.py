from math import exp
from math import pow
import matplotlib.pyplot as plt

temp = 820
v_nagrz = 0.5
Q = 140000
R = 8.3144
temp_K = temp + 273
d0 = 0.000041
D = d0 * exp(-Q/(R * temp_K)) * 1e10
dx = 0.1
dt = 0.001
C_ALFA = (temp - 912)/-240
print(C_ALFA)
ksi = 0
while (D*dt)/pow(dx, 2) > 0.5:
    dt -= 0.001

c1 = []

for i in range(0, 100):
    if i < 6:
        c1.append(0.67)
    elif i == 6:
        c1.append(0.02)
        ksi = i
    else:
        c1.append(0.02)

    c2= c1[:]

steps = 1000
for i in range(0, steps):
    for j in range(0, ksi+1):
        if j == 0:
            c2[j] = (1 - 2 * (D * dt / pow(dx, 2))) * c1[j] + (D * dt / pow(dx, 2)) * (c1[j] + c1[j + 1])
        elif j == ksi:
            c2[j] = (1 - 2 * (D * dt / pow(dx, 2))) * c1[j] + (D * dt / pow(dx, 2)) * (c1[j - 1] + c1[j])
        else:
            c2[j] = (1 - 2 * (D * dt / pow(dx, 2))) * c1[j] + (D * dt / pow(dx, 2)) * (c1[j - 1] + c1[j + 1])
    if ksi < len(c1) -1:
        c2[ksi + 1] = c2[ksi]
    c1 = c2[:]
    if c1[ksi] >= C_ALFA and ksi<len(c1)-1:
        ksi += 1

# for element in c1:
#     print(element)

x = []
total_length = 0
for i in range(0, len(c1)):
    x.append(total_length)
    total_length += dx

plt.plot(x, c1, 'ro')
plt.show()
