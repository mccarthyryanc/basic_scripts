#!/usr/bin/env python
#
# Quick script to visualize a correlation matrix
#
# How to use:
#   Pipe in tabbed separated data such that:
#    -each row is an instance/point/dataum
#    -each column is a variable/feature
#
from numpy import corrcoef, transpose, arange
import matplotlib.pyplot as plt
import fileinput

#default plot filename
filename = "corr_matrix_plot"

data = []

# read in data
for line in fileinput.input():
    row = [float(item) for item in line.strip().split("\t")]
    data.append(row)

data_t = transpose(data)
features = len(data_t)
data = None # Clear information in data, just in case it is large

# plot the correlation matrix
fig = plt.figure()
R = corrcoef(data_t)
fig = plt.pcolor(R)
plt.colorbar()
plt.yticks(arange(0.5,float(features)+0.5),range(0,features))
plt.xticks(arange(0.5,float(features)+0.5),range(0,features))

plt.savefig(filename+'.svg', bbox_inches='tight')
