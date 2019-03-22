## https://pynative.com/python-postgresql-tutorial/

# import os
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

        # self.conn = psycopg2.connect(self.conn)
        # self.cur = self.conn.cursor()
        #
        # self.cur.execute('select * from people')
        # self.results = self.cur.fetchall()

    def setSQL(self, query):
        # print(self.conn, " : ", query)
        try:
            connection = psycopg2.connect(self.conn)
            cursor = connection.cursor()

            cursor.execute(query)
            connection.commit()

        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating PostgreSQL table", error)

        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")

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
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")

        return returnValue

    def createTable(self, table_name = None, listNames = []):
        if table_name is not None:
            self.setSQL('CREATE TABLE IF NOT EXISTS {} (ID INTEGER PRIMARY KEY, {} AUTO, {} AUTO, {} AUTO);'.format(table_name, listNames[0], listNames[1], listNames[2]))

    def newRow(self, schema_name = 'public', table_name = None, listNames = [], listValues = [], getID = True):
        # I need: self, table_name, list of columns, list of values
        # connect to DB
        # Check/create table existance
        # check/insert table cokumns
        # get all column names from table
        # insert values (if not existant)
        # ? get id ?
        # close connection to DB

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

        table = table_name.lower()
        schema = schema_name.lower()
        names = []
        for item in listNames:
            names.append(item.lower())
        values = []

        getIDquery = []
        for n in range( len(names) ):
            getIDquery.append('\"{}\" = \'{}\''.format(names[n], listValues[n]))
        getIDquery = '''SELECT MAX(id)
            FROM \"''' + table + '''\"
            WHERE ''' + '''
            AND '''.join(getIDquery) + '''
            ;'''

        try:
            ## connect to DB
            connection = psycopg2.connect(self.conn)
            cursor = connection.cursor()

            ## create table (if not exists)
            query = '''CREATE TABLE IF NOT EXISTS \"{}\"
                (id SERIAL PRIMARY KEY);'''.format(table)
            print(query)
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
            print('{}'.format(query))
            cursor.execute(query)
            connection.commit()

            print(getIDquery)
            cursor.execute(getIDquery)
            query = cursor.fetchall()
            # print(query, query[0], type(query[0]), query[0][0], type(query[0][0]))
            if getID and (query[0][0] is not None):
                return query[0][0]
            if not getID and (query[0][0] is not None):
                return

            ## get all column names
            query = '''SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = \'{}\'
                AND table_name   = \'{}\'
                ;'''.format(schema, table)
            print(query)
            cursor.execute(query)
            query = cursor.fetchall()

            listColumns = []
            for i in query:
                listColumns.append(i[0])
            print(listColumns)

            for col in listColumns:
                if col not in names:
                    values.append('DEFAULT')
                else:
                    for n in range( len(names) ):
                        if names[n] == col:
                            values.append("\'" + listValues[n] + "\'")
            print(values)

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
            print('{}'.format(query))
            cursor.execute(query)
            connection.commit()

            ## get ID (if required)
            if getID:
                print(getIDquery)
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

    # def json2sql(self, json = None):
    #     self.setSQL('''
    #         DO
    #         $do$
    #         BEGIN
    #
    #         EXECUTE (
    #            SELECT format('CREATE TABLE %I(%s)', metadata->>'tablename', c.cols)
    #            FROM   public.json_metadata m
    #            CROSS  JOIN LATERAL (
    #               SELECT string_agg(quote_ident(col->>'name')
    #                                 || ' ' ||  (col->>'datatype')::regtype, ', ') AS cols
    #               FROM   json_array_elements(metadata->'columns') col
    #               ) c
    #            );
    #         END
    #         $do$;''')

    def getID(self, table_name = None, names = [], values = []):
        if table_name is not None:
            self.cur.execute('SELECT MAX(id) FROM {} WHERE name LIKE ?;'.format(table_name))
            return self.cur.fetchall()



    # todo:
    #     1. does table exist?
    #     2. if no: create table shell
    #     3. does entry exist?
    #     4. if yes: get ID
    #     5. if no: create entry and get ID


    # cursor.execute("CREATE TABLE IF NOT EXISTS outdoors(id INTEGER PRIMARY KEY, name TEXT)")
    # cursor.execute("SELECT max(id) FROM outdoors WHERE name LIKE ?", ([outdoors_name]))
    # outdoors_id = cursor.fetchone()[0]
    # if outdoors_id is None:
    #     cursor.execute("INSERT INTO outdoors(name) VALUES (?)", ([outdoors_name]))
    #     cursor.execute('SELECT max(id) FROM outdoors')
    #     outdoors_id = cursor.fetchone()[0]
