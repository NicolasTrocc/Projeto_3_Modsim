import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import odeint

altura = 178
m = 75
g = 9.8
p = 1.2
Cd = 1.05

L = 2
A = 0.965

def modelo3(z, t, m):
    
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
    print(Rx/m, Ry/m)
    dzdt = [dxdt, dydt, dvxdt, dvydt]
    return dzdt