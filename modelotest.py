import numpy as np
from scipy.integrate import odeint
from math import pi, sin, cos, radians, sqrt
import pandas as pd


colunas = ['t', 'x', 'y', 'vx', 'vy']
data = pd.read_csv('pendulos novo.csv', names=colunas)

te = data.t.to_numpy()
xe = data.x.to_numpy()
ye = data.y.to_numpy()
vxe = data.vx.tolist()
vye = data.vy.tolist()

raio = 0.042 / 2
m = 0.021
g = 9.786
p = 1.2
Cd = 0.5
A = pi * (raio**2)
L = 0.232


def modelo(z, t):
    Sx = z[0]
    Sy = z[1]
    vx = z[2]
    vy = z[3]
    v = sqrt(vx**2 + vy**2)
    v2 = v**2

    if v > 0:
        Far = 0.5 * Cd * p * A * v2
        cos_a = -vx / v
        sen_a = -vy / v
    else:
        Far = 0
        cos_a = 0
        sen_a = 0

    sen_0 = Sx / L
    cos_0 = -Sy / L
    P = m * g
    T = (m * v2 / L) + (P * cos_0)

    Rx = Far * cos_a - T * sen_0
    Ry = T * cos_0 - P + Far * sen_a

    dxdt = vx
    dydt = vy
    dvxdt = Rx/m
    dvydt = Ry/m


    return [dxdt, dydt, dvxdt, dvydt]


tempo = te

#CI
x0 = L * sin(radians(60))
y0 = -L * cos(radians(60))
vx0 = 0
vy0 = 0
z0 = [x0, y0, vx0, vy0]


solucao = odeint(modelo, z0, tempo)
xs = solucao[:, 0]  # posição x do modelo

