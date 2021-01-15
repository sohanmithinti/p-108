import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv 

count = []
sum = []
for i in range(0, 100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum.append(dice1 + dice2)
    count.append(i)

print(count)    
print(sum)

graph = ff.create_distplot([sum], ["result"])
graph.show()