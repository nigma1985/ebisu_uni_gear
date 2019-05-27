import glob, os

from IPython.display import display, HTML
import pandas as pd
import numpy as np
import math

# Using plotly + cufflinks in offline mode

import plotly.offline as py
# import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
cf.set_config_file(offline=True)


from module.connectPostgreSQL import database

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:21255Dohren@localhost:5434/postgres')
df = pd.read_sql_query('SELECT * FROM public.v_superstore;',con=engine)


os.chdir("../ebisu_uni_gear/")

# SELECT
# 	DATE_PART('year', orderdate) AS orderdate,
# 	SUM(profit) AS profit
# FROM
# 	v_superstore
# GROUP BY
# 	DATE_PART('year', orderdate)
# ;


for i in df:
    print(i)

################################################################################

cat_profits = df.groupby(by='category').sum()["profit"]
cat_profits = cat_profits.sort_values(ascending=False)

print(cat_profits.index.values)

data = [go.Bar(
            x=cat_profits.index.values,
            y=cat_profits
    )]

py.plot(data, filename='plotly/cat_profits-basic-bar.html', auto_open=True)

################################################################################

# cat_profits = df.groupby(by=['category','segment']).sum()["profit"]
# cat_profits = df.pivot(index='category', columns='segment', values="profit")
cat_profits = pd.pivot_table(df,
    index='category',
    columns='segment',
    values="profit",
    aggfunc=np.sum)
cat_cnts = pd.pivot_table(df,
    index='category',
    columns='segment',
    values="profit",
    aggfunc=lambda x: len(x.dropna()))

op_max = 0
for cat in cat_cnts:
    for val in cat_cnts[cat]:
        op_max = max(op_max, val)

cat_opacity = cat_cnts
for cat in cat_cnts:
    cat_opacity[cat] = cat_opacity[cat] / op_max

# print(cat_cnts, op_max, cat_opacity)

# for x in cat_cnts:
#     for y in cat_cnts[x]:
#         # print(y, max(x[y]))
#         print(y)
#     print(x, cat_cnts[x], max(cat_cnts[x]))
# cat_profits = cat_profits.sort_values(ascending=False)
##################################################################################
data = [
    go.Bar(
        x=cat_profits.index.values, # assign x as the dataframe column 'x'
        y=cat_profits[col],
        name = col,
        marker=dict(
            opacity=cat_opacity[col]
            )
    ) for col in cat_profits.columns
]

layout = go.Layout(
    barmode='stack',
    title='Stacked Bar with Pandas'
)

fig = go.Figure(data=data, layout=layout)

url = py.plot(fig, filename='plotly/cat_profits-segemnts-bar.html', auto_open=True)
# py.plot(data, filename='plotly/cat_profits-segemnts-bar.html', auto_open=True)

################################################################################

# dt_profits = df.groupby(by='orderdate').sum()["profit"]

dt_profits = pd.pivot_table(df,
    index='orderdate',
    columns='segment',
    values="profit",
    aggfunc=np.sum)
dt_profits = dt_profits.sort_index(ascending=True)
dt_cnts = pd.pivot_table(df,
    index='orderdate',
    columns='segment',
    values="profit",
    aggfunc=lambda x: len(x.dropna()))
dt_cnts = dt_cnts.sort_index(ascending=True)

op_max = 0
for cat in dt_cnts:
    for val in dt_cnts[cat]:
        op_max = max(op_max, val)

dt_opacity = dt_cnts
for cat in dt_cnts:
    dt_opacity[cat] = dt_opacity[cat] / op_max # if dt_opacity[cat] is not pd.np.nan else 0

dt_opacity = dt_opacity.replace({pd.np.nan: 0})

# print(dt_opacity)
#
# print(dt_profits.index.values)

data = [
    go.Scatter(
        x=dt_profits.index.values[0:100], # assign x as the dataframe column 'x'
        y=dt_profits[col],
        mode='lines',
        # mode='marker',
        name = col,
        line=dict(
            opacity=dt_opacity[col]
            )
    ) for col in dt_profits.columns
]

py.plot(data, filename='plotly/dt_profits-lines+markers.html', auto_open=True)
