import scipy
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import numpy as np

x=[0,1,2]
y=[1,3,2]
plt.figure(figsize=(10,8))
plt.plot(x, y, 'o', markersize=12)
plt.grid()
plt.title("data points")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

""""the f=1.5"""
f=interp1d(x,y)
y_hat=f(1.5)
print(y_hat)

plt.figure(figsize=(10,8))
plt.plot(x, y, '-o')
plt.plot(1.5,y_hat, 'o', markersize=10)
plt.grid()
plt.title('linear interpolation at x-1.5')
plt.title("data points")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

""""for cubic spcline creating the values from 0 to 2 and the nubmers between them are 100"""
f=CubicSpline(x,y,bc_type='natural')
x_new=np.linspace(0,2,100)
y_new=f(x_new)
print(x_new)
print(y_new)

plt.figure(figsize=(10,8))
plt.plot(x_new,y_new)
plt.plot(x,y,'o',markersize=10)
plt.title('cubic linspace Interpolation')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.figure(figsize=(10,8))
plt.plot(x_new,y_new)
plt.plot(x,y,'o',markersize=10)
plt.plot(1.5,f(1.5),'o',markersize=10)
#plt.plot(1.5,y_hat,'o',markersize=10)
plt.title('cubic spllne interpolation')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
""""for check the difference between the two f1,f2 """
f2=CubicSpline(x,y)
x_new2=np.linspace(0,2,100)
y_new2=f2(x_new2)
print(y_new2)
print(x_new2)
F=f2(1.5)
print(F)

plt.figure(figsize=(10,8))
plt.plot(x_new2,y_new2)
plt.plot(x,y,'o')
plt.plot(1.5,f2(1.5),'o',markersize=10)
plt.plot(x_new,y_new,'--',color='grey')
plt.plot(x_new2,y_new2,'--',color='red')
plt.plot(1.5,f(1.5),'x',markersize=8)
plt.plot(1.5,y_hat,'x',markersize=8)
plt.title('cubic spline(Not a Knot) Interpolation')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()