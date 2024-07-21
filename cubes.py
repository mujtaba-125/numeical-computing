#: A number raised to the third power is a cube. Plot the first five 
#cubic numbers, and then plot the first 5000 cubic numbers

# import matplotlib.pyplot as plt

# x=[1,2,3,4,5]
# y=[1,8,27,64,125]

# plt.scatter(x,y,edgecolors="none",c=y,cmap=plt.cm.Reds,s=30)
# plt.title("cubic graph",fontsize=24)
# plt.xlabel("values",fontsize=14)
# plt.ylabel("cubix values",fontsize=14)
# plt.tick_params(axis="both",labelsize=10,color="black")
# plt.axis([0,6,0,150])
# plt.show()

import matplotlib.pyplot as plt
x_values=range(0,50001)
y_values=[x**3 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,edgecolors="none",cmap=plt.cm.Reds)
plt.title("practise question",fontsize=24)
plt.xlabel("values",fontsize=14)
plt.ylabel("cubic values",fontsize=14)
plt.tick_params(axis="both",labelsize=10,color="red")
plt.grid()
plt.axis([0,50001,0,max(y_values)*1.1])
plt.show()