"""
App Tools for application
"""
#Imports
import os
import sqlite3
import shutil
import jsonpickle


# Setup Tool
def generate_database():
    """
    Creats Sqlite3 Database
    """
    APP_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager'
    
    DESTINATION_FILE_PATH = APP_PATH + '\\src\\appResources\\docs\\database'
    
    
    if os.path.isfile('data.db') == False:
        try:
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS manager (
                            name TEXT,
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


def jsonLineCount():
    line_count = 0
    JSON_FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\json\\account.json'
    with open(JSON_FILE_PATH) as j:
        for line in j:
            line_count+=1
    return line_count

class accountObject:
    """
    Initializes object for account
    """
    def __init__(self, first, last, fullname, username, password):
        self.first = first
        self.last = last
        self.fullname = fullname
        self.username = username
        self.password = password
