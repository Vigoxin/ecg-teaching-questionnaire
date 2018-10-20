from app import db, Response

result = Response.query.all()
data = [row.__dict__ for row in result]
print(data)
# data = [{key: row[key] for key in row.__dict__.keys() if key != '_sa_instance_state'} for row in result]
data = []
for row in result:
	item = {}
	row = row.__dict__
	for key in row:
		item[key] = row[key]
	data.append(item)
# print(data)

# nums = list(range(1, 11))
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# print({num: alphabet[num-1] for num in nums})