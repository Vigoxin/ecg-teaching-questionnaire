import os
from app import db, Response, basedir
from sqlalchemy import create_engine

engine = create_engine('sqlite:///' + os.path.join(basedir, 'data.sqlite'))

Response.__table__.drop(engine)