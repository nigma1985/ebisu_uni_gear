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

    def getQuery(
        query = None, option = '',
        schema_name = 'public', table_name = None,
        listNames = [], listValues = [],
        whereNames = [], whereValues = []):

        ## check variables
        if query is None:
            raise Exception('missing query')
        if not isinstance(query, str):
            raise Exception('query is type {}. Only string is allowed.'.format(type(query)))
        if table_name is None:
            raise Exception('missing table name')
        if not isinstance(table_name, str):
            raise Exception('table name is type {}. Only string is allowed.'.format(type(table_name)))

        def chkBalance(a, b):
            ## check two lists for substance and symetry
            if (a is None) or (len(a) == 0) or (b is None) or (len(a) == 0):
                return 'missing value'
            if not isinstance(a, (list, tuple)) or not isinstance(b, (list, tuple)):
                return 'missing list (types : {}/{})'.format(type(a),type(b))
            if len(a) != len(b):
                return 'uneven lists (lengths : {}/{})'.format(len(a),len(b))
            else:
                return False

        result = None
        table = table_name.lower()

        ## create query to fetch one ID
        if query = 'get ID':
            result = []
            bal = chkBalance(listNames, listValues)
            if bal:
                raise Exception('can\'t get ID - ', bal)

            if option is None:
                raise Exception('missing option')
            elif not isinstance(option, str):
                raise Exception('option is type {}. Only string allowed.'.format(type(option)))

            ## strict search: only result for exact match
            elif option is 'strict':
                for n in range( len(listNames) ):
                    result.append('(\"{}\" = \'{}\')'.format(listNames[n], listValues[n]))

            ## include NULL search: like strict seatch but also includes values that are NULL/None
            elif option is 'include NULL':
                for n in range( len(listNames) ):
                    result.append('((\"{}\" = \'{}\') OR (\"{}\" IS NULL))'.format(listNames[n], listValues[n]), listNames[n])
            else:
                raise Exception('unknown option: \'{}\''.format(option))
            result = '''SELECT MAX(id)
                FROM \"''' + table + '''\"
                WHERE ''' + '''
                AND '''.join(result) + '''
                ;'''
            return result

        ## create query to create table (if not exists)
        elif query = 'create table':
            result = '''CREATE TABLE IF NOT EXISTS \"{}\"
                (id SERIAL PRIMARY KEY);'''.format(table)
            return result

        ## create query to add columns to table (if not exists)
        elif query = 'add columns':
            result = []
            if (listNames is None) or listNames == 0:
                raise Exception('can\'t add columns - missing list')

            for n in range( len(listNames) ):
                result.append('ADD COLUMN IF NOT EXISTS \"{}\" TEXT'.format(listNames[n]))
            result = '''ALTER TABLE IF EXISTS {}
                '''.format(table) + ''',
                '''.join(result) + '''
                ;'''
            return result

        ## create query to update set: update all names = values, WHERE names = values
        elif query = 'update set':
            bal = chkBalance(listNames, listValues)
            if bal:
                raise Exception('can\'t update set - ', bal)

            bal = chkBalance(whereNames, whereValues)
            if bal:
                raise Exception('can\'t update set - ', bal)

            result = []
            where = []
            for n in range( len(listNames) ):
                result.append('(\"{}\" = \'{}\')'.format(listNames[n], listValues[n]))
            for n in range( len(whereNames) ):
                where.append('(\"{}\" = \'{}\')'.format(whereNames[n], whereValues[n]))
            result = '''UPDATE {} SET
                '''.format(table) + ''',
                '''.join(result) + '''
                WHERE''' + '''
                AND '''.join(where) + '''
                ;'''
            return result

        ## create query to get all column names within table
        elif query = 'get columns':
            if table_schema is None:
                raise Exception('missing schema name')
            if not isinstance(table_schema, str):
                raise Exception('table schema is type {}. Only string is allowed.'.format(type(table_schema)))

            result = '''SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = \'{}\'
                AND table_name   = \'{}\'
                ;'''.format(schema_name.lower(), table)
            return result

        ## create query to insert set into table: insert all names = values
        elif query = 'insert into':
            bal = chkBalance(listNames, listValues)
            if bal:
                raise Exception('can\'t insert into - ', bal)

            result = '''
                INSERT INTO \"{}\" (
                    \"{}\")
                VALUES (
                    {})
                ;'''.format(table, '''\",
                    \"'''.join(listNames), ''',
                    '''.join(listValues)
                    )
            return result

        else:
            raise Exception('unknown option: \'{}\''.format(query))

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

        id = None
        names = []
        values = []
        for i in range( len(listValues) ):
            if listValues[i].lower() in (None, '', 'none', 'null'):
                name.append(listNames[i])
                values.append(listValues[i])
        listNames = names
        listValues = values

        ## variables
        table = table_name.lower()
        schema = schema_name.lower()
        names = []
        for i in range( len(listNames) ):
            names.append(listNames[i].lower())
        values = []

        try:
            ## connect to DB
            connection = psycopg2.connect(self.conn)
            cursor = connection.cursor()

            ## create table (if not exists)
            query = getQuery(
                query = 'create table',
                table_name = table):
            # print(query)
            cursor.execute('{}'.format(query))
            connection.commit()

            ## add columns (if not exists)
            query = getQuery(
                query = 'add columns',
                table_name = table,
                listNames = names)
            cursor.execute(query)
            connection.commit()

            # print(getIDquery)
            cursor.execute(getIDquery(table = table, rangeName = names, rangeValues = listValues, mode = 'update'))
            query = cursor.fetchall()
            id = query[0][0]
            # print(query, query[0], type(query[0]), query[0][0], type(query[0][0]))

            if id is not None:
                ## update row
                query = []
                for n in range( len(names) ):
                    query.append('(\"{}\" = \'{}\')'.format(names[n], listValues[n]))
                query = '''UPDATE {} SET
                    '''.format(table) + ''',
                    '''.join(query) + '''
                    WHERE id = {};'''.format(str(id))
                cursor.execute(query)
                connection.commit()
                if getID:
                    return id
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
                cursor.execute(getIDquery(table = table, rangeName = names, rangeValues = listValues, mode = 'check'))
                return cursor.fetchall()[0][0]


        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while handling PostgreSQL database:", error)

        finally:
            ## closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
