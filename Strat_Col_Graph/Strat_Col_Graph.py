import pandas as pd
import csv
import matplotlib.pyplot as plt

#Locates data in folder
with open('Units.csv', 'r') as file:
    data = csv.reader(file)
    data = list(data)


length=len(data)

UDepth = [float(data[i][1]) for i in range(1,length,1)]
Unit = [float(data[i][0]) for i in range(1,length,1)]


#Figure size and font variables
Length = 75
Width = 9
font = 40
top = 20
bottom = 80

#Create data frame
Units = pd.DataFrame({'x': Unit,
                     'y': UDepth})

#Create figure, specify size
plt.figure(1, figsize=(Width,Length)) #size of the figure in inches #Actual figure area - changing this without changing the symbol size can introduce weird spacing
plt.rcParams['axes.facecolor'] = 'white' #background color of plot 

#plot line graph
plt.plot(Units.x, Units.y, drawstyle='steps', c='black', label="Units", linewidth = 2)

#Fill line with specific color when a certain length
plt.fill_betweenx(Units.y, 0, 1, where=Units.x <= 1, interpolate = False, color='black')
plt.fill_betweenx(Units.y, 0, 1.5, where=Units.x == 1.5, interpolate = False, color='grey')

#titles and limits
plt.title('Stratigraphy', fontsize=font)
plt.xticks(fontsize=font) #font size of axis labels
plt.yticks(fontsize=font)
plt.xlabel("", fontsize=0) #labels for axis
plt.ylabel("Depth (m)", fontsize=font)
plt.xlim(0,2.5) #limits to axis. Order DOES matter.
plt.ylim(bottom, top)




#Save figure as a pdf
plt.savefig("SLAPP_Strat.pdf")




