"""
Author:     Alan Danque
Date:       20201029
Heat maps for aviation dataset
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
aviationdf = pd.read_csv(".\\datasets\\AviationDataSupplement_baaa-acro.csv", index_col=0)

# Cleanup: update any isnan to 0
avdf = aviationdf.fillna(0)
# review isnans
#print(avdf.isnull().values.any())
avdf.columns = [c.lower().replace(' ', '_') for c in avdf.columns]
#print(avdf.columns)

# Create Dataframe only containing only the specific planes
avnewdf = avdf[['type_of_aircraft','crew_on_board', 'crew_fatalities', 'pax_on_board', 'pax_fatalities', 'other_fatalities', 'total_fatalities', 'planeage', 'survivors']].copy()
avnewdf['has_survivor'] = np.where(avnewdf['survivors']!= 'Yes', 1, 0)
del avnewdf['survivors']
planetypes = ['Boeing 737-200','Boeing 737-300','Boeing 737-400','Boeing 737-500','Boeing 737-800','Boeing 757-200','Boeing 777-200','Boeing 777-300','Boeing KC-135 Stratotanker','Boeing KC-137 Stratoliner']
avndf = avnewdf[avnewdf['type_of_aircraft'].isin(planetypes)]
#print(avndf.head(10))

# Create Aggregated Counts Dataframe
av = avndf.groupby('type_of_aircraft')['type_of_aircraft'].count().to_frame(name='crash_counts')
#av.columns = av.columns.droplevel(0)
#print(av.info)
av = av.reset_index(drop=False)
av.rename(columns={'type_of_aircraft':'type_of_aircraft_right'}, inplace=True)
avnoutdf = avndf.groupby(['type_of_aircraft'])['crew_on_board', 'crew_fatalities', 'pax_on_board', 'pax_fatalities', 'other_fatalities', 'total_fatalities', 'planeage', 'has_survivor'].apply(lambda x : x.astype(int).sum())
avnoutdf = avnoutdf.reset_index(drop=False)
avnoutdf.rename(columns={'type_of_aircraft':'type_of_aircraft_left'}, inplace=True)

# Combine Dataframes
avcomplete = pd.merge(avnoutdf, av, left_on='type_of_aircraft_left', right_on='type_of_aircraft_right', how='inner')#.drop('id1', axis=1))
avcomplete.rename(columns={'type_of_aircraft_left':'type_of_aircraft'}, inplace=True)
del avcomplete['type_of_aircraft_right']

# Review Dataframe
print(avcomplete)
for col in avcomplete.columns:
    print(col)

"""
avnoutdf = avndf.groupby(['type_of_aircraft']).agg(
     sum_crew_on_board = ('crew_on_board','sum'),
     sum_crew_fatalities = ('crew_fatalities','sum'),
 ).reset_index()
"""

# Reset dataframe index to the label
avcomplete.set_index('type_of_aircraft', inplace=True)

# Heat maps
sns.heatmap(avcomplete, cmap='Blues', linewidths=0.30)
plt.xticks(rotation=90)
plt.xticks(fontsize=7)
plt.xlabel("Metric", size=16)
plt.ylabel("Type of Air Craft", size=16)
plt.title("Heat Map Analysis on all \nFictious Airways Air Craft", size=18)
plt.savefig(".\\plots\\Heat Map AviationData.png")
plt.show()


