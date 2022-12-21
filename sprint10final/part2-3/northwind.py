'''sqlite3 conection and queries executed on the northwind database'''

import sqlite3



connection = sqlite3.connect('northwind_small-1.sqlite3')

cursor = connection.cursor()


#==============Queries===============

expensive_items = '''SELECT * FROM product
                     ORDER BY UnitPrice  DESC
                     LIMIT 10;'''

'''[(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0), (29, 'Thüringer Rostbratwurst', 12, 6, '50 bags x 30 sausgs.', 123.79, 0, 0, 0, 1), (9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97, 29, 0, 0, 1), (20, "Sir Rodney's Marmalade", 8, 3, '30 gift boxes', 81, 40, 0, 0, 0), (18, 'Carnarvon Tigers', 7, 8, '16 kg pkg.', 62.5, 42, 0, 0, 0), (59, 'Raclette Courdavault', 28, 4, '5 kg pkg.', 55, 79, 0, 0, 0), (51, 'Manjimup Dried Apples', 24, 7, '50 - 300 g pkgs.', 53, 20, 0, 10, 0), (62, 'Tarte au sucre', 29, 3, '48 pies', 49.3, 17, 0, 0, 0), (43, 'Ipoh Coffee', 20, 1, '16 - 500 g tins', 46, 17, 10, 25, 0), (28, 'Rössle Sauerkraut', 12, 7, '25 - 825 g cans', 45.6, 26, 0, 0, 1)]'''


avg_hire_age = '''SELECT AVG(HireDate - BirthDate) AS avg_hire_age
                  FROM employee;'''

'''[(37.22222222222222,)]'''


ten_most_expensive = '''SELECT ProductName, UnitPrice, CompanyName
                        FROM product 
                        INNER JOIN Supplier
                        ON product.Id = supplier.Id
                        ORDER BY UnitPrice DESC
                        LIMIT 10;'''

'''[('Thüringer Rostbratwurst', 123.79, "Forêts d'érables"), ('Mishi Kobe Niku', 97, 'PB Knäckebröd AB'), ("Sir Rodney's Marmalade", 81, 'Leka Trading'), ('Carnarvon Tigers', 62.5, 'Aux joyeux ecclésiastiques'), ('Rössle Sauerkraut', 45.6, 'Gai pâturage'), ('Schoggi Schokolade', 43.9, 'Escargots Nouveaux'), ('Northwoods Cranberry Sauce', 40, 'Specialty Biscuits, Ltd.'), ('Alice Mutton', 39, 'Svensk Sjöföda AB'), ('Queso Manchego La Pastora', 38, 'Plutzer Lebensmittelgroßmärkte AG'), ('Gumbär Gummibärchen', 31.23, 'Pasta Buttini s.r.l.')]'''


largest_category = '''SELECT COUNT(DISTINCT ProductName), CategoryId
                      FROM product
                      LEFT JOIN category
                      ON product.Id = category.Id
                      GROUP BY CategoryId;'''

'''[(12, 1), (12, 2), (13, 3), (10, 4), (7, 5), (6, 6), (5, 7), (12, 8)]'''


cursor.execute(expensive_items)
cursor.execute(avg_hire_age)
cursor.execute(ten_most_expensive)
cursor.execute(largest_category)

connection.commit()
results = cursor.fetchall()
print(results)
