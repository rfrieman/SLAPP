import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib import cm
import math as m
import scipy
from scipy.interpolate import interp1d
from scipy.signal import find_peaks


with open('GS_Stats_columns_RF.csv', 'r') as file:
    data = csv.reader(file)
    data = list(data)
print("This program only runs if the grainsize fractions are cumulative")
zero = 0
Length = 50
Width = 8
font = 40
# ======================================
levels = int(len(data))
#print(levels)
for k in range(0,levels,1):
 # Header   
# data1 = [float(data[i][2]) for i in range(1+k*116,117+k*116,1)]
# gsize = [float(data[i][1]) for i in range(1+k*116,117+k*116,1)]
 # No Header
 depth = [float(data[i][0]) for i in range(0,k,1)]
 mud = [float(data[i][1]) for i in range(0,k,1)]
 finesilt = [float(data[i][2]) for i in range(0,k,1)]
 medsilt = [float(data[i][3]) for i in range(0,k,1)]
 coarsesilt = [float(data[i][4]) for i in range(0,k,1)]
 sand = [float(data[i][5]) for i in range(0,k,1)]
 #print(len(mud))
 

plt.figure(figsize=(Width, Length))
plt.ylim(76, 0)
plt.xlabel("Percent", fontsize=font) #labels for axis
plt.ylabel("Depth (m)", fontsize=font)
plt.xticks(fontsize=font) #font size of axis labels
plt.yticks(fontsize=font)
plt.hlines(depth, zero, mud, colors = 'slategrey')
plt.hlines(depth, mud, finesilt, colors = 'paleturquoise')
plt.hlines(depth, finesilt, medsilt, colors = 'mediumturquoise')
plt.hlines(depth, medsilt, coarsesilt, colors = 'teal')
plt.hlines(depth, coarsesilt, 100, colors = 'indianred')
