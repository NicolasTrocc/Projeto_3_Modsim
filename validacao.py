#validacao
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pandas
colunas = ['t', 'x', 'y', 'vx', 'vy']
data = pandas.read_csv('pendulos novo.csv', names=colunas)

te = data.t.tolist()
xe = data.x.tolist()
ye = data.y.tolist()
vxe = data.vx.tolist()
vye = data.vy.tolist()

raio = 0.042/2
m = 0.021
g = 9.786
p = 1.2
Cd = 0.5
A = pi * (raio**2) 
L = 0.232

#modelo
def modelo(z, t):
    
    Sx = z[0]
    Sy = z[1]
    vx = z[2]
    vy = z[3]
    v = ((vx**2) + (vy**2))**(1/2)
    v2 = v**2
    if v > 0:
        Far = (Cd*p*A*(v2))/2
        cos_a = (-vx/v)
        sen_a = (-vy/v)
            
    else:
        Far = 0
        cos_a = 0
        sen_a = 0
        
    
    sen_0 = (Sx/L)
    cos_0 = (-Sy/L)
    P = m*g
    
    T = ((m*(v2)/L) + (P*cos_0))
    
    Rx = Far*cos_a - T*sen_0
    Ry = T*cos_0 - P + Far*sen_a

    dxdt = vx
    dydt = vy
    dvxdt = Rx/m
    dvydt = Ry/m
    dzdt = [dxdt, dydt, dvxdt, dvydt]
    return dzdt

#implementar
tempo = np.arange(10.5, 26, 1e-3)
x0 = L*sin(radians(60))
y0 = -L*cos(radians(60))
vx0 = 0
vy0 = 0
z0 = [x0,y0,vx0,vy0]

solucao = odeint(modelo, z0, tempo)
xs = solucao[:,0]
ys = solucao[:,1]
vxs = solucao[:,2]
vys = solucao[:,3]

plt.plot(xs,ys)
# plt.plot(xs[0],ys[0],'ro')
plt.title('trajetoria')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.plot(xe, ye, 'mo', label='experimento')
plt.axis('equal')
plt.grid()
plt.show()

plt.plot(te, xe, 'mo', label='experimento')
plt.plot(tempo, xs)
plt.xlabel('tempo [s]')
plt.ylabel('posição x [m]')
plt.grid()
plt.show()

solucao_temp = odeint(modelo, z0, te)


