import shelve

with shelve.open('shelf') as shelf:
	shelf['data'] = []