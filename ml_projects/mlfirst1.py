import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as gg

# x = np.array([[1, 2, 4], [5, 6, 7]])
# print(x)
# data = [93, 90, 86, 76, 65]
# index = ['physics', 'english', 'bio', 'chem', 'maths']
# xx = pd.Series(data, index)
# print(xx)
# q1 = {'india': 1947, 'japan': 1932, 'europe': 1876}
# q2 = {'china': 1832, 'india': 1961, 'japan': 1222}
# country1 = pd.Series(q1)
# country2 = pd.Series(q2)
# print(country1['india'])
# q3 = country1 + country2
# print(q3)
# print(country2.add(country1, fill_value=0))
# dataf = np.random.randint(0, 101, (4, 5))
# print(dataf)
# indexdf = ['rishav', 'rahul', 'rohit', 'sumit']
# col = ['tax', 'date', 'bot', 'nan', 'ol']
# # df = pd.DataFrame(dataf, indexdf, col)
# # print(df)
# df = pd.read_csv('sample_submission1.csv')
# print(df)
# xxx = np.load("b4416884e3.npy")
# print(xxx)
# print(df.info())
# print(df.describe())
# g = np.zeros((5,4))
# print(g)
# h = np.reshape(g,(4,5))
# print(h)

np.random.seed(42)

random_x = sorted(np.random.randint(1, 101, 100))
random_y = sorted(np.random.randint(1, 101, 100))

data = [gg.Scatter(x = random_x, y = random_y, mode='markers',marker=dict(size=12, color = 'rgb(0,255,0)', symbol = 'pentagon', line ={'width': 2}))]
layout = gg.Layout(title = "plot of rand", xaxis=dict(title = "randint_x_axis"),yaxis=dict(title = "randint_y_axis",))
fig = gg.Figure(data=data,layout=layout)
pyo.plot(fig, filename="scatter.html")
