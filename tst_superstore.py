import pandas as pd
import numpy as np
import matplotlib
import cufflinks as cf

from module.connectPostgreSQL import database


# super = database(db_type=None, host='localhost', user='postgres', password='21255Dohren', dbname='postgres')

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:21255Dohren@localhost:5432/postgres')
df = pd.read_sql_query('select * from public.v_superstore;',con=engine)
