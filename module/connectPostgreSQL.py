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
            print ("Error while creating PostgreSQL table", error)

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

    def newRow(self, table_name = None, listNames = [], listValues = []):
        if table_name is not None:
            self.setSQL('INSERT INTO {}({}, {}, {}) VALUES ({}, {}, {});'.format(table_name, listNames[0], listNames[1], listNames[2], listValues[0], listValues[1], listValues[2]))

    def json2sql(self, json = None):
        self.setSQL('''
            DO
            $do$
            BEGIN

            EXECUTE (
               SELECT format('CREATE TABLE %I(%s)', metadata->>'tablename', c.cols)
               FROM   public.json_metadata m
               CROSS  JOIN LATERAL (
                  SELECT string_agg(quote_ident(col->>'name')
                                    || ' ' ||  (col->>'datatype')::regtype, ', ') AS cols
                  FROM   json_array_elements(metadata->'columns') col
                  ) c
               );
            END
            $do$;''')

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
