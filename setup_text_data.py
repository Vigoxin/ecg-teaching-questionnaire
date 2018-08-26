# Setting up text database
with open('text_data.txt', 'w') as file:
	to_add = [5, 5, 5, 5, 'testing', 'testing comment']
	to_add = ','.join([str(el) for el in to_add]) + '\n'
	file.write(to_add)