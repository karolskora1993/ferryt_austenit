from math import exp
from math import pow
import matplotlib.pyplot as plt
import itertools

temp = float(input("Podaj temperaturę: "))
v_heat = float(input("Podaj temperaturę nagrzewania(V=0- stała temperatura): "))
initial_temp = temp;
Q = 140000
R = 8.3144
d0 = 0.000041
dx = 0.1
markers = itertools.cycle((',', '+', '^', '.', 'o', '*', 'h', 'X', 'D', '4', '8', '_'))


def compute_temp(prev_temp, v_heat):
    if v_heat == 0:
        return prev_temp
    else:
        return prev_temp + dt * v_heat


def plot_step(results):
    x = []
    total_length = 0
    for k in range(0, len(results)):
        x.append(total_length)
        total_length += dx
    plt.plot(x, c1, linestyle='solid', marker=next(markers))


def compute_d(temp_c):
    return d0 * exp(-Q/(R * (temp_c + 273))) * 1e10


def compute_c_alfa(temp_c):
    return abs((4.8513 - 0.005776 * temp_c))


def neumann_cond(temp_c, initial_dt, dx):
    dt = initial_dt;
    while (compute_d(temp_c)*dt)/pow(dx, 2) > 0.5:
        dt -= 0.001
    return dt

dt = neumann_cond(temp, 0.001, dx)
c1 = []
ksi = 0

for i in range(0, 100):
    if i < 6:
        c1.append(0.67)
    elif i == 6:
        c1.append(0.02)
        ksi = i
    else:
        c1.append(0.02)

c2 = c1[:]
steps = 10000
plot_steps = steps/5


for i in range(0, steps):
    for j in range(0, ksi+1):
        if j == 0:
            c2[j] = (1 - 2 * (compute_d(temp) * dt / pow(dx, 2))) * c1[j] + (compute_d(temp) * dt / pow(dx, 2)) * (c1[j] + c1[j + 1])
        elif j == ksi:
            c2[j] = (1 - 2 * (compute_d(temp) * dt / pow(dx, 2))) * c1[j] + (compute_d(temp) * dt / pow(dx, 2)) * (c1[j - 1] + c1[j])
        else:
            c2[j] = (1 - 2 * (compute_d(temp) * dt / pow(dx, 2))) * c1[j] + (compute_d(temp) * dt / pow(dx, 2)) * (c1[j - 1] + c1[j + 1])
    if ksi < len(c1) - 2:
        c2[ksi + 1] = c2[ksi]
    if c2[ksi] >= compute_c_alfa(temp) and ksi < len(c2)-2:
        ksi += 1
        print("ksi++")
        c2[ksi] = 0.02
    if i % plot_steps == 0:
        plot_step(c1)
    temp = compute_temp(temp, v_heat)
    c1 = c2[:]

plt.title("Temperatura: {0} prędkość nagrzewania: {1}". format(initial_temp, v_heat))
plt.xlabel("Odległość")
plt.ylabel("Stężenie")
plt.show()

