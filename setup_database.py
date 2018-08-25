from app import db, Response

# Creates all the tables Model --> DB table
db.create_all()

test_response = Response(5, 5, 5, 5, 5, 5, 'asdfother', 'asdfcomments')
db.session.add(test_response)
db.session.commit()

