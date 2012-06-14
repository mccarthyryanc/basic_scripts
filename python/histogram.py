#! /usr/bin/env python
#
# Simple script to make histogram from a single column of piped in data.
# Example:
#   cat data.txt | ./histogram.py <plot_title> <x_axis_label>
#
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import sys, re

# read from stdin
data = []
for line in sys.stdin:
    data.append(float(line.strip()))

# get the file/title/axes names
title = sys.argv[1]
x_axis = sys.argv[2]

filename = re.sub(r'\W+', '_', title)
filename = re.sub(r'_+','_', filename).lower()

#get some quick stats about the data
avg = np.mean(data)
median = np.median(data)

fig = plt.figure()
ax = fig.add_subplot(111)

# the histogram of the data
n, bins, patches = ax.hist(data, 50, normed=1, alpha=0.75)

# plot the stats
avg_text = "mean: %10.3f" % avg
med_text = "median: %10.3f" % median
p1 = plt.axvline(x=avg, color='r', label=avg_text)
p2 = plt.axvline(x=median, color='g', label=med_text)

ax.legend()
ax.set_xlabel(x_axis)
ax.set_ylabel('Frequency')
ax.set_title(title)
ax.set_xlim(min(data), max(data))
ax.set_ylim(0, max(n))
ax.grid(True)

fig.savefig(filename+'.png', bbox_inches='tight')
