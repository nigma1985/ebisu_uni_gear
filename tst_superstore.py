import plotly.plotly as py
import cufflinks as cf
cf.go_offline(connected=True)
import pandas as pd
import numpy as np
print (cf.__version__)
# import matplotlib

from module.connectPostgreSQL import database


# super = database(db_type=None, host='localhost', user='postgres', password='21255Dohren', dbname='postgres')

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:21255Dohren@localhost:5434/postgres')
# df = pd.read_sql_query('SELECT version();',con=engine)
df = pd.read_sql_query('SELECT * FROM public.v_superstore;',con=engine)

for i in df:
    print(i)
#
# py.iplot([{
#     'x': df.index,
#     'y': df[col],
#     'name': col
# }  for col in df.columns], filename='cufflinks/simple-line')

super = df.groupby('orderdate').profit.agg('sum')

print(super, type(super+))
# for i in super:
#     print(i)

#
# py.iplot([{
#     'x': super.index,
#     'y': super[col],
#     'name': col
# }  for col in super.column], filename='cufflinks/simple-line')
# super.iplot(
#     kind='scatter',
#     mode='lines+markers',
#     x='orderdate',
#     # title='Events over Time',
#     y='profit',
#     # margin={'l':450}
#     )
