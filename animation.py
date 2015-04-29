import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(100))
ax.set_ylim(0, 1)

from serial import Serial

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} TTY'.format(__file__))
        exit(1)


def update(data):
    line.set_ydata(data)
    return line,

bufs = []
for i in range(6):
    bufs.append([0 for _ in range(100)])

def data_gen():
    while True:
        mbed.write('!')
        line = mbed.readline()
        vals = line.split()
        for i, v in zip(range(12), vals):
            del bufs[i][0]
            bufs[i].append(float(v))

        yield buf


mbed = Serial(sys.argv[1])
ani = animation.FuncAnimation(fig, update, data_gen, interval=10)

plt.show()
