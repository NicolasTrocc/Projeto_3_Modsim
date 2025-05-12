#Aqui serão definidos os parametros e as funções modelo
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import odeint

#parametros

m = 75
g = 9.8
p = 1.2
Cd = 1.05
Area = 0.965
L = 1

#modelo
def modelo(x, t):
    
    Sx = x[0]
    Sy = x[1]
    vx = x[2]
    vy = x[3]
    v = ((vx**2) + (vy**2))**(1/2)

    Far = (1/2)*Cd*p*Area*(v**2)
    cos_0 = (vx/v)
    sen_0 = (vy/v)
    P = m*g

    T = ((m*(v**2)/L) + (P*cos_0))
    
    Rx = -(Far*cos_0) + (T*sen_0)
    Ry = (T*cos_0) - P + (Far*sen_0)

    dxdt = vx
    dydt = vy
    dvxdt = Rx/m
    dvydt = Ry/m
    
    return [dxdt, dydt, dvxdt, dvydt]

#implementar
tempo = np.arange(0, 5, 1e-3)
CI = []
x0 = 30
y0 = 0
vx0 = 0
vy0 = 0
z0 = [x0,y0,vx0,vy0]

solucao = odeint(modelo, z0, tempo)
xs = solucao[:,0]
ys = solucao[:,1]
vxs = solucao[:,2]
vys = solucao[:,3]

plt.plot(xs,ys)
plt.xlabel('posições em X')
plt.ylabel('posições em Y')
plt.grid()
plt.show()