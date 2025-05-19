import modelo2 as m
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import odeint
import pandas

lista_L = np.arange(0.5, 40.5, 0.5)

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
    plt.plot(m.tempo,svxs)
    # plt.plot(solx[0], soly[0], 'bo')
plt.grid()
plt.xlabel('tempo')
plt.ylabel('velocidade em x')
plt.show()



colunas = ['t', 'x', 'y', 'vx', 'vy']
data = pandas.read_csv('pendulos novo.csv', names=colunas)

te = data.t.tolist()
xe = data.x.tolist()
ye = data.y.tolist()
vxe = data.vx.tolist()
vye = data.vy.tolist()

plt.title('trajetoria')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.plot(xe, ye, 'mo', label='experimento')
plt.plot


plt.axis('equal')
plt.grid()
plt.show()