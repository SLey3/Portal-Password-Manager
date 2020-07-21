"""
SQL tools for Application data manegment
"""
# Imports
import sqlite3
import os
import wx
import shutil

# SQL code below
def append(name, url, username, password):
    """
    Inserts user data into SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    name = name.capitalize()
    
    conn = sqlite3.connect(FILE_PATH)

    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO manager VALUES (?, ?, ?, ?)", (name, url, username, password))
    conn.commit()
    conn.close()
    
def updateName(new_name, url):
    """
    Updates the name from the SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    web_name = new_name.capitalize()
    
    conn = sqlite3.connect(FILE_PATH)

    cursor = conn.cursor()
    
    with conn:
        cursor.execute("""UPDATE manager SET name = :name
                          WHERE url = :url""",
                          {'name': web_name, 'url': url})
    conn.commit()
    conn.close()
    
def updateLink(web_name, url):
    """
    Updates the url from the SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    web_name = web_name.capitalize()
    
    conn = sqlite3.connect(FILE_PATH)

    cursor = conn.cursor()
    
    with conn:
        cursor.execute("""UPDATE manager SET url = :url
                          WHERE name = :name""",
                          {'name': web_name, 'url': url})
    conn.commit()
    conn.close()
    
def updateUsername(usr, web_name):
    """
    Updates the username from the SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    web_name = web_name.capitalize()
    
    conn = sqlite3.connect(FILE_PATH)

    cursor = conn.cursor()
    
    with conn:
        cursor.execute("""UPDATE manager SET username = :username
                          WHERE name = :name""",
                          {'name': web_name, 'username': usr})
    conn.commit()
    conn.close()
        
def updatePassword(pwd, web_name):
    """
    Updates the password from the SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    web_name = web_name.capitalize()
    
    conn = sqlite3.connect(FILE_PATH)

    cursor = conn.cursor()
    
    with conn:
        cursor.execute("""UPDATE manager SET password = :password
                          WHERE name = :name""",
                          {'name': web_name, 'password': pwd})
    conn.commit()
    conn.close()
    
def remove_Account_Data(web_name, url, username, password):
    """
    Removes an account data from the SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    web_name = web_name.capitalize()
    
    conn = sqlite3.connect(FILE_PATH)

    cursor = conn.cursor()
    
    with conn:
        cursor.execute("DELETE from manager WHERE name = :name AND url = :url AND username = :username AND password = :password",
                       {'name': web_name, 'url': url, 'username': username, 'password': password})
    conn.commit()
    conn.close()
    
def getAll(web_name):
    """
    Gets all information from SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    web_name = web_name.capitalize()
    
    conn = sqlite3.connect(FILE_PATH)

    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM manager WHERE name=(?)", (web_name,))
    data = cursor.fetchall()
    if data == [] and data == None:
        app = wx.App()
        wx.MessageBox("Information not found. Check your spelling or grammer Or Account data does not exist.", 'Error', wx.OK|wx.ICON_ERROR)
    conn.close()
    return data
    
def getWebsiteName(web_name):
    """
    Gets the name of the website from the SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    web_name = web_name.capitalize()
    
    conn = sqlite3.connect(FILE_PATH)

    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM manager WHERE name=(?)", (web_name,))
    data = cursor.fetchone()
    if data == [] and data == None:
        app = wx.App()
        wx.MessageBox("Information not found. Check your spelling or grammer Or Account data does not exist.", 'Error', wx.OK|wx.ICON_ERROR)
    conn.close()
    return data
    
def getUrl(web_name):
    """
    Gets the url from the SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    web_name = web_name.capitalize()
    
    conn = sqlite3.connect(FILE_PATH)

    cursor = conn.cursor()
    
    cursor.execute("SELECT url FROM manager WHERE name=(?)", (web_name,))
    data = cursor.fetchone()
    if data == [] and data == None:
        app = wx.App()
        wx.MessageBox("Information not found. Check your spelling or grammer Or Account data does not exist.", 'Error', wx.OK|wx.ICON_ERROR)
    conn.close()
    return data

def getUsername(web_name):
    """
    Gets the username from the SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    web_name = web_name.capitalize()
    
    conn = sqlite3.connect(FILE_PATH)

    cursor = conn.cursor()
    
    cursor.execute("SELECT username FROM manager WHERE name=(?)", (web_name,))
    data = cursor.fetchone()
    if data == [] and data == None:
        app = wx.App()
        wx.MessageBox("Information not found. Check your spelling or grammer Or Account data does not exist.", 'Error', wx.OK|wx.ICON_ERROR)
    conn.close()
    return data
    
def getPassword(web_name):
    """
    Gets password from SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    web_name = web_name.capitalize()
    
    conn = sqlite3.connect(FILE_PATH)

    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM manager WHERE name=(?)", (web_name,))
    data = cursor.fetchone()
    if data == [] and data == None:
        app = wx.App()
        wx.MessageBox("Information not found. Check your spelling or grammer Or Account data does not exist.", 'Error', wx.OK|wx.ICON_ERROR)
    conn.close()
    return data

def regenerateDatabase():
    """
    Regenerates the SQL database
    """
    FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\database\\data.db'
    wx.App()
    wx.MessageBox("Are you sure you want to regenerate the database? Doing this may delete any existing data in the database", 'Information', wx.YES_NO|wx.ICON_INFORMATION)
    if wx.YES:
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
            APP_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager'
    
            DESTINATION_FILE_PATH = APP_PATH + '\\src\\appResources\\docs\\database'
            
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
        wx.MessageBox("Database regenerated.", 'Information', wx.OK|wx.ICON_INFORMATION)
