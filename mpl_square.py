import matplotlib.pyplot as plt

square=[1,4,9,16,25]
input_values=[1,2,3,4,5]
plt.plot(input_values,square,linewidth=5)

plt.title("learning matplotlib",fontsize=24)
plt.xlabel("values",fontsize=14)
plt.ylabel("squares values",fontsize=14)

plt.tick_params(axis=("both"),labelsize=14)
plt.show()

