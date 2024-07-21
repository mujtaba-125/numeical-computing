import pygal 
from die import dies

die_1=dies()
die_2=dies(10)

results=[]

for num in  range(50000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

frequencies=[]

max=die_1.num_points+die_2.num_points

for value in range(2,max+1):
    frequency=results.count(value)
    frequencies.append(frequency) 

hist=pygal.Bar()

hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']

hist._title="rolling two dice 1000 times"
hist.x_labels="result"
hist.y_labels="freqency"

hist.add("D6 + D10",frequencies)
hist.render_to_file('die_visual.svg')