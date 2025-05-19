import modelo2 as m
import modelo3 as m3
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import odeint
import pandas

lista_L = np.arange(0.5, 40.5, 0.5)
vmax = []
for L in lista_L:

    x0 = L*sin(radians(45))
    y0 = -L*cos(radians(45))
    vx0 = 0
    vy0 = 0
    c0 = [x0,y0,vx0,vy0]
    result = odeint(m.modelo2,c0, m.tempo, args=(L,))
    solx = result[:,0]
    soly = result[:,1]
    svxs = result[:,2]
    svys = result[:,3]
    vmax.append(max(svxs))
    # plt.plot(m.tempo,svxs)
    # plt.plot(solx[0], soly[0], 'bo')
# plt.grid()
# plt.xlabel('tempo')
# plt.ylabel('velocidade em x')
# plt.show()

plt.plot(lista_L,vmax)
plt.ylabel('velocidades máximas')
plt.xlabel('comprimentos')
plt.grid()
plt.show()

lista_m = np.arange(50,330,10)


L = 8
velmax = []
for ma in lista_m:
    x0 = L*sin(radians(45))
    y0 = -L*cos(radians(45))
    vx0 = 0
    vy0 = 0
    c0 = [x0,y0,vx0,vy0]
    result = odeint(m3.modelo3,c0, m.tempo, args=(ma,))
    solx = result[:,0]
    soly = result[:,1]
    svxs = result[:,2]
    svys = result[:,3]
    velmax.append(max(svxs))

print(velmax)
    
plt.plot(lista_m,velmax)
plt.grid()
plt.ylabel('Velocidades máximas')
plt.xlabel('massa')
plt.show()