import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('./Fluid/postProcessing/forceCoeffs_object/0/coefficient.dat', comments='#')

fs = 16
fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(10, 8))
ax0.plot(data[:, 0], data[:, 1], label='Cd', lw=4)
# ax0.set_title('Amplitude', fontsize=fs)
ax0.set_xlabel(r'time (s)', fontsize=fs)
ax0.set_ylabel(r'$C_D$', fontsize=fs)
# ax0.legend(fontsize=fs-2,loc=2)
ax0.set_xlim([0, 0.2])
ax0.grid()

ax1.plot(data[:, 0], data[:, 4], label='Cd', lw=4)
# ax0.set_title('Amplitude', fontsize=fs)
ax1.set_xlabel(r'time (s)', fontsize=fs)
ax1.set_ylabel(r'$C_L$', fontsize=fs)
# ax0.legend(fontsize=fs-2,loc=2)
ax1.set_xlim([0, 0.20])
ax1.grid()
