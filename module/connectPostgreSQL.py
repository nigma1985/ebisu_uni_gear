## https://pynative.com/python-postgresql-tutorial/

import psycopg2
from psycopg2 import Error


def getQuery(
    cursor = None,
    query = None, option = '',
    schema_name = 'public', table_name = None,
    listNames = [], listValues = [],
    whereNames = [], whereValues = []):

    ## check variables
    if cursor is None:
        raise Exception('missing cursor')
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

    # def reValue(a):
    #     ## check two lists for substance and symetry
    #     if isinstance(a, str):
    #         return a.replace("'","\'\'")
    #     else:
    #         return a

    result = None
    table = table_name.lower()
    vals = []

    ## create query to fetch one ID
    if query == 'get ID':
        result = []
        bal = chkBalance(listNames, listValues)
        if bal:
            raise Exception('can\'t get ID - ', bal)

        if option is None:
            raise Exception('missing option')
        elif not isinstance(option, str):
            raise Exception('option is type {}. Only string allowed.'.format(type(option)))

        ## strict search: only result for exact match
        elif option == 'strict':
            for n in range( len(listNames) ):
                result.append('(\"{}\" = %s)'.format(listNames[n]))
                vals.append(str(listValues[n]))

        ## include NULL search: like strict seatch but also includes values that are NULL/None
        elif option == 'include NULL':
            for n in range( len(listNames) ):
                result.append('((\"{}\" = %s) OR (\"{}\" IS NULL))'.format(listNames[n], listNames[n]))
                vals.append(str(listValues[n]))
        else:
            raise Exception('unknown option: \'{}\''.format(option))

        result = '''SELECT MAX(id)
            FROM \"''' + table + '''\"
            WHERE ''' + '''
            AND '''.join(result) + '''
            ;'''
        # print(result, vals)
        return cursor.execute(result, vals)

    ## create query to create table (if not exists)
    elif query == 'create table':
        result = '''CREATE TABLE IF NOT EXISTS \"{}\"
            (id SERIAL PRIMARY KEY);'''.format(table)
        # print(result)
        return cursor.execute(result)

    ## create query to add columns to table (if not exists)
    elif query == 'add columns':
        result = []
        if (listNames is None) or listNames == 0:
            raise Exception('can\'t add columns - missing list')

        for n in range( len(listNames) ):
            result.append('ADD COLUMN IF NOT EXISTS \"{}\" TEXT'.format(listNames[n]))
        result = '''ALTER TABLE IF EXISTS {}
            '''.format(table) + ''',
            '''.join(result) + '''
            ;'''
        # print(result)
        return cursor.execute(result)

    ############################################################################
    ## create query to add columns to table (if not exists)
    # whereNames = [], whereValues = []
    elif query == 'add with types columns':
        result = []

        bal = chkBalance(listNames, listValues)
        if bal:
            raise Exception('can\'t add columns - ', bal)

        for n in range( len(listNames) ):
            result.append('ADD COLUMN IF NOT EXISTS \"{}\" {}'.format(
                listNames[n],
                'TEXT' if listValues[n] is None else listValues[n]))
        result = '''ALTER TABLE IF EXISTS {}
            '''.format(table) + ''',
            '''.join(result) + '''
            ;'''
        # print(result)
        return cursor.execute(result)
    ############################################################################

    ## create query to update set: update all names = values, WHERE names = values
    elif query == 'update set':
        bal = chkBalance(listNames, listValues)
        if bal:
            raise Exception('can\'t update set - ', bal)

        bal = chkBalance(whereNames, whereValues)
        if bal:
            raise Exception('can\'t update set - ', bal)

        result = []
        where = []
        for n in range( len(listNames) ):
            result.append('\"{}\" = %s'.format(listNames[n], listValues[n]))
            vals.append(str(listValues[n]))
        for n in range( len(whereNames) ):
            where.append('\"{}\" = %s'.format(whereNames[n], whereValues[n]))
            vals.append(str(whereValues[n]))
        result = '''UPDATE {} SET
            '''.format(table) + ''',
            '''.join(result) + '''
            WHERE''' + '''
            AND '''.join(where) + '''
            ;'''
        # print(result, vals)
        return cursor.execute(result, vals)

    ## create query to get all column names within table
    elif query == 'get columns':
        if schema_name is None:
            raise Exception('missing schema name')
        if not isinstance(schema_name, str):
            raise Exception('table schema is type {}. Only string is allowed.'.format(type(schema_name)))

        result = '''SELECT column_name
            FROM information_schema.columns
            WHERE table_schema = \'{}\'
            AND table_name   = \'{}\'
            ;'''.format(schema_name.lower(), table)
        # print(result)
        return cursor.execute(result)

    ## create query to insert set into table: insert all names = values
    elif query == 'insert into':
        bal = chkBalance(listNames, listValues)
        if bal:
            raise Exception('can\'t insert into - ', bal)

        placeholders = []
        for item in listValues:
            if item == 'DEFAULT':
                placeholders.append('DEFAULT')
            else:
                placeholders.append('%s')
                vals.append(item)

        result = '''
            INSERT INTO \"{}\" (
                \"{}\")
            VALUES (
                {})
            ;'''.format(table, '''\",
                \"'''.join(listNames), ''',
                '''.join(placeholders)
                )
        # print(result, vals)
        return cursor.execute(result, vals)

    else:
        # print('error')
        raise Exception('unknown option: \'{}\''.format(query))

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
        id = None
        table = table_name.lower()
        # print(table_name, table_name.lower(), table)
        schema = schema_name.lower()

        names = []
        values = []
        for i in range( len(listValues) ):
            if str(listValues[i]).lower() not in (None, '', 'none', 'null'):
                names.append(listNames[i])
                values.append(str(listValues[i]))


        listNames = names
        listValues = values

        names = []

        for i in range( len(listNames) ):
            names.append(listNames[i].lower())
        values = []

        try:
            ## connect to DB
            connection = psycopg2.connect(self.conn)
            cursor = connection.cursor()

            ## create table (if not exists)
            # print('cursor =', cursor)
            # print('query =', 'create table')
            # print('table_name =', table)
            getQuery(
                cursor = cursor,
                query = 'create table',
                table_name = table
                )
            connection.commit()

            ## add columns (if not exists)
            # print('cursor =', cursor)
            # print('query =', 'add columns')
            # print('table_name =', table)
            # print('listNames =', names)
            getQuery(
                cursor = cursor,
                query = 'add columns',
                table_name = table,
                listNames = names)
            connection.commit()

            # print(getIDquery)
            # print('cursor =', cursor)
            # print('query =', 'get ID', '|', 'option =', 'include NULL')
            # print('table_name =', table)
            # print('listNames =', names, '|', 'listValues =', listValues)
            getQuery(
                cursor = cursor,
                query = 'get ID', option = 'include NULL',
                table_name = table,
                listNames = names, listValues = listValues)
            query = cursor.fetchall()
            id = query[0][0]
            # print('id:', id, '|', query, query[0], type(query[0]), query[0][0], type(query[0][0]))

            if id is not None:
                ## update row
                # print('cursor =', cursor)
                # print('query =', 'update set')
                # print('table_name =', table)
                # print('listNames =', names, '|', 'listValues =', listValues)
                # print('whereNames =', ['id'], '|', 'whereValues =', [id])
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

            ## get all column names
            # print('cursor =', cursor)
            # print('query =', 'get columns')
            # print('schema_name =', schema_name, '|', 'table_name =', table)
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

            ## standard insert
            # query = '''
            #     INSERT INTO \"{}\" (
            #         \"{}\")
            #     VALUES (
            #         {})
            #     ;'''.format(table, '''\",
            #         \"'''.join(listColumns), ''',
            #         '''.join(values)
            #         )

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

            # print('cursor =', cursor)
            # print('query =', 'insert into')
            # print('table_name =', table)
            # print('listNames =', listColumns, '|', 'listValues =', values)
            getQuery(
                cursor = cursor,
                query = 'insert into',
                table_name = table,
                listNames = listColumns, listValues = values)
            connection.commit()

            ## get ID (if required)
            # print('getID', getID)
            if getID:
                # print(getIDquery)
                # print('cursor =', cursor)
                # print('query =', 'get ID', '|', 'option =', 'strict')
                # print('table_name =', table)
                # print('listNames =', names, '|', 'listValues =', listValues)
                getQuery(
                    cursor = cursor,
                    query = 'get ID', option = 'strict',
                    table_name = table,
                    listNames = names, listValues = listValues
                )
                query = cursor.fetchall()
                id = query[0][0]
                # print('id:', id, '|', query, query[0], type(query[0]), query[0][0], type(query[0][0]))
                return id


        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while handling PostgreSQL database:", error)

        finally:
            ## closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def getViews(self):
        return [i[0] for i in self.getSQL('''
            SELECT
                table_name AS nm
            FROM
                INFORMATION_SCHEMA.views AS v
            ;''')]

def dict2sql(
    dictionary = None, db_name = None,
    # father_table = None, father_id = None,
    table_name = None,
    addNames = [], addValues = []
    ):
    if dictionary is None:
        raise Exception('missing dictionary')
    if not isinstance(dictionary, dict):
        raise Exception('dictionary is type {}. Only dict is allowed.'.format( type(table_name) ))
    if db_name is None:
        raise Exception('missing database')
    if table_name is None:
        raise Exception('missing table name')
    if not isinstance(table_name, str):
        raise Exception('table name is type {}. Only string is allowed.'.format( type(table_name) ))
    if (addNames is None):
        raise Exception('missing list of names')
    if (addValues is None):
        raise Exception('missing list of values')
    if not isinstance(addNames, (list, tuple)):
        raise Exception('names are type {}. Only lists or tuples allowed.'.format(type(addNames)))
    if not isinstance(addValues, (list, tuple)):
        raise Exception('values are type {}. Only lists or tuples allowed.'.format(type(addValues)))
    if len(addNames) != len(addValues):
        raise Exception('unequal number of names ({}) and values ({})'.format(len(addNames),len(addValues)))

    print('--' + table_name + '--')
    names = []
    values = []

    subTable = []

    for d in dictionary:
        # print(d, type(dictionary[d]))
        if isinstance(dictionary[d], (list, tuple)):
            subTable.append(d)
        elif isinstance(dictionary[d], (dict)):

            ## for right join (n:1)
            if d == 'id':
                names.append(table_name + '_' + d)
            else:
                names.append(d)
                # print(' -1', 'dictionary =', dictionary[d])
                # print(' -1', 'db_name =', db_name)
                # print(' -1', 'table_name =', d)
            values.append(
                dict2sql(
                    dictionary = dictionary[d],
                    db_name = db_name,
                    table_name = d)
            )
        else:
            if d == 'id':
                names.append(table_name + '_' + d)
            else:
                names.append(d)
            values.append(dictionary[d])

    for i in range( len(addNames) ):
        if addNames[i] == 'id':
            names.append(table_name + '_' + addNames[i])
        else:
            names.append(addNames[i])
        values.append(addValues[i])

    ## regular entry / new row
    # print(' -2', 'table_name =', table_name)
    # print(' -2', 'listNames =', names)
    # print(' -2', 'listValues =', values)
    id = db_name.newRow(
        table_name = table_name,
        listNames = names,
        listValues = values)


    ## for left join (1:n)
    for sub in subTable:
        for d in dictionary[sub]:
            dict2sql(
                dictionary = d,
                db_name = db_name,
                table_name = sub,
                addNames = [table_name],
                addValues = [id])

    return id
