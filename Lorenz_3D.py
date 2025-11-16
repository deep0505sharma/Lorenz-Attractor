import matplotlib.pyplot as plt
import numpy as np

def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Calculates the derivatives for the Lorenz system.

    Parameters
    ----------
    xyz : array-like, shape (3,)
        Current state (x, y, z) in three-dimensional space.
    s, r, b : float
        Parameters defining the Lorenz attractor (sigma, rho, beta).

    Returns
    -------
    xyz_dot : array, shape (3,)
        Values of the Lorenz attractor's partial derivatives at *xyz*.
    """
    x, y, z = xyz
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return np.array([x_dot, y_dot, z_dot])

# Parameters for the simulation
dt = 0.01  # Time step
num_steps = 10000  # Number of steps to simulate

# Initialize an array to store the trajectory
xyzs = np.empty((num_steps + 1, 3))

# Set initial values for (x, y, z)
xyzs[0] = (0., 1., 1.05)

# Integrate the Lorenz system using Euler's method
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

# Plotting the Lorenz attractor
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

ax.plot(xyzs[:, 0], xyzs[:, 1], xyzs[:, 2], lw=0.7)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
plt.show()