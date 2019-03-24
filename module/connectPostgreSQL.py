## https://pynative.com/python-postgresql-tutorial/

import psycopg2
from psycopg2 import Error

class database:

    ## Class Attribute
    # species = 'mammal'
    # year = 2019

    # Initializer / Instance Attributes
    def __init__(self, db_type = None, host = None, user = None, port = None, password = None, dbname = None):
        self.conn = ''
        if host is not None:
            self.conn = self.conn + ' host=' + host
        if user is not None:
            self.conn = self.conn + ' user=' + user
        if port is not None:
            self.conn = self.conn + ' port=' + port
        if password is not None:
            self.conn = self.conn + ' password=' + password
        if dbname is not None:
            self.conn = self.conn + ' dbname=' + dbname

    def setSQL(self, query):
        # print(self.conn, " : ", query)
        try:
            connection = psycopg2.connect(self.conn)
            cursor = connection.cursor()

            cursor.execute(query)
            connection.commit()

        except (Exception, psycopg2.DatabaseError) as error :
            print("Error while creating PostgreSQL table", error)

        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                # print("PostgreSQL connection is closed")

    def getSQL(self, query):
        returnValue = None
        # print(self.conn, " : ", query)
        try:
            connection = psycopg2.connect(self.conn)
            cursor = connection.cursor()

            cursor.execute(query)
            returnValue = cursor.fetchall()

        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating PostgreSQL table:", error)

        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

        return returnValue

    def newRow(self, schema_name = 'public', table_name = None, listNames = [], listValues = [], getID = True):
        ## check variables
        if table_name is None:
            raise Exception('missing table name')
        if not isinstance(table_name, str):
            raise Exception('table name is type {}. Only string is allowed.'.format(type(table_name)))
        if (listNames is None) or (len(listNames) == 0):
            raise Exception('missing list of names')
        if (listValues is None) or (len(listValues) == 0):
            raise Exception('missing list of values')
        if not isinstance(listNames, (list, tuple)):
            raise Exception('names are type {}. Only lists or tuples allowed.'.format(type(listNames)))
        if not isinstance(listValues, (list, tuple)):
            raise Exception('values are type {}. Only lists or tuples allowed.'.format(type(listValues)))
        if len(listNames) != len(listValues):
            raise Exception('unequal number of names ({}) and values ({})'.format(len(listNames),len(listValues)))
        if not isinstance(getID, bool):
            raise Exception('getID is type {}. Only boolean is allowed.'.format(type(getID)))

        ## variables
        table = table_name.lower()
        schema = schema_name.lower()
        names = []
        for i in range( len(listNames) ):
            # if listValues[i] not in (None, '', 'None', 'Null'):
            names.append(listNames[i].lower())
        values = []

        ## contruct query to read the ID
        def getIDquery(table = None, rangeName = [], rangeValues = [], mode = None):
            if mode is None:

            IDquery = []
            for n in range( len(names) ):
                if mode.lower() is 'check':
                    IDquery.append('(\"{}\" = \'{}\')'.format(names[n], listValues[n]))
                elif mode.lower() is 'update':
                    IDquery.append('((\"{}\" = \'{}\') OR (\"{}\" IS NULL))'.format(names[n], listValues[n]), names[n])
                else:
                    return Exception('please choose mode for getID query: \'update\' or \'check\'.')
            IDquery = '''SELECT MAX(id)
                FROM \"''' + table + '''\"
                WHERE ''' + '''
                AND '''.join(IDquery) + '''
                ;'''
            return IDquery

        try:
            ## connect to DB
            connection = psycopg2.connect(self.conn)
            cursor = connection.cursor()

            ## create table (if not exists)
            query = '''CREATE TABLE IF NOT EXISTS \"{}\"
                (id SERIAL PRIMARY KEY);'''.format(table)
            # print(query)
            cursor.execute('{}'.format(query))
            connection.commit()

            ## add columns (if not exists)
            query = []
            for n in range( len(names) ):
                query.append('ADD COLUMN IF NOT EXISTS \"{}\" TEXT'.format(names[n]))
            query = '''ALTER TABLE IF EXISTS {}
                '''.format(table) + ''',
                '''.join(query) + '''
                ;'''
            # print('{}'.format(query))
            cursor.execute(query)
            connection.commit()

            # print(getIDquery)
            cursor.execute(getIDquery(table = table, rangeName = names, rangeValues = listValues, mode = 'update'))
            query = cursor.fetchall()
            # print(query, query[0], type(query[0]), query[0][0], type(query[0][0]))

            if query[0][0] is not None:
                ## update row
                if getID:
                    return query[0][0]
                if not getID:
                    return

            ## get all column names
            query = '''SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = \'{}\'
                AND table_name   = \'{}\'
                ;'''.format(schema, table)
            # print(query)
            cursor.execute(query)
            query = cursor.fetchall()

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
                            if isinstance(listValues[n], str):
                                values.append("\'" + listValues[n] + "\'")
                            else:
                                values.append("\'" + str(listValues[n]) + "\'")
            # print(values)

            ## standard insert
            query = '''
                INSERT INTO \"{}\" (
                    \"{}\")
                VALUES (
                    {})
                ;'''.format(table, '''\",
                    \"'''.join(listColumns), ''',
                    '''.join(values)
                    )

            ## include conflict treatment
            # query = '''
            #     INSERT INTO \"{}\" (
            #         \"{}\")
            #     VALUES (
            #         {})
            #     ON CONFLICT (
            #         \"{}\") DO NOTHING
            #     ;'''.format(table, '''\",
            #         \"'''.join(listColumns), ''',
            #         '''.join(values), '''\",
            #         \"'''.join(names)
            #         )
            # print('{}'.format(query))
            cursor.execute(query)
            connection.commit()

            ## get ID (if required)
            if getID:
                # print(getIDquery)
                cursor.execute(getIDquery)
                return cursor.fetchall()[0][0]


        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while handling PostgreSQL database:", error)

        finally:
            ## closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
