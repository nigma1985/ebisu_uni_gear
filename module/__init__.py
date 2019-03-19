## https://pynative.com/python-postgresql-tutorial/

import os
import json
import psycopg2

def json2py(jsonPath):
    with open(jsonPath, 'r') as f:
        return json.load(f)


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

        self.conn = psycopg2.connect(self.conn)
        self.cur = self.conn.cursor()

        self.cur.execute('select * from people')
        self.results = self.cur.fetchall()

    def createTable(self, table_name = None):
        if table_name is not None:
            self.cur.execute('CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY);'.format(table_name))
            self.conn.commit()

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
