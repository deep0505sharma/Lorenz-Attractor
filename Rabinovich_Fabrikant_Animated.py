import numpy as np, matplotlib.pyplot as plt, matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Rabinovich-Fabrikant attractor animation (RK4 integration + GIF save)
# Parameters and initial condition
x0, y0, z0 = 0.1, 0.0, 0.1
alpha = 0.14
gamma = 0.1

# Time settings
t0 = 0.0
tf = 60.0
dt = 0.01
t = np.arange(t0, tf, dt)
n = len(t)

# RF system RHS and RK4 step
def EDOs(r):
    x, y, z = r
    dx = y * (z - 1 + x*x) + gamma * x
    dy = x * (3*z + 1 - x*x) + gamma * y
    dz = -2.0 * z * (alpha + x * y)
    return np.array([dx, dy, dz])

def RK4_step(r, dt):
    k1 = EDOs(r)
    k2 = EDOs(r + 0.5*dt*k1)
    k3 = EDOs(r + 0.5*dt*k2)
    k4 = EDOs(r + dt*k3)
    return r + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

# Integrate
r = np.array([x0, y0, z0], dtype=float)
evol = np.zeros((n, 3), dtype=float)
evol[0] = r
for i in range(n - 1):
    r_next = RK4_step(evol[i], dt)
    # simple divergence safeguard
    if not np.isfinite(r_next).all() or np.any(np.abs(r_next) > 1e6):
        evol = evol[:i+1]
        n = evol.shape[0]
        t = t[:n]
        print(f"Integration stopped at step {i} due to divergence/NaN.")
        break
    evol[i + 1] = r_next

# Setup figure and single Line3D for speed
fig = plt.figure('Rabinovich-Fabrikant', facecolor='k', figsize=(6,5))
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()
line, = ax.plot([], [], [], color='cyan', lw=0.8)

# static axis limits so view doesn't jump
ax.set_xlim(evol[:,0].min(), evol[:,0].max())
ax.set_ylim(evol[:,1].min(), evol[:,1].max())
ax.set_zlim(evol[:,2].min(), evol[:,2].max())

# init function for animation
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return (line,)

# frame skipping to speed up animation
skip = 12
frames = max(130, n // skip)

def update(frame):
    idx = min(frame * skip, n - 1)
    line.set_data(evol[:idx,0], evol[:idx,1])
    line.set_3d_properties(evol[:idx,2])
    ax.view_init(elev=20, azim=0.3*frame)
    return (line,)

ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=20, repeat=True)

# try inline display (notebook), otherwise save a GIF
try:
    from IPython.display import HTML, display
    display(HTML(ani.to_jshtml()))
except Exception as e:
    print('Inline display not available:', e)

out_path = '/Users/deepak/Downloads/rf_anim.gif'
ani.save(out_path, writer='pillow', fps=30)
print(f'Saved RF animation to {out_path}')
plt.close(fig)
