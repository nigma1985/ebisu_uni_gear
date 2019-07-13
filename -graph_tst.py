import pandas as pd
import numpy as np
import matplotlib
import cufflinks as cf

# # import plotly
# import plotly.plotly as py
# import plotly.graph_objs as go
#
# plotly.tools.set_config_file(world_readable=False,
#                              sharing='private')
#
# data = [go.Bar(
#             x=['giraffes', 'orangutans', 'monkeys'],
#             y=[20, 14, 23]
#     )]
#
# py.iplot(data, filename='basic-bar')

import plotly.offline as py
import plotly.graph_objs as go

trace1 = {'x': [1.5, 2, 3, 4, 5], 'y': [1, 2, 1,  2, 1.5]}
trace2 = {'x': [1, 2.5, 3, 4, 5], 'y': [2, 1, 0, -1, 2  ]}
trace3 = {'x': [1, 2, 3.5, 4, 5], 'y': [3, -1, 0, -1, 4  ]}
trace4 = {'x': [1, 2, 3, 4.5, 5], 'y': [1, 2, 2, 3, 3]}
trace5 = {'x': [1, 2, 3, 4, 5.5], 'y': [3, 2, 1, 3, 3]}

data = [trace1, trace2, trace3, trace4, trace5]
layout = {}

fig = go.Figure (
    data = data, layout = layout
)
plot_url = py.plot(fig, auto_open=True)

print(plot_url)
# py.iplot(fig)

trace = go.Surface (
    colorscale = 'Viridis',
    z = [[ 3,  5,  8, 13, 50, 10],
         [50, 21, 13,  8,  5, 45],
         [-1, -3, -2, -4,  0, 10],
         [10, 25,-10, -5, 10, 33]]
)
data = [trace]
py.plot(data)
