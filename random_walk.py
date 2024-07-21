#random is the module built in the python that generate the random number and perform random operation and 
# choice is the module present in the random that return the randomly selected element from a non empty sequence
from random import choice

""""A class to generate the random walk"""
class RandomWalk():

    """"initialize the function that generate the points start with 0"""
    def __init__(self,num_points=5000) :
        #set the random walk points (default) i.e:5000
        self.num_points=num_points

        """" These are the points that initialize the value of x and y start from zero"""
        self.x_values=[0]
        self.y_values=[0]


    def fill_walk(self):
        #The whiel loop continue until the length of xvalues is reaches the num_points 
        while len(self.x_values)<self.num_points:


            x_direction=choice([1,-1])#randomly choose the direction one for right and one for left
            x_distance=choice([0,1,2,3,4])#randomly choose the distance move from the x axis
            x_step=x_direction*x_distance#calculate the step in the x direction

            
            y_direction=choice([1,-1])#randomly choose the direction one for the up and one for the down
            y_distance=choice([0,1,2,3,4])#randomly choose the distance move on the y axis
            y_step=y_direction*y_distance#calculate the step in the y direction

            #if both step are zero the stop the iteration
            if x_step==0 and y_step==0:
                continue
            #the highest point of x + the step to take in the x direction
            net_x=self.x_values[-1]+x_step
            #the highest point of y + the step to take in the y direction
            net_y=self.y_values[-1]+y_step

            self.x_values.append(net_x)
            self.y_values.append(net_y)