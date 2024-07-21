import matplotlib.pyplot as plt
import numpy as np

from pandas import read_csv
dataframe=read_csv("longley.csv",header=None)
data=dataframe.values
print(data)

x,y=data[:,4],data[:,-1]
plt.figure(figsize=(8,6))
plt.scatter(x,y)
plt.show()

def objective_1(x,a,b):
    return a*x+b

from scipy.optimize import curve_fit

popt,_=curve_fit(objective_1,x,y)
a,b=popt
print('y = {:.5f} * x + {:.5f}'.format(a, b))

plt.figure(figsize=(8,6))
plt.scatter(x,y)
x_line=np.arange(min(x),max(x),0.1)
y_1=objective_1(x_line,a,b)
plt.plot(x_line,y_1,'--')
plt.show()

def objective_2(x,a,b,c):
    return a*x+b*x**2+c

popt,_=curve_fit(objective_2,x,y)
a,b,c=popt
print('y = {:.5f} * x + {:.5f}*x^2+{:.5f}'.format(a, b,c))

plt.figure(figsize=(8,6))
plt.scatter(x,y)
x_line=np.arange(min(x),max(x),0.1)
y_2=objective_2(x_line,a,b,c)
plt.plot(x_line,y_2,'--')
plt.show()

def objective_5(x,a,b,c,d,e,f):
    return a*x+b*x**2+c*x**3+d*x**4+e*x**5+f*x**6

popt,_=curve_fit(objective_5,x,y)
a,b,c,d,e,f=popt

plt.figure(figsize=(8,6))
plt.scatter(x,y)
x_line=np.arange(min(x),max(x),0.1)
y_5=objective_5(x_line,a,b,c,d,e,f)
plt.plot(x_line,y_5,'--')
plt.show()

plt.figure(figsize=(10,8))
plt.scatter(x,y,marker='x',s=80)
x_line=np.arange(min(x),max(x),0.1)
plt.plot(x_line,y_1,'--',label='x')



plt.legend()
plt.show()
