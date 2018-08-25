from app import db, Response
import sqlite3
import pandas
con = sqlite3.connect('data.sqlite')
table = pandas.read_sql('select * from response', con)
table.to_csv('output.csv')