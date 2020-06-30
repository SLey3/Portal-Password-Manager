# Imports
import sqlite3
import wx
import wx.html
from pubsub import pub
import appResources.resources.encryption.encryption as encryption
import appResources.resources.PWDgenerator.generator as generator
import json
import os

###Portal Password Manager Application

## Variable Definitions

APP_EXIT = 1

JSON_FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\resource\\appResources\\docs\\json\\accounts.json'

del_char = ["'"]


user_username = None

raw_user_password = None

## App frame
class register(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, title="Register", size=(500,650))
        
        r_sizer = wx.BoxSizer(wx.HORIZONTAL)
        r_lbl = wx.StaticText(self, label="Register Account")
        r_sizer.Add(r_lbl, 0, wx.ALL|wx.TOP|wx.CENTER, 5)
        
        line_sizer = wx.BoxSizer(wx.HORIZONTAL)
        line = wx.StaticLine(self, 0, size=wx.DefaultSize, style=wx.LI_HORIZONTAL)
        line_sizer.Add(line, 0, wx.ALL|wx.CENTER, 5)
        
        f_sizer = wx.BoxSizer(wx.HORIZONTAL)
        f_lbl = wx.StaticText(self, label="First Name:")
        f_sizer.Add(f_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.f_ctrl = wx.TextCtrl(self)
        f_sizer.Add(self.f_ctrl, 0, wx.ALL, 5)
        
        l_sizer = wx.BoxSizer(wx.HORIZONTAL)
        l_lbl = wx.StaticText(self, label="Last Name:")
        l_sizer.Add(l_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.l_ctrl = wx.TextCtrl(self)
        l_sizer.Add(self.l_ctrl, 0, wx.ALL, 5)
        
        username_sizer = wx.BoxSizer(wx.HORIZONTAL)
        username_lbl = wx.StaticText(self, label="Username:")
        username_sizer.Add(username_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.username_ctrl = wx.TextCtrl(self)
        username_sizer.Add(self.username_ctrl, 0, wx.ALL, 5)
        
        password_sizer = wx.BoxSizer(wx.HORIZONTAL)
        password_lbl = wx.StaticText(self, label="Password:")
        password_sizer.Add(password_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.password_ctrl = wx.TextCtrl(self, style= wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        password_sizer.Add(self.password_ctrl, 0, wx.ALL, 5)
        
        register_btn = wx.Button(self, label="Register")
        register_btn.Bind(wx.EVT_BUTTON, self.dataRegister)
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(r_sizer, 0, wx.ALL, 5)
        mainSizer.Add(line_sizer, 0, wx.ALL, 5)
        mainSizer.Add(f_sizer, 0, wx.ALL, 5)
        mainSizer.Add(l_sizer, 0, wx.ALL, 5)
        mainSizer.Add(username_sizer, 0, wx.ALL, 5)
        mainSizer.Add(password_sizer, 0, wx.ALL, 5)
        mainSizer.Add(register_btn, 0, wx.ALL|wx.LEFT, 5)
        
        self.SetSizer(mainSizer)
    def dataRegister(self, data):
        first = self.f_ctrl.GetValue()
        last = self.l_ctrl.GetValue()
        username = self.username_ctrl.GetValue()
        raw_password = self.password_ctrl.GetValue()
        b_password = encryption.encrypt(raw_password)
        password = str(b_password)
        full_name = first + " " + last
        account_JSON = {
            "Account": [
                {
                    "first":first,
                    "last":last
                },
                {
                    "Username":username,
                    "Password":password
                }
            ],
            "Profile": [
                {
                    "Name":full_name,
                    "Age":0,
                    "Gender":"None",
                    "Company":"None"
                }
            ]
    }   
        with open(JSON_FILE_PATH, 'a') as j:
            try:
                json.dump(account_JSON, j, indent=2, separators=(',',':'))
                j.write(",\n") 
            except TypeError:
                pass
            self.Destroy()
        
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
        
        pwd_btn = wx.Button(self, label="Register")
        pwd_btn.Bind(wx.EVT_BUTTON, self.register)
        frameSizer.Add(pwd_btn, 0, wx.ALL|wx.LEFT, 5)
        
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
        else:
            wx.MessageBox("Username or Password incorrect", 'Warning', wx.OK|wx.ICON_WARNING)
            
    
    def register(self, event):
        #TODO Create server for registering account
        llg = register()
        llg.ShowModal()
        
    
class mainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

class mainFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super(mainFrame, self).__init__(parent, title=title, size=size)
        panel = mainPanel(self)
        pub.subscribe(self.listener, "frameListener")
        
        dlg = loginLog()
        dlg.ShowModal()
        
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
        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)
        
    def onQuit(self, e):
        self.Close()
        
def main():
    app = wx.App(False)
    frame = mainFrame(None, "Portal Password Manager", (850, 750))
    app.MainLoop()
    
if __name__ == '__main__':
    main()