import modelo2 as m
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.integrate import odeint

lista_L = np.arange(0.5, 40.5, 0.5)

for L in lista_L:
    result = odeint(m.modelo2,m.z0, m.tempo, args=(L,))
    solx = result[:,0]
    soly = result[:,1]
    svxs = result[:,2]
    svys = result[:,3]
    plt.plot(solx,soly)
    plt.plot(solx[0], soly[0], 'bo')
plt.grid()
plt.xlabel('tempo')
plt.ylabel('velocidade em x')
plt.show()