# -*- coding: utf-8 -*-
"""
Visualize a simulation log file
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from logfmt import parse

def strToFTup(s):
    return tuple(float(x) for x in s.split(','))

class LogToAnimation:

    def __init__(self, logpath):
        self.patches = {}
        self.positions = {}
        self.steps = 0
        tpos = {}
        with open(logpath) as f:
            for value in parse(f):
                t = value['tag']
                if t == 'add':
                    if value['shape'] == 'circle':
                        pos = strToFTup(value['pos'])
                        k = value['id']
                        self.patches[k] = plt.Circle(pos, float(value['radius']), fc='y')
                        ax.add_patch(self.patches[k])
                        self.positions[k] = []
                        tpos[k] = pos
                    else:
                        print('Unknown shape ' + value['shape'])
                elif t == 'update':
                    tpos[value['id']] = strToFTup(value['pos'])
                elif t == 'step':
                    for k in self.patches.keys():
                        self.positions[k].append(tpos[k])
                    self.steps = self.steps + 1
                else:
                    print('Unknown tag ' + t)

    def init(self):
        return self.patches.values()

    def animate(self, i):
        ret = []
        for k, v in self.patches.items():
            v.center = self.positions[k][i]
            ret.append(v)
        return ret

# Setup Plot
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))

# Parse Log
loganim = LogToAnimation('test/example.logfmt')

# Animate
anim = animation.FuncAnimation(fig, loganim.animate,
                               init_func=loganim.init,
                               frames=loganim.steps,
                               interval=33.34,
                               blit=True)
anim.save('animation.gif');
