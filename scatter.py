import matplotlib.pyplot as plt

# x_values=[1,2,3,4,5]
# y_values=[1,4,9,16,25]

# plt.scatter(x_values,y_values,s=50)
# plt.title("scatter plotting",fontsize=24)
# plt.xlabel("x-axis",fontsize=14)
# plt.ylabel("y-axis",fontsize=14)
# plt.tick_params(axis="both",which="major",labelsize=14,color="red")
# plt.show()

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]

plt.scatter(x_values,y_values,edgecolors="none",c=y_values,cmap=plt.cm.Blues,s=40)
plt.title("scatter plotting",fontsize=24)
plt.xlabel("x-axis",fontsize=14)
plt.ylabel("y-axis",fontsize=14)
plt.tick_params(axis="both",which="major",labelsize=14,color="red")
plt.axis([0,1100,0,1100000])
plt.show()
plt.savefig("scatter.png",bbox_inches="tights")