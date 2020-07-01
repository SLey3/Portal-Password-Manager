# Imports
import sqlite3
import wx
import wx.html
from pubsub import pub
import appResources.resources.encryption.encryption as encryption
import appResources.resources.PWDgenerator.generator as generator
import json
import os
import configuration

###Portal Password Manager Application

## Variable Definitions

APP_EXIT = 1

JSON_FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\resource\\appResources\\docs\\json\\account.json'

SIGNED_IN = open('check.txt', 'r').read()

INITIAL_SETUP_COMPLETED = open('Initial.txt', 'r').read()

del_char = ["'"]


user_username = None

raw_user_password = None

## App frame
class loginLog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, title="Portal Password Manager", size=(850, 750))
        
        usr_sizer = wx.BoxSizer(wx.HORIZONTAL)
        usr_lbl = wx.StaticText(self, label="Username:")
        usr_sizer.Add(usr_lbl, 0, wx.ALL|wx.LEFT, 5)
        self.user = wx.TextCtrl(self)
        usr_sizer.Add(self.user, 0, wx.ALL, 5)
        
        pwd_sizer = wx.BoxSizer(wx.HORIZONTAL)
        pwd_lbl = wx.StaticText(self, label="Password:")
        pwd_sizer.Add(pwd_lbl, 0, wx.ALL|wx.LEFT, 5)
        self.pwd = wx.TextCtrl(self, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        pwd_sizer.Add(self.pwd, 0, wx.ALL, 5)
        #TODO Get logo image for bitmap
        frameSizer = wx.BoxSizer(wx.VERTICAL)
        frameSizer.Add(usr_sizer, 0, wx.ALL, 5)
        frameSizer.Add(pwd_sizer, 0, wx.ALL, 5)
        login_btn = wx.Button(self, label="Login")
        login_btn.Bind(wx.EVT_BUTTON, self.onLogin)
        frameSizer.Add(login_btn, 0, wx.ALL|wx.LEFT, 5)
        
        self.SetSizer(frameSizer)
        
    def onLogin(self, event):
        global user_username, raw_user_password
        #TODO  Create server for checking account values
        
        user_usr = self.user.GetValue()
        user_pwd = self.pwd.GetValue()
        
        try:
           with open(JSON_FILE_PATH) as f:
                account_JSON = json.load(f)
                if user_username is None and raw_user_password is None:
                    user_username = account_JSON['Account'][1]['Username']
                    raw_user_password = account_JSON['Account'][1]['Password']
        except json.decoder.JSONDecodeError:
            wx.MessageBox("No account created under that username or password.", 'Error', wx.OK|wx.ICON_ERROR)
        except UnboundLocalError:
            wx.MessageBox("No entry detected.", 'Error', wx.OK|wx.ICON_ERROR)
        raw_user_password = str(raw_user_password)
        for i in del_char:
            raw_user_password = raw_user_password.replace(i, '')
        raw_user_password = raw_user_password[1::]
        raw_user_password = raw_user_password.encode()
        user_password = encryption.de_encrypt(raw_user_password)
        if(user_pwd == user_password) and (user_usr == user_username):
            pub.sendMessage("frameListener", message="show")
            self.Destroy()
            SIGNED_IN = open('check.txt', 'w').write("True")
        else:
            wx.MessageBox("Username or Password incorrect", 'Warning', wx.OK|wx.ICON_WARNING)
    
class mainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

class mainFrame(wx.Frame):
    def __init__(self, parent, title, size, INITIAL_SETUP_COMPLETED):
        super(mainFrame, self).__init__(parent, title=title, size=size)
        panel = mainPanel(self)
        pub.subscribe(self.listener, "frameListener")
        if INITIAL_SETUP_COMPLETED == "False":
            configuration.main()
        elif SIGNED_IN == "False":
            dlg = loginLog()
            dlg.ShowModal()
            dlg.Centre()
        else:
            self.Show()
            self.menuFrame()
            self.InitUI()
            self.Centre()
        
    def listener(self, message, agr2=None):
        self.Show()    
        
    def InitUI(self):
        pass
    
    def menuFrame(self):
        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        quit = wx.MenuItem(filemenu, APP_EXIT, '&Quit\tCtrl+Q')
        #TODO Set bitmap for exit menu item
        filemenu.Append(quit)
        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)
        sign_out = wx.MenuItem(filemenu, APP_EXIT, '&Sign out')
        #TODO Set bitmap for sign out menu item
        filemenu.Append(sign_out)
        self.Bind(wx.EVT_MENU, self.signOut, id=APP_EXIT)
        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)
        
    def onQuit(self, e):
        self.Close()
        
    def signOut(self, s):
        SIGNED_IN = open('check.txt', 'w').write("False")
        self.Destroy()
        llg = loginLog()
        llg.ShowModal()
        llg.Centre()
        
def main():
    app = wx.App(False)
    frame = mainFrame(None, "Portal Password Manager", (850, 750), INITIAL_SETUP_COMPLETED)
    app.MainLoop()
    
if __name__ == '__main__':
    main()