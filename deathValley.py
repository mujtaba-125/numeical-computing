from datetime import datetime
import matplotlib.dates as mdate
import matplotlib.pyplot as plt
import csv

with open('death_valley_2014.csv') as f:
    reader=csv.reader(f)
    header=next(reader)

    highs,lows,dates=[],[],[]
    for row in reader:

        try:
            high=int(row[1])
            
            date=datetime.strptime(row[0],'%Y-%m-%d')
            dated=date.strftime('%y-%m-%d')
            
            low=int(row[3])

        except ValueError:
            print("current value is missing")

        else:
            dates.append(dated)
            highs.append(high)
            lows.append(low)    

fig,ax=plt.figure(dpi=128,figsize=(10,6)),plt.gca()
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)

plt.fill_between(dates,lows,highs,facecolor='blue',alpha=0.3)

plt.title('Daily High and low temperature of death valley,2014',fontsize=24)


plt.xlabel('',fontsize=14)
fig.autofmt_xdate()

ax.xaxis.set_major_locator(mdate.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdate.DateFormatter('%d-%b-2014'))

plt.ylabel('Temperature in farhenite',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=15)

plt.grid()

plt.show()