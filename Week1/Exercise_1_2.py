"""
Author:     Alan Danque
Date:       20200902
Exercise:   1.2
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

def func(pct, allvalues):
    absolute = int(pct / 100. * np.sum(allvalues))
    return "{:.1f}%\n({:d})".format(pct, absolute)

#Step 1:  Load data into the dataframe
adf = pd.read_csv(".\\datasets\\airline-safety.csv")
adf_sorted = adf.sort_values('fatalities_85_99',ascending=False)

hddf = pd.read_excel('.\\datasets\\hotdog-contest-winners.xlsm', sheet_name='hot-dog-contest-winners')
hddf_sorted = hddf.sort_values('Dogs eaten',ascending=False)

oadf = pd.read_excel('.\\datasets\\obama-approval-ratings.xls', sheet_name='Sheet1')
oadf_sorted = oadf.sort_values('Approve',ascending=False)

"""
# Airline Safety
plt.figure(figsize=(10,6))
# bar plot with matplotlib
plt.bar('airline', 'fatalities_85_99',data=adf_sorted)
plt.xticks(rotation=90)
plt.xlabel("Airline", size=15)
plt.ylabel("Fatalities", size=15)
plt.title("Number of Airline Fatalities Between 85-99", size=18)
plt.savefig(".\\plots\\Airline Fatalities bar chart.png")
plt.show()

# Hot Dog Contests
plt.figure(figsize=(10,6))
# bar plot with matplotlib
plt.bar('Country', 'Dogs eaten',data=hddf_sorted)
plt.xticks(rotation=90)
plt.xlabel("Country", size=15)
plt.ylabel("Number of Eaten Hot Dogs", size=15)
plt.title("Highest Number of Hot Dog Contests By Country", size=18)
plt.savefig(".\\plots\\Highest Number of Hot Dog Contest By Country.png")
plt.show()
"""
######### Bar Chart
# Obama Approval Ratings
plt.figure(figsize=(10,6))
plt.bar('Issue', 'Approve',data=oadf_sorted)
plt.xticks(rotation=90)
plt.xlabel("Issue", size=15)
plt.ylabel("Approval Ratings", size=15)
plt.title("Obama Approval Rating by Issue", size=18)
plt.savefig(".\\plots\\Obama Approval Rating by Issue Bar Chart.png")
plt.show()


######### Stacked Bar Chart
# Obama Approval Ratings
fig = plt.figure()
labels=oadf_sorted['Issue']
oadf_sorted.index = oadf_sorted[['Issue']]
oadf_sorted[['Approve','Disapprove','None']].plot(kind='bar', stacked=True, rot=90, alpha=0.8, legend=True, label=labels)
plt.xticks(rotation=90)
plt.xlabel("Issue", size=15)
plt.ylabel("Approval Ratings", size=15)
plt.title("Obama Approval Rating by Issue", size=18)
plt.savefig(".\\plots\\Obama Approval Rating by Issue Stacked Bar Chart.png")
plt.show()


######### Pie Chart
labels = oadf_sorted['Issue']
explode = oadf_sorted[['Approve']]
fig = plt.figure(figsize=(10, 7))
plt.pie(explode, autopct = lambda pct: func(pct, explode), labels=labels)
plt.title("Obama Approval Rating by Issue", size=18)
plt.savefig(".\\plots\\Obama Approval Rating by Issue Stacked Pie Chart.png")
plt.show()


######### Donut Chart
labels = oadf_sorted['Issue']
explode = oadf_sorted[['Approve']]
fig = plt.figure(figsize=(10, 7))
plt.pie(explode, autopct = lambda pct: func(pct, explode), labels=labels)
plt.title("Obama Approval Rating by Issue", size=18)
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.savefig(".\\plots\\Obama Approval Rating by Issue Stacked Donut Chart.png")
plt.show()
