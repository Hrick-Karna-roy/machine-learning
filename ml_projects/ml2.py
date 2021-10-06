import numpy as np
import pandas as pd
import plotly.offline as plo
import plotly.graph_objects as go

np.random.seed(56)
x = np.linspace(0, 1, 100)
y = np.random.randn(100)
trace0 = go.Scatter(x=x, y=y + 5, mode='markers', name='markers')
trace1 = go.Scatter(x=x, y=y, mode='lines', name='line_graph')
trace2 = go.Scatter(x=x, y=y - 5, mode='lines+markers', name='line_graph')
data = [trace0, trace1, trace2]
plo.plot(data)
heart = pd.read_csv("heart.csv")
print(heart)
heart2 = heart[heart['fbs'] == 1]
print(heart2)
zn = [l for col in heart.columns if col.stacortswith('c')]
print(zn)
h2 = heart2[zn]
print(h2)

data = [go.Scatter(x=h2.columns,y=h2.loc[i],mode='lines',name=i) for i in h2.index]
#plo.plot(data)