#! /usr/bin/env python
#
# Simple script to make 3D Scatter plot from piped in data.
# Example:
#   cat data.tsv | ./histogram.py <plot_title> <x_axis_label> <y_axis_label> <z_axis_label>
#
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from mpl_toolkits.mplot3d import Axes3D
import sys, re, time

# read from stdin
x = []
y = []
z = []
color = []
for line in sys.stdin:
    temp = line.strip().split("\t")
    if len(temp) == 3:
        x.append(float(temp[0]))
        y.append(float(temp[1]))
        z.append(float(temp[2]))
    elif len(temp) == 4:
        x.append(float(temp[0]))
        y.append(float(temp[1]))
        z.append(float(temp[2]))
        color.append(float(temp[3]))

# get the file/title/axes names
title = sys.argv[1]
x_axis = sys.argv[2]
y_axis = sys.argv[3]
z_axis = sys.argv[4]

filename = re.sub(r'\W+', '_', title)
filename = re.sub(r'_+','_', filename).lower()


fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')

if len(temp) == 3:
    sc = ax.scatter(x, y, z, c=z)
elif len(temp) == 4:
    sc = ax.scatter(x, y, z, c=color)

plt.colorbar(sc)
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.set_zlabel(z_axis)
ax.set_title(title)

fig.savefig(filename+'.png', bbox_inches='tight')
