# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:19:54 2024

@author: claudio.caccia
"""

import numpy as np
import matplotlib.pyplot as plt

def naca_4digit(m, p, t, c, n_points=100):
    """
    Generate the coordinates for a NACA 4-digit airfoil.
    m: maximum camber (as fraction of chord)
    p: location of maximum camber (as fraction of chord)
    t: maximum thickness (as fraction of chord)
    c: chord length
    n_points: number of points to generate
    """
    x = np.linspace(0, c, n_points)
    yt = 5 * t * c * (
        0.2969 * np.sqrt(x/c) -
        0.1260 * (x/c) -
        0.3516 * (x/c)**2 +
        0.2843 * (x/c)**3 -
        0.1015 * (x/c)**4
    )
    
    yc = np.where(
        x < p * c,
        m * x / p**2 * (2 * p - x/c),
        m * (c - x) / (1 - p)**2 * (1 + x/c - 2 * p)
    )
    
    dyc_dx = np.where(
        x < p * c,
        2 * m / p**2 * (p - x/c),
        2 * m / (1-p)**2 * (p - x/c)
    )
    
    theta = np.arctan(dyc_dx)
    
    xu = x - yt * np.sin(theta)
    yu = yc + yt * np.cos(theta)
    
    xl = x + yt * np.sin(theta)
    yl = yc - yt * np.cos(theta)
    
    return np.concatenate([xu[::-1], xl]), np.concatenate([yu[::-1], yl])

def compute_properties(x, y):
    """
    Compute the centroid, moments of inertia and product of inertia.
    x, y: coordinates of the airfoil cross-section
    """
    A = 0
    Cx, Cy = 0, 0
    Ix, Iy, Ixy = 0, 0, 0

    n = len(x)
    for i in range(n - 1):
        xi, yi = x[i], y[i]
        xi1, yi1 = x[i + 1], y[i + 1]

        dA = xi * yi1 - xi1 * yi
        A += dA
        Cx += (xi + xi1) * dA
        Cy += (yi + yi1) * dA

        Ix += (yi**2 + yi * yi1 + yi1**2) * dA
        Iy += (xi**2 + xi * xi1 + xi1**2) * dA
        Ixy += (xi * yi1 + 2 * xi * yi + 2 * xi1 * yi1 + xi1 * yi) * dA

    A *= 0.5
    Cx /= (6 * A)
    Cy /= (6 * A)
    Ix /= 12
    Iy /= 12
    Ixy /= 24

    Ix -= A * Cy**2  # Adjust moment of inertia about x-axis to centroid
    Iy -= A * Cx**2  # Adjust moment of inertia about y-axis to centroid
    Ixy -= A * Cx * Cy  # Adjust product of inertia to centroid

    return A, Cx, Cy, Ix, Iy, Ixy

def principal_axes(Ix, Iy, Ixy):
    """
    Calculate the principal moments of inertia and the orientation of the principal axes.
    """
    I_avg = (Ix + Iy) / 2
    R = np.sqrt(((Ix - Iy) / 2)**2 + Ixy**2)
    I1 = I_avg + R
    I2 = I_avg - R

    theta = 0.5 * np.arctan2(2 * Ixy, Ix - Iy)

    return I1, I2, np.degrees(theta)

# NACA 2312 parameters (m = 2%, p = 30%, t = 12%)
m = 0.02
p = 0.3
t = 0.12
chord = 0.1

# Generate airfoil coordinates
x, y = naca_4digit(m, p, t, chord)

# Compute geometric properties
A, Cx, Cy, Ix, Iy, Ixy = compute_properties(x, y)

# Compute principal moments and axes
I1, I2, theta = principal_axes(Ix, Iy, Ixy)

# Output results
print(f"Area: {A:.4e} m^2")
print(f"Centroid: ({Cx:.4e}, {Cy:.4e}) m")
print(f"Moment of Inertia about x-axis (Ix): {Ix:.4e} m^4")
print(f"Moment of Inertia about y-axis (Iy): {Iy:.4e} m^4")
print(f"Product of Inertia (Ixy): {Ixy:.4e} m^4")
print(f"Principal Moment of Inertia I1: {I1:.4e} m^4")
print(f"Principal Moment of Inertia I2: {I2:.4e} m^4")
print(f"Principal Axes Angle (Theta): {theta:.2f} degrees")

rho = 3000
g = 9.81
length = 0.3
E = 2e8


load = rho*g*A
f = load * length**4/(8*E*Ix)

print(load)
print(rho*g*A*length)

print(f"freccia: {f:5e} m")


# Optional: Plot the airfoil
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='NACA 2312 Airfoil')
plt.plot(Cx, Cy, 'ro', label='Centroid')
plt.axis('equal')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.title('NACA 2312 Airfoil')
plt.show()
