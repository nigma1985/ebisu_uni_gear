import pandas as pd
import numpy as np

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

import plotly
import plotly.graph_objs as go

plotly.offline.plot({
    "data": [go.Bar(
                x=['giraffes', 'orangutans', 'monkeys'],
                y=[20, 14, 23]
        )],
    "layout": go.Layout(title="hello world")
}, auto_open=True)
