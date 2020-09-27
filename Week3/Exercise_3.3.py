"""
Author:     Alan Danque
Date:       20200913
Exercise:   3.2
Python tree map, area charts and stacked area chart
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import matplotlib.pyplot as plt
import squarify # pip install squarify
import pandas as pd
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

#Step 1:  Load data into the dataframe
expdf = pd.read_csv(".\\datasets\\expenditures.txt", sep='\t', lineterminator='\r')

ppgdf = pd.read_csv(".\\datasets\\unemployement-rate-1948-2010.csv")
ppgdf["PERIODVAL"] = ppgdf["Year"].astype(str) + ppgdf['Period'].astype(str).str.replace('M','')
ppgdf["MONTH"] = ppgdf['Period'].astype(str).str.replace('M','')

ppgdfout = ppgdf.groupby('Year')['Value'].sum()
ppgdfout = ppgdfout.to_frame().reset_index()
#ppgdf_sorted = ppgdf.sort_values('G',ascending=True)
#ppgdf_sorted.insert(0, 'ID', range(0, 0 + len(ppgdf_sorted)))

print(ppgdfout)
print("ppgdffiltered50")
ppgdffiltered50 = ppgdfout[ppgdfout["Year"].astype(str).str.contains('195')]["Value"]
ppgdffiltered50 = ppgdffiltered50.reset_index(drop=True)
print(ppgdffiltered50)

ppgdffiltered60 = ppgdfout[ppgdfout["Year"].astype(str).str.contains('196')]["Value"]
ppgdffiltered60 = ppgdffiltered60.reset_index(drop=True)
print(ppgdffiltered60)

ppgdffiltered70 = ppgdfout[ppgdfout["Year"].astype(str).str.contains('197')]["Value"]
ppgdffiltered70 = ppgdffiltered70.reset_index(drop=True)
print(ppgdffiltered70)

ppgdffiltered80 = ppgdfout[ppgdfout["Year"].astype(str).str.contains('198')]["Value"]
ppgdffiltered80 = ppgdffiltered80.reset_index(drop=True)
print(ppgdffiltered80)

ppgdffiltered90 = ppgdfout[ppgdfout["Year"].astype(str).str.contains('199')]["Value"]
ppgdffiltered90 = ppgdffiltered90.reset_index(drop=True)
print(ppgdffiltered90)

ppgdffiltered00 = ppgdfout[ppgdfout["Year"].astype(str).str.contains('200')]["Value"]
ppgdffiltered00 = ppgdffiltered00.reset_index(drop=True)
print(ppgdffiltered00)

tempData    = {"The 50s":ppgdffiltered50,
                "The 60s":ppgdffiltered60,
               "The 70s": ppgdffiltered70,
               "The 80s": ppgdffiltered80,
               "The 90s": ppgdffiltered90,
               "The 2000s": ppgdffiltered00
                };
print(tempData)
generations = ("The 50s", "The 60s", "The 70s", "The 80s", "The 90s", "The 2000s")
dfUnemployementGenerations = pd.DataFrame(tempData) #, index=generations
print(dfUnemployementGenerations)

# tree map
YEAR = ppgdfout["Year"].astype(str)
VALUES = round(ppgdfout["Value"])
squarify.plot(sizes=VALUES, label=YEAR, alpha=0.6 )
plt.title("Unemployment Rates between 1984 to 2010", size=18)
plt.savefig(".\\plots\\Unemployment Rates between 1984 to 2010 Tree Map Python.png")
plt.show()
plt.close()


# area charts
#xtickvals = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth"]
xtickvals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dfUnemployementGenerations.plot(kind='area', stacked=False, xticks=xtickvals)
plt.ylabel("Unemployment Rate by Generational Year")
plt.xlabel("Generational Year Number")
plt.title("Unemployment Rates by Decade", size=18)
plt.savefig(".\\plots\\Unemployment Rates by Decade Area Chart Python.png")
#plt.show(block=True);
plt.show()
plt.close()

#stacked area chart
# Pivot Expenditures DataFrame
print(expdf)
expdfpivot = pd.pivot_table(expdf, values = 'expenditure', index=['year'], columns = 'category').reset_index() #
print("expdfpivot")
print(expdfpivot)

# Index
index = expdfpivot["year"]
print(index)
print(len(index))

# Data  -- convert DataFrame to List of Tuples
data1 = expdfpivot[['Alcoholic Beverages', 'Apparel', 'Cash Contributions', 'Education', 'Entertainment', 'Food', 'Healthcare', 'Housing', 'Miscellaneous', 'Personal Care', 'Personal Insurance', 'Reading', 'Tobacco Products', 'Transportation']].copy()
print(data1)
#data1 = data1.reset_index(drop=True, inplace=True)

records = data1.to_records(index=False)
data = list(records)
#for i in data:
#    print(i)
df1 = pd.DataFrame(data1
                    , columns=['Alcoholic Beverages', 'Apparel', 'Cash Contributions', 'Education', 'Entertainment', 'Food', 'Healthcare', 'Housing', 'Miscellaneous', 'Personal Care', 'Personal Insurance', 'Reading', 'Tobacco Products', 'Transportation']
                   )

# Columns
columns = list(data1.columns.values)

# Draw a stacked area plot
fmt = '$%.0f'
positions = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
#positions = (0,5, 10, 15, 20, 24)
# plt.rcParams.update({'font.size': 12})
ax = df1.plot.area(stacked=True, xticks=positions, rot=90);
ax.yaxis.set_major_formatter(FormatStrFormatter(fmt))
#ax = df1.plot.area(stacked=True, rot=45);
ax.set_xticklabels(index)
plt.xticks(fontsize=8)
plt.ylabel("Year", size=10)
plt.xlabel("Expenditure Amount", size=10)
plt.title("Expenditures by Year", size=18)
ax.legend(bbox_to_anchor=(1.1, 1.05), prop={"size":7})
plt.savefig(".\\plots\\Expenditures by Year Stacked Area Chart Python.png")
plt.show()
plt.close()
