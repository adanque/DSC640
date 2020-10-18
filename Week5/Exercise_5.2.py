"""
Author:     Alan Danque
Date:       20201010
Exercise:   5.2
Python Heat maps, Spatial charts and Contour chart
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import matplotlib.cbook
import seaborn as sns
import numpy as np
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

#Step 1:  Load data into the dataframe
costcodf = pd.read_csv(".\\datasets\\costcos-geocoded.csv")
bballdf = pd.read_csv(".\\datasets\\ppg2008.csv", index_col=0)
bballdf.rename(columns={'Name  ':'Name'}, inplace=True)

# Heat maps
sns.heatmap(bballdf, cmap='Blues', linewidths=0.30)
plt.xticks(rotation=90)
plt.xticks(fontsize=7)
plt.xlabel("Statistic", size=16)
plt.ylabel("Basketball Player", size=16)
plt.title("2008 Basketball Player Statistics", size=18)
plt.savefig(".\\plots\\Heat Map Python.png")
plt.show()

# Spatial charts
import folium
import pandas as pd
import webbrowser

#create a map
this_map = folium.Map(prefer_canvas=True)
def plotDot(point):
    folium.CircleMarker(location=[point.Latitude, point.Longitude],
                        radius=2,
                        popup = point.Address + " " + point.City + " " + point.State + " " + point["Zip Code"],
                        fill_color=point.State,
                        fill=True,
                        fill_opacity=0.7,
                        weight=5).add_to(this_map)
    #folium.Marker(
    #    location=[point.Latitude, point.Longitude],
    #    popup=point.Address +" "+ point.City  +" "+ point.State +" "+ point["Zip Code"] ,
    #    tooltip="Click for Costco Address"
    #).add_to(this_map)

#use df.apply(,axis=1) to "iterate" through every row in your dataframe
costcodf.apply(plotDot, axis = 1)
#Set the zoom to the maximum possible
this_map.fit_bounds(this_map.get_bounds())
#Save the map to an HTML file
output_file='C://Users/aland/DSC640/Week5/plots/Spatial Map Python.html'
this_map.save(output_file)
#display(this_map)
webbrowser.open(output_file, new=2)

# contour charts
import numpy as np
in_num = np.nan

Z = bballdf.pivot_table(index='FGA', columns='PTS', values='FGP').T.values
X_unique = np.sort(bballdf.FGA.unique())
Y_unique = np.sort(bballdf.PTS.unique())

X, Y = np.meshgrid(X_unique, Y_unique)
Z[np.isnan(Z)] = 0
pd.DataFrame(Z).round(3)
pd.DataFrame(X).round(3)
pd.DataFrame(Y).round(3)

from IPython.display import set_matplotlib_formats

set_matplotlib_formats('svg')

import matplotlib.pyplot as plt
from matplotlib import rcParams

# Initialize plot objects
rcParams['figure.figsize'] = 5, 5 # sets plot size
fig = plt.figure()
ax = fig.add_subplot(111)

# Generate a contour plot
cp = ax.contourf(X, Y, Z)
ax=plt.gca() #get the current axes
PCM=ax.get_children()[2] #get the mappable, the 1st and the 2nd are the x and y axes
plt.colorbar(PCM, ax=ax)

plt.xticks(rotation=90)
plt.xticks(fontsize=7)
plt.xlabel("Field Goal Attempts", size=8)
plt.ylabel("Field Goal Points", size=8)
plt.title("Contour Plot Basketball FGP based on FGA and PTS", size=10)
plt.savefig(".\\plots\\Contour Plot Python.png")
plt.show()

