import numpy as np
import matplotlib.pyplot as plt

plot_data = True

# timestep
dt = 0.001

# total time
T = 2.0

# flap law parameters
A = 0.002  # amplitude

freq =  2.0  # frequency in Hz
omega = 2 * np.pi * freq 

cos_cycles = 2  # number of cosine cycles

Tcos = cos_cycles / freq # time for cosine ramp

with open('flap.dat', 'w') as f:
    for curr_t in np.arange(dt, T, dt):
        if curr_t < Tcos:
            scale_factor = 0.5 * (1 - np.cos(np.pi * curr_t / Tcos))
        else:
            scale_factor = 1.0
        
        y = A * scale_factor * np.sin(omega * curr_t)
        f.write(f"{curr_t:.3f} {y:.11f}\n")

print("Data written to flap.dat")


if plot_data:
    plt.figure(figsize=(10, 5))
    data = np.loadtxt('flap.dat')
    time = data[:, 0]
    flap = data[:, 1]   
    plt.plot(time, flap, label='Flap Displacement')
    plt.title('Flap Displacement Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.grid()
    plt.legend()
    plt.show()