import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw=RandomWalk(50000)
    rw.fill_walk()

    plt.figure(dpi=128,figsize=(10,6))

    points_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=points_numbers,s=1,cmap=plt.cm.Reds,edgecolors="none")
    
    #generating the first point
    plt.scatter(0,0,c="green",s=100,edgecolors="none")
    
    #emphasize the last point
    plt.scatter(rw.x_values[-1],rw.y_values[-1],edgecolors="none",c="red",s=100)

    #remove the axis
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    break_point=input("do you want to generate more random walks (y/n)")
    if break_point=="n":
        print("Thanks for generating the random walks")
        break
    else:
        print("Genrate the random walk")