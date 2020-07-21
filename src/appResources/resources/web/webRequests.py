# import
import requests
from bs4 import BeautifulSoup

# Website Requests

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
        self.parse
    
    @property
    def parse(self):
        with requests.Session() as r:
            pass