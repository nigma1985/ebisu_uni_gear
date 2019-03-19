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
    def __init__(self, db_type, host, user, password, dbname):
        self.conn = ''
        if host is not None:
            self.conn = self.conn + ' host=' + host
        if user is not None:
            self.conn = self.conn + ' user=' + user
        if password is not None:
            self.conn = self.conn + ' password=' + password
        if dbname is not None:
            self.conn = self.conn + ' dbname=' + dbname

        self.conn = psycopg2.connect(self.conn)
        self.cur = self.conn.cursor()

        self.cur.execute('select * from people')
        self.results = self.cur.fetchall()

    # todo:
    #     1. does table exist?
    #     2. if no: create table shell
    #     3. does entry exist?
    #     4. if yes: get ID
    #     5. if no: create entry and get ID
