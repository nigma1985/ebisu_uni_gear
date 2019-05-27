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

# for i in df:
#     print(i)
#
# tab_x = pd.pivot_table(df,
#     index='subcategory',
#     columns='segment',
#     values="profit",
#     aggfunc=[np.sum, lambda x: len(x.dropna()) ])
#
# print(tab_x)
#
# for i in tab_x:
#     print(i, tab_x[i])

# old_df = pd.DataFrame(
#     #data = ((1,3,5,7,9), (2,4,6,8,0)),
#     #index = ('A', 'B', 'C', 'D', 'E'),
#     # columns = ('odd', 'even')
#     )
old_df = {
    'odd': (1,3,5,7,9),
    'even': (2,4,6,8,0)
}
print(old_df)

old_df = pd.DataFrame(
    data = old_df,
    index = ('A', 'B', 'C', 'D', 'E')#,
    # columns = ('odd', 'even')
    )

print(old_df)
