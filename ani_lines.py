import sys

import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

from serial import Serial

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} TTY'.format(__file__))
        exit(1)

mbed = Serial(sys.argv[1])
bufs = []
for i in range(12):
    bufs.append([0 for _ in range(100)])


# evenly sampled time at 200ms intervals
fig, ax = plt.subplots()
ax = plt.axes(xlim=(0, 100), ylim=(0, 1))

lines = [ax.plot(buf)[0] for buf in bufs]


def update(values):
    for line, data in zip(lines, values):
        line.set_ydata(data)

def data_gen():
    while True:
        mbed.write('!')
        for buf, val in zip(bufs, mbed.readline().split()):
            del buf[0]
            buf.append(float(val))

        yield bufs

ani = animation.FuncAnimation(fig, update, data_gen, interval=100)

plt.show()
