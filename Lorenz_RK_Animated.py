import numpy as np, matplotlib.pyplot as plt, matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Efficient, notebook-friendly Lorenz animation that also saves a GIF to /tmp
x, y, z  = 0.0, 1.0, 1.05  # initial state
rho, sigma, beta = 28.0, 10.0, 8.0/3.0

t0 = 0.0
tf = 40.0
dt = 0.01
t = np.arange(t0, tf, dt)
n = len(t)

#Functions to compute Lorenz system and do RK4 integration step
def EDOs(r):
    x, y, z = r
    return np.array([sigma*(y - x), rho*x - y - x*z, x*y - beta*z])

def RK4_step(r, dt):
    k1 = EDOs(r)
    k2 = EDOs(r + 0.5*dt*k1)
    k3 = EDOs(r + 0.5*dt*k2)
    k4 = EDOs(r + dt*k3)
    return r + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

r = np.array([x, y, z])
evol = np.zeros((n, 3))
evol[0] = r
for i in range(n - 1):
    evol[i + 1] = RK4_step(evol[i], dt)

# Setup figure and a single Line3D object that we'll update (faster than replotting)
fig = plt.figure('Atrator de Lorenz', facecolor='k', figsize=(6, 5))
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()
line, = ax.plot([], [], [], color='lime', lw=0.9)

# Set static limits from full trajectory so axes don't jump
ax.set_xlim(evol[:,0].min(), evol[:,0].max())
ax.set_ylim(evol[:,1].min(), evol[:,1].max())
ax.set_zlim(evol[:,2].min(), evol[:,2].max())

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return (line,)

# We use a frame-skip so the animation is shorter and faster to render
skip = 6
frames = max(100, n // skip)

def update(frame):
    idx = min(frame * skip, n - 1)
    line.set_data(evol[:idx,0], evol[:idx,1])
    line.set_3d_properties(evol[:idx,2])
    ax.view_init(elev=20, azim=0.2*frame)
    return (line,)

ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=20, repeat=True)

# Try to display inline if running in a notebook; always save a GIF for offline viewing
try:
    from IPython.display import HTML, display
    display(HTML(ani.to_jshtml()))
except Exception as e:
    print('Inline display not available:', e)

# Save a compact GIF to /tmp so you can open it outside the notebook
out_path = '/Users/deepak/Downloads/lorenz_anim.gif'
ani.save(out_path, writer='pillow', fps=30)
print(f'Saved animation to {out_path}')
plt.close(fig)