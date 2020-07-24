# import
import requests
from bs4 import BeautifulSoup
import js2py
import os
import shutil


# Website Requests
JS_FILEPATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\resources\\web\\lib\\js-package\\Scraper.js'

def headerDict(header = None):
  """
  stores header in dict form
  """
  
  header = {
    'user-agent': '{}'.format(header)
    }
  return header

class webRequest:
    """
    Copies and pastes username and password by default with the option of the first/last initial or fullname into a login form of a website
    """
    def __init__(self, url, usr, pwd, first=None, last=None, fullname=None, headers=headerDict()):
        self.url = 'http://' + url
        self.usr = usr
        self.pwd = pwd
        self.headers = headers
        if first != None:
            self.first = first
        else:
            pass
        if last != None:
            self.last = last
        else:
            pass
        if fullname != None:
            self.fullname = fullname
        else:
            pass

        try:
          from . import scraper as Scrape
        except ImportError:
          js2py.translate_file(JS_FILEPATH, 'scraper.py')
          SCRAPER_PATH = os.path.join(os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\', 'scraper.py')
          FINAL_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\resources\\web'
          shutil.move(SCRAPER_PATH, FINAL_PATH, cop_function=shutil.copytree)
          from . import scraper as Scrape
        
        self.parse
    
    @property
    def parse(self):
        with requests.Session() as r:
            website = r.get(self.url, headers=self.headers)

try:
  from . import scraper as Scrape
except ImportError:
  js2py.translate_file(JS_FILEPATH, 'scraper.py')
  SCRAPER_PATH = os.path.join(os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\', 'scraper.py')
  FINAL_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\resources\\web'
  shutil.move(SCRAPER_PATH, FINAL_PATH, copy_function=shutil.copytree)
  
