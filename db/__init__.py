import psycopg2

conn = psycopg2.connect('host=copyright user=pi password=21255Dohren dbname=test')
cur = conn.cursor()

cur.execute('select * from people')

results = cur.fetchall()

for result in results:
    print(result)
