from sqlite3 import *


with connect('database.db') as db:
    cursor = db.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS table1 (id INTEGER PRIMARY KEY, name TEXT,  expenses TEXT )""")

    cursor.execute(""" CREATE TABLE IF NOT EXISTS table2 (id INTEGER PRIMARY KEY, name TEXT,  expenses TEXT )""")


def list_tables():
    cursor.execute("""SELECT name FROM sqlite_master WHERE type = "table" """)
    return cursor.fetchall()

def information():
    cursor.execute("SELECT * FROM table1")
    return cursor.fetchall()


