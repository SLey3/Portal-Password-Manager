#Imports
from setuptools import setup
import os
import sqlite3
import pip
### Setup Code
## Sqlite3 setup
if os.path.isfile('data.db') == False:
    try:
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS manager (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        url TEXT,
                        username TEXT,
                        password TEXT
                        )""")
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
## Setup Configuration
AUTHOR = "Sergio Ley Languren"

EMAIL = "ghub4127@gmail.com"

APP = "Portal Password Manager"
