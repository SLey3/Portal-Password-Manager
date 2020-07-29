# import
import requests
import js2py
import os
import shutil
from selenium import webdriver

# Website Requests
JS_FILEPATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\resources\\web\\lib\\js-package\\Scraper.js'

HTML_FILEPATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\resources\\web\\lib\\html-package\\index.html'

WEB_DRIVER_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\resources\\web\\lib\\bin\\chromedriver.exe'

def headerDict():
  """
  stores header in dict form
  """
  driver = webdriver.Chrome(executable_path=WEB_DRIVER_PATH)
  driver.get(HTML_FILEPATH)
  temp_header_result = driver.find_elements_by_id('1')
  for c in temp_header_result:
    header = c.text
  
  header = {
    'user-agent': '{}'.format(header)
    }

  return header

class webRequest:
    """
    Copies and pastes username and password by default with the option of the first/last initial or fullname into a login form of a website
    """
    def __init__(self, url, usr, pwd, login_page="", first=None, last=None, fullname=None, headers=headerDict()):
        self.url = 'http://' + url
        self.usr = usr
        self.pwd = pwd
        if headers != {}:
          self.headers = headers
        else:
          pass
        if login_page != "":
          self.login_page = login_page
        else:
          pass
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
        
        self.parse
    
    @property
    def parse(self):
     with requests.Session() as r:
       try:
        import scraper as Scrape
       except ImportError:
        js2py.translate_file(JS_FILEPATH, 'scraper.py')
        SCRAPER_PATH = os.path.join(os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\', 'scraper.py')
        FINAL_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\resources\\web'
        shutil.move(SCRAPER_PATH, FINAL_PATH, copy_function=shutil.copytree)
        import scraper as Scrape
       website = r.get(self.url, headers=self.headers)
       Scraped = Scrape.PyJsHoisted_Scraper_(website.url)
       data = {
         "username":self.usr,
         "password":self.pwd
       }