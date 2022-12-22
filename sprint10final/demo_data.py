'''In this file i will conect to and execute queries
from the from the queries module to access the data base
i will create called demo_data.qlite3'''
import sqlite3

connection = sqlite3.connect('demo_data.sqlite3')

cursor = connection.cursor()

demo_table = '''
    CREATE TABLE IF NOT EXISTS demo
    ("s" VARCHAR NOT NULL PRIMARY KEY,
    "X" INT NOT NULL,
    "Y" INT NOT NULL);
    '''

cursor.execute(demo_table)

cursor.execute('''INSERT OR IGNORE INTO demo VALUES ("g", 3, 9);''')
cursor.execute('''INSERT OR IGNORE INTO demo VALUES ('v', 5, 7);''')
cursor.execute('''INSERT OR IGNORE INTO demo VALUES ('f', 8, 7);''')


select_all = '''SELECT * FROM demo;'''

'''[('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]'''

row_count = '''SELECT count(S) AS num_of_rows
               FROM demo'''

'''[(3,)]'''


xy_at_least_5 = '''SELECT count(*)
                   FROM demo
                   WHERE (x >= 5) AND
                   (y >=5);
                   '''

'''[(2,)]'''


unique_y = '''SELECT count(DISTINCT y)
FROM demo;'''

'''[(2,)]'''


cursor.fetchall()

print(cursor.execute(select_all).fetchall())
print(cursor.execute(row_count).fetchall())
print(cursor.execute(xy_at_least_5).fetchall())
print(cursor.execute(unique_y).fetchall())
connection.commit()
