import glob, os, sys, psycopg2
from zipfile import ZipFile
from pathlib import Path
from psycopg2 import Error

from module.connectPostgreSQL import database, dict2sql, getQuery
from module.import_tankerkoenig import tankerkoenig2sql
from module import json2py, py2json

# import module.files as fls

from datetime import datetime
from datetime import timedelta
import time

from random import sample, randint, random
start_time = time.mktime(datetime.now().timetuple())

# os.chdir("/home/pi/ebisu_uni_gear/")
os.chdir("../ebisu_uni_gear/")

details = '../details.json'
details = json2py(details)

print('details', details)
postgres = []
for d in details:
    try:
        if d['provider'] == 'PostgreSQL' and d['host'] == 'localhost':
            postgres.append(d)
        else:
            pass
    except:
        pass

if len(postgres) > 0:
    postgres = postgres[1]
else:
    pass

################################################################################


def newRow(database = None, schema_name = 'public', table_name = None, listNames = [], listValues = [], listWhere = [], listTypes = [], getID = True):
    ## variables
    id = None
    table = table_name.lower()
    # print(table_name, table_name.lower(), table)
    schema = schema_name.lower()

    names = []
    values = []
    where = {}
    for i in range( len(listValues) ):
        if str(listValues[i]).lower() not in (None, '', 'none', 'null'):
            names.append(listNames[i])
            values.append(str(listValues[i]))

    listNames = names
    listValues = values
    listWhere = [i.lower() for i in listWhere]
    listTypes = [i.upper() if i is not None else None for i in listTypes]

    names = []

    for i in range( len(listNames) ):
        names.append(listNames[i].lower())
        if listNames[i].lower() in listWhere:
            where[listNames[i].lower()] = listValues[i]
        print(i, listNames[i].lower(), listValues[i])
    values = []
    print(where)

    try:
        ## connect to DB
        connection = psycopg2.connect(database.conn)
        cursor = connection.cursor()

        getQuery(
            cursor = cursor,
            query = 'create table',
            table_name = table
            )
        connection.commit()

        getQuery(
            cursor = cursor,
            query = 'add with types columns',
            table_name = table,
            listNames = listNames,
            listValues = listTypes)
        connection.commit()

        getQuery(
            cursor = cursor,
            query = 'get ID', option = 'include NULL',
            table_name = table,
            listNames = [key for key in where], ### only selected columns
            listValues = [where[key] for key in where])
        query = cursor.fetchall()
        id = query[0][0]

        # print([entry for key, entry in where])

        if id is not None:
            getQuery(
                cursor = cursor,
                query = 'update set',
                table_name = table,
                listNames = names, listValues = listValues,
                whereNames = ['id'], whereValues = [id])
            connection.commit()
            if getID:
                return id
            if not getID:
                return

        getQuery(
            cursor = cursor,
            query = 'get columns',
            schema_name = schema_name, table_name = table)
        # print(query)
        query = cursor.fetchall()
        # print(query)

        ## create full list of Columns from DB table
        listColumns = []
        for i in query:
            listColumns.append(i[0])
        # print(listColumns)

        for col in listColumns:
            if col not in names:
                values.append('DEFAULT')
            else:
                for n in range( len(names) ):
                    if names[n] == col:
                        values.append(listValues[n])
        # print(values)

        getQuery(
            cursor = cursor,
            query = 'insert into',
            table_name = table,
            listNames = listColumns, listValues = values)
        connection.commit()

        ## get ID (if required)
        # print('getID', getID)
        if getID:
            getQuery(
                cursor = cursor,
                query = 'get ID', option = 'strict',
                table_name = table,
                listNames = names, listValues = listValues
            )
            query = cursor.fetchall()
            id = query[0][0]
            return id


    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while handling PostgreSQL database:", error)

    finally:
        ## closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


################################################################################





# print(postgres, postgres['host'], postgres['password'])

ebisu = database(db_type=None, port=postgres['port'], host=postgres['host'], user=postgres['user'], password=postgres['password'], dbname=postgres['database'])


# Find all views with name "v_coordinates_*"
table_name = []
for table in ebisu.getViews():
    # print(y)
    if 'v_coordinates_' in table and 'v_coordinates_all' not in table:
        table_name.append(table)
print(table_name)


# random call view from database
table_name = sample(table_name, 1)[0]
print(table_name)

# get 1000 rows from view
sql_data = ebisu.getSQL('''
    SELECT
        a.latitude,
        a.longitude,
        a.prio::FLOAT / (SELECT MAX(b.prio) FROM {} AS b WHERE a."user" = b."user"),
        a.last_visit,
        a."user"
    FROM
        {} AS a'''.format(table_name, table_name))
try:
    sql_data = sample(sql_data, 1000)
except:
    pass
print(sql_data)

# summerize priority values
## done
# data = []
# for row in sql_data:
#     data.append(
#         {
#             'latitude': row[0],
#             'longitude': row[1],
#             'prio': row[2],
#             'last_visit': row[3],
#             'user': row[4],
#             'table': table_name[14:],
#         }
#     )
#
# print(data)
# # send lat, long, priority and date with view name to table
#
# dict2sql(
#     dictionary = data,
#     db_name = ebisu,
#     table_name = 'tab_coordinates_all'
#     )

for row in sql_data:
    newRow(
        database = ebisu,
        schema_name = 'public',
        table_name = 'tab_coordinates_all',
        listNames = ['latitude', 'longitude', 'prio', 'last_visit', 'user', 'table'],
        listValues = [row[0], row[1], row[2], row[3], row[4], table_name[14:]],
        listWhere = ['latitude', 'longitude', 'user', 'table'],
        listTypes = ['FLOAT', 'FLOAT', 'FLOAT', 'TIMESTAMPTZ', 'TEXT', None])
    # dict2sql(
    #     dictionary = {
    #         'latitude': row[0],
    #         'longitude': row[1],
    #         'prio': row[2],
    #         'last_visit': row[3],
    #         'user': row[4],
    #         'table': table_name[14:],
    #         },
    #     db_name = ebisu,
    #     table_name = 'tab_coordinates_all',
    #     listTypes = ,
    #     listWhere =
        # )

# send lat, long, priority and date with view name to table
