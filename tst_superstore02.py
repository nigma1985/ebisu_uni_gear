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

dt_profits = df.groupby(by='orderdate').sum()["profit"]
dt_profits = dt_profits.sort_index(ascending=True)

print(dt_profits.index.values)

data = [go.Scatter(
            x=dt_profits.index.values,
            y=dt_profits,
            mode='lines+markers'
    )]

py.plot(data, filename='plotly/dt_profits-lines+markers.html', auto_open=True)
