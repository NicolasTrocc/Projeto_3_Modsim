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
#encontra xs mais prox a zero
menor = min(xe)
zeros = []
indices = []
for x in range(len(xe)):
    if xe[x] >= menor and xe[x] <= menor+0.01:
        zeros.append(xe[x])
        indices.append(x)
#calcula velocidades
vel_maxes = []
for i in indices:
    vely = (abs(ye[i]) - abs(ye[i-1]))/(1/30)
    velx = (abs(xe[i]) - abs(xe[i-1]))/(1/30)
    vm = sqrt(velx**2+vely**2)
    vel_maxes.append(vm)

vmax = max(vel_maxes)

# raio = medida/2*pi
m = 0.06
g = 9.8
p = 1.3
Cd = 0.42
A = 0.004
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
vs = []
for v in range(len(vxs)):
    agr = sqrt(vxs[v]**2+vys[v]**2)
    vs.append(agr)

vmas = max(vs)
erro_pct = vmas/(vmax-1)

print (abs(erro_pct))

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
plt.grid()
plt.show()

# print(erro_medio)