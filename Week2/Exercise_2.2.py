"""
Author:     Alan Danque
Date:       20200913
Exercise:   2.2
"""


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

#Step 1:  Load data into the dataframe
ppgdf = pd.read_csv(".\\datasets\\ppg2008.csv")
ppgdf_sorted = ppgdf.sort_values('G',ascending=True)
ppgdf_sorted.insert(0, 'ID', range(0, 0 + len(ppgdf_sorted)))
print(ppgdf_sorted)

#Line Chart
ppgdf_sorted.plot(x ='ID', y='G', kind = 'line', color="blue")
plt.legend(["Games Played"]);
plt.xlabel("Player ID", size=15)
plt.ylabel("Games Played", size=15)
plt.title("Number of Games Played by Player ID", size=18)
plt.savefig(".\\plots\\Line Chart Number of Games Played by Player ID Python.png")
plt.show()
plt.close()

#Step Charts
plt.figure()
list_id = ppgdf_sorted['ID'].to_list()
g_id = ppgdf_sorted['G'].to_list()
plt.plot(list_id, g_id, drawstyle='steps', linestyle='-', label='steps-pre aka steps', alpha=1, color="grey")
plt.legend(["Games Played"]);
plt.xlabel("Player ID", size=15)
plt.ylabel("Games Played", size=15)
plt.title("Number of Games Played by Player ID", size=18)
plt.savefig(".\\plots\\Step Chart Number of Games Played by Player ID Python.png")
plt.show()
plt.close()