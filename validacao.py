#validacao
import matplotlib.pyplot as plt
import pandas
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
plt.axis('equal')
plt.grid()
plt.show()


plt.plot(te, xe, 'mo', label='experimento')
plt.grid()
plt.show()

