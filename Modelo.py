#Aqui serão definidos os parametros e as funções modelo
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import odeint

#parametros

m = 0
g = 9.8
p = 0
Cd = 0
Area = 0
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