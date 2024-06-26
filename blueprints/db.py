import mysql.connector
from flask import g


def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host="localhost:3306",
            user="root",
            password="root",
            database="data_catalog"
        )
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
