from random import randint

class dies:
    
    def __init__(self,num_points=6) :
        self.num_points=num_points

    def roll(self):    
        return randint(1,self.num_points)

