import sqlite3
import pprint

connection = sqlite3.connect('data.sqlite')
cursor = connection.cursor()
result = cursor.execute("SELECT * FROM RESPONSE")
connection.commit()
cols = [description[0] for description in cursor.description]
print(cols)
data = []
for row in result:
	item = {}
	for i, col in enumerate(cols):
		item[col] = row[i]
	data.append(item)
connection.close()
pprint.pprint(data)
