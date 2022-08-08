import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="BBoH$$.")

c = conn.cursor()
c.execute('select version()')

db_version = c.fetchone()
print('DB server version:', db_version)

c.close()
conn.close()