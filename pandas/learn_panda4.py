import pandas as pd
import matplotlib.pyplot as plt

#index_col=0 parameter specifies that the first column (index 0) in the CSV file should be used as the index of the DataFrame.
#parse_dates=True parameter tells pandas to attempt to parse the index as dates.
air_quality=pd.read_csv('air_quality_no2.csv',index_col=0,parse_dates=True)
print(air_quality.head())

air_quality.plot()
plt.xlabel('Datetime')
plt.show()

air_quality['station_paris'].plot()
plt.xlabel('datetime')
plt.show()

#A scatter plot displays individual data points plotted on a two-dimensional graph.
air_quality.plot.scatter(x='station_london',y='station_paris',alpha=0.5)
plt.xlabel('station_london')
plt.ylabel('staion_paris')
plt.show()

[
    method_Name
    for method_Name in dir(air_quality.plot)
    if not method_Name.startswith("_")
]

air_quality.plot.box()
plt.grid()
plt.show()

axs = air_quality.plot.area(figsize=(12,8), subplots=True)
plt.show()

fig,axs=plt.subplot(figsize=(12,8))
air_quality.plot.area(ax=axs)
plt.xlabel("Dateime")
plt.ylabel("2$_concentration")
fig.savefig("concentration 2$")
plt.show()
