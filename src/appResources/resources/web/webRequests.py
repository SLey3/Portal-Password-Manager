# import
import requests
from bs4 import BeautifulSoup
import js2py
import os


# Website Requests
JS_FILEPATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\resources\\web\\lib\\js-package\\webScraper.js'

class webRequest:
    """
    Copies and pastes username and password by default with the option of the first/last initial or fullname into a login form of a website
    """
    def __init__(self, url, usr, pwd, first=None, last=None, fullname=None, headers={}):
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
          from . import scraper as Scrape
        
        self.parse
    
    @property
    def parse(self):
        with requests.Session() as r:
            website = r.get(self.url)
webRequest('gmail.com', 'ghub4127@gmail.com', 'Empire')
