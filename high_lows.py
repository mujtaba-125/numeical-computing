from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv #stand for comma separated values

file_name='sitka_weather_2014.csv'# store the name of the file in variable
with open(file_name) as f:
    reader=csv.reader(f)#call the csv.reader to pass the arguement f to create an object 
    header=next(reader)#use the next function that return the next cell in this way the values of the header will be printed
    #print(header)

    #for index,header_column in enumerate(header):#enumrates is the built-in funciton loop the will iterate each valus until the list is completed
        #print(index,header_column)

    highs,dates,lows=[],[],[]

    for row in reader:

        date=datetime.strptime(row[0],'%Y-%m-%d')
        dated=date.strftime('%y-%m-%d')
        dates.append(dated)

        high=int(row[1])
        highs.append(high)

        low=int(row[3])
        lows.append(low)

    # print(highs)
    # print(lows)
    # print(dates) 

# first_time_obj=datetime.strptime('2014-7-1','%Y-%m-%d')

# first_time=first_time_obj.strftime('%y-%m-%d')
# print(first_time)    

fig,ax=plt.figure(dpi=128,figsize=(10,6)),plt.gca()    

plt.plot(highs,c='red')
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)

plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.3)

plt.title("Daily high and low temperature of 2014 ",fontsize=24)
plt.xlabel('',fontsize=14)
fig.autofmt_xdate()

plt.ylabel("Temerature (f)",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=15)

ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-2014')) 
plt.grid()
plt.show()