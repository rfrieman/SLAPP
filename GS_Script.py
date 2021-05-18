import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.image as mpimg


#=========================================================================================================================
#=========================================================================================================================

#File information
with open('GSData.csv', 'r') as file: #Finds .csv file by name in folder script is saved in.
    data = csv.reader(file)
    data = list(data)
length = len(data)

#assigns names to the columns in csv file. 
#[float(data[i][column#]) for i in range(First cell#,length variable assigned above,1)]
xx = [float(data[i][1]) for i in range(1,length,1)]
yy = [float(data[i][0]) for i in range(1,length,1)]
zz = [float(data[i][2]) for i in range(1,length,1)]

#=========================================================================================================================
#=========================================================================================================================

#Figure size variables in inches
Length = 75
Width = 20
font = 40
top = 20
bottom = 78

#Adjust the color scaling for the normalization
maxval = 3
minval = 0.5

#Set the ratio and size of the symbol used for the scatter plot. assigns it the name "verts"
v_val=1 #start at .3 and 2
h_val=4
verts = list(zip([-h_val,h_val,h_val,-h_val],[-v_val,-v_val,v_val,v_val])) #dimentions for the rectangle marker 'verts'

#Assign name and create data frame of the x,y,z using the names assigned to the columns at lines 17-21
data = pd.DataFrame({'x': xx,
                     'y': yy,
                     'z': zz})

#choose the colormap for the graph. Log and normalize the colormap
colormap = plt.get_cmap('coolwarm')
norm = mpl.colors.LogNorm(vmax=maxval, vmin=minval)

#=========================================================================================================================
#=========================================================================================================================

#Plot figure 1, assign its size in inches.
#plt.figure(figure#, figsize=(width#,length#))
plt.figure(1, figsize=(Width, Length))

#Set the color of the background
plt.rcParams['axes.facecolor'] = 'black' 

#Scatter plot
#plt.scatter(dataframename.x, dataframename.y, s=size of symbol, c=dataframename.z, cmap=colormap(see line 49), marker=verts(see line 41), edgecolor=none, norm=norm(see line 50))
scatter = plt.scatter(data.x, data.y, s=85, c=data.z, cmap=colormap, marker=verts, alpha=1, edgecolor="none", norm=norm) #plots grainsize data




plt.title('Grainsize', fontsize=font)
plt.xticks(fontsize=font) #font size of axis labels
plt.yticks(fontsize=font)
plt.xlabel("Grainsize (μm)", fontsize=font) #labels for axis
plt.ylabel("Depth (m)", fontsize=font)
plt.xscale('log') #applites log scale to x axis
plt.xlim(0.1,1000) #limits to axis. Order DOES matter.
plt.ylim(bottom, top)

#=====================================================================



##TO REMOVE ADDITIONAL POINTS FROM PLOT, COMMENT OUT PLT.LEGEND, OR MAKE CLIM NOT INCLUDE 0
##setting the limits manually allowed me to inverse the axis to better represent depth

plt.grid(b=None, which='major', axis='x', color='white') ##Creates gridlines for the x axis
plt.clim(minval, maxval) ##DON'T TOUCH  THIS UNTIL WE KNOW WHAT IT DOES. CHANGE THE COLORS AT TOP MINVAL, MAXVAL
cbar = plt.colorbar(scatter)

plt.savefig("SLAPP_Grainsize.pdf") ##Saves pdf in whatever folder/location the notebook is in
