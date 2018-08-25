from app import db, Response

# Read
print(Response.query.get(1))