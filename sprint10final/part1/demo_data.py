'''In this file i will conect to and execute queries
from the from the queries module to access the data base
i will create called demo_data.qlite3'''
import sqlite3



connection = sqlite3.connect('demo_data.sqlite3')

cursor = connection.cursor()

demo_table = '''
    CREATE TABLE IF NOT EXISTS demo_table
    ("s" VARCHAR NOT NULL PRIMARY KEY,
    "X" INT NOT NULL,
    "Y" INT NOT NULL);
    '''

cursor.execute(demo_table)

cursor.execute('''INSERT OR IGNORE INTO demo_table VALUES ("g", 3, 9);''')
cursor.execute('''INSERT OR IGNORE INTO demo_table VALUES ('v', 5, 7);''')
cursor.execute('''INSERT OR IGNORE INTO demo_table VALUES ('f', 8, 7);''')

#==================QUERIES====================

select_all = '''SELECT * FROM DEMO_TABLE;'''

'''[('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]'''


row_count = '''SELECT count(S) AS num_of_rows
               FROM demo_table'''

'''[(3,)]'''


xy_at_least_5 = '''SELECT count(*)
                   FROM demo_table
                   WHERE (x >= 5) AND 
                   (y >=5);
                   '''

'''[(2,)]'''


unique_y = '''SELECT count(DISTINCT y)
FROM demo_table;'''

'''[(2,)]'''



cursor.execute(select_all)
cursor.execute(row_count)
cursor.execute(xy_at_least_5)
cursor.execute(unique_y)

connection.commit()
results = cursor.fetchall()
print(results)
