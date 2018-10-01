# -*- coding: utf-8 -*-
"""
Visualize a simulation log file
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
patch = plt.Circle((0, 0), 0.2, fc='y')

def init():
    patch.center = (0, 0)
    ax.add_patch(patch)
    return patch,

def animate(i):
    x, y = patch.center
    x = 3 * np.sin(np.radians(i))
    y = 3 * np.cos(np.radians(i))
    patch.center = (x, y)
    return patch,

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)

plt.show()
anim.save('animation.gif');