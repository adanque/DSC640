"""
Author:     Alan Danque
Date:       20200913
Exercise:   4.2
Python scatterplots, bubble charts and density plot charts
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

#Step 1:  Load data into the dataframe
brdf = pd.read_csv(".\\datasets\\birth-rates-yearly.csv")
crdf = pd.read_csv(".\\datasets\\crimerates-by-state-2005.csv")

# scatterplot
brdfout = brdf.groupby('year', sort=False)["rate"].mean().reset_index(name ='rate')
N = brdfout.shape[0]
x = brdfout["year"].astype(int)
y = brdfout["rate"].astype(int)
area = y

plt.scatter(x, y, s=area, c="blue", alpha=0.5)
plt.title("Average Birthday Rates between 1960 to 2008", size=18)
plt.savefig(".\\plots\\Birthday Rates between 1960 to 2008 Scatter Plot Python.png")
plt.show()


# bubble charts
delete_row = crdf[crdf["state"]=="United States"].index
dcrdf = crdf.drop(delete_row)
N = dcrdf.shape[0]
color = dcrdf.index.values.tolist()
plt.scatter('state', 'motor_vehicle_theft',
             s='motor_vehicle_theft',
             c=color,
             alpha=0.5, data=dcrdf)
plt.xticks(rotation=90)
plt.xticks(fontsize=7)
plt.xlabel("State", size=16)
plt.ylabel("Motor vehicle thefts", size=16)
plt.title("Motor Vehicle Theft Rate by US State", size=18)
plt.savefig(".\\plots\\Motor Vehicle Theft Rate by US State Bubble Chart Python.png")
plt.show()


# density plot charts
data = dcrdf["motor_vehicle_theft"]
print(type(data))
print(data)
data.plot.kde()
plt.title("Motor Vehicle Theft Rate Density Plot", size=18)
plt.savefig(".\\plots\\Motor Vehicle Theft Rate Density Plot Python.png")
plt.show()

