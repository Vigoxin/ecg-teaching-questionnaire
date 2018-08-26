import shelve
with shelve.open('shelf') as shelf:
	print(shelf['data'])