import psycopg2


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

# Instantiate the Dog object
philo = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')
print(philo.results)
