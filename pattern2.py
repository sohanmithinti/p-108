import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv 

reader = pd.read_csv("class1.csv")

graph = ff.create_distplot([reader["Marks"].tolist()], ["marks"], show_hist = False)
graph.show()