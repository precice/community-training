import numpy as np
import matplotlib.pyplot as plt

data_raw = np.genfromtxt('precice-Fluid-convergence.log',skip_header=1)

#print(data_raw)

steps =int(data_raw[-1,0])

data = np.zeros((steps,4))


data[:,0] = np.arange(steps)+1

for jj in range(np.size(data_raw,0)):
    data[int(data_raw[jj,0])-1,2:] = data_raw[jj,2:]
    data[int(data_raw[jj,0])-1,1] = data_raw[jj,1]
    
plt.figure(figsize=(8,5))
plt.subplot(2,1,1)
plt.plot(data[:,0],data[:,2],label='disp')
plt.plot(data[:,0],data[:,3],label='force')
plt.yscale('log')
plt.legend()
plt.grid()
plt.xlabel('time step')
plt.ylabel('convergence')
plt.subplot(2,1,2)
plt.plot(data[:,0],data[:,1])
plt.ylim([0,10])
plt.grid()
plt.xlabel('time step')
plt.ylabel('iterations')
plt.show()
