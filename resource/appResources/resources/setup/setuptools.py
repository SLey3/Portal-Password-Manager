"""
Setup Tools for application
"""
#Imports
import os
import sqlite3
import shutil

# Setup Tool
def generate_database():
    """
    Creats Sqlite3 Database
    """
    APP_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager'
    
    DESTINATION_FILE_PATH = APP_PATH + '\\resource\\appResources\\docs\\database'
    
    
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
    ORIGINAL_FILE_PATH = os.path.join(APP_PATH, 'data.db')
    shutil.move(ORIGINAL_FILE_PATH, DESTINATION_FILE_PATH, copy_function=shutil.copytree)
    
# Setup Configuration
__AUTHOR__ = "Sergio Ley Languren"

__EMAIL__ = "ghub4127@gmail.com"

__APP__ = "Portal Password Manager"