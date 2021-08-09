import sqlite3

from sqlite3 import Error
from sqlite3.dbapi2 import Cursor, sqlite_version

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"")


db_file = "./votingapp/db.sqlite3"

conn = sqlite3.connect(db_file)

cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()

cur.execute("SELECT * FROM auth_user_groups").fetchall()

cur.execute("SELECT * FROM auth_user").fetchall()

cur.execute("SELECT * FROM auth_permission").fetchall()
cur.execute("SELECT * FROM django_admin_log").fetchall()
cur.execute("SELECT * FROM auth_user").fetchall()


