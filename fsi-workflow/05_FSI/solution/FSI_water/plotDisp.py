# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:10:07 2024

@author: claudio.caccia
"""

import numpy as np
import matplotlib.pyplot as plt

# Load data from the log files
data_tip = np.genfromtxt("./Solid/precice-Solid-watchpoint-tip.log", skip_header=1)
data_te = np.genfromtxt("./Solid/precice-Solid-watchpoint-tip-trailing.log", skip_header=1)
data_le = np.genfromtxt("./Solid/precice-Solid-watchpoint-tip-leading.log", skip_header=1)

# Extract time (column 1) and Y-displacement (column 6)
time_tip = data_tip[:, 0]
displacement_tip = data_tip[:, 5]

time_te = data_te[:, 0]
displacement_te = data_te[:, 5]

time_le = data_le[:, 0]
displacement_le = data_le[:, 5]

# Create the plot
plt.figure(figsize=(10,7))
plt.grid(True)

# Set title and labels
plt.title('Displacement of the Wing Tip')
plt.xlabel('time (s)')
plt.ylabel('Y-Displacement (m)')

plt.xlim([0,0.2])

# Plot the data
plt.plot(time_tip, displacement_tip, label="tip", linestyle='-', color='b')
plt.plot(time_te, displacement_te, label="tip TE", linestyle='-', color='r')
plt.plot(time_le, displacement_le, label="tip LE", linestyle='-', color='g')

# Show legend
plt.legend()

# Display the plot
plt.show()
