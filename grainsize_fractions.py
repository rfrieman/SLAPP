import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib import cm
import math as m
import scipy
from scipy.interpolate import interp1d
from scipy.signal import find_peaks

#================================================================================================================================
#================================================================================================================================
#load in data file
with open('GS_Stats_columns_RF.csv', 'r') as file:
    data = csv.reader(file)
    data = list(data)
#This program only runs if the grainsize fractions are cumulative.

zero = 0
Length = 50
Width = 8
font = 40
# ======================================
levels = int(len(data))

for k in range(0,levels,1):

#assign variables to the columns
depth = [float(data[i][0]) for i in range(0,k,1)]
mud = [float(data[i][1]) for i in range(0,k,1)]
finesilt = [float(data[i][2]) for i in range(0,k,1)]
medsilt = [float(data[i][3]) for i in range(0,k,1)]
coarsesilt = [float(data[i][4]) for i in range(0,k,1)]
sand = [float(data[i][5]) for i in range(0,k,1)]

 
#================================================================================================================================
#================================================================================================================================
#plot the horizontal lines for the different grain sizes.
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


plt.savefig("SLAPP_Fractions.pdf")#Saves file as a pdf in folder the script is in.
