# Imports
import wx
import wx.html
from pubsub import pub
import appResources.resources.encryption.encryption as encryption
import appResources.resources.PWDgenerator.generator as generator
import appResources.resources.SQL.SQLtools as SQLtools
import appResources.resources.setup.apptools as apptools
import jsonpickle
import os
import sys
from cryptography.fernet import InvalidToken
import configuration

###Portal Password Manager Application

## Variable Definitions

APP_EXIT = 1

JSON_FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\json\\account.json'

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
        register_btn = wx.Button(self, label="Register")
        register_btn.Bind(wx.EVT_BUTTON, self.onRegister)
        frameSizer.Add(register_btn, 0, wx.ALL|wx.LEFT, 5)
        
        self.SetSizer(frameSizer)
    def onRegister(self, event):
        rlg = configuration.register()   
        rlg.ShowModal()
    def onLogin(self, event):
        global user_username, raw_user_password
        
        user_usr = self.user.GetValue() 
        user_pwd = self.pwd.GetValue()
        try:
           with open(JSON_FILE_PATH) as f:
                account_JSON = jsonpickle.decode(f.read())
                if user_username is None and raw_user_password is None:
                    user_username = account_JSON[user_usr].username
                    raw_user_password = account_JSON[user_usr].password
                raw_user_password = str(raw_user_password)
                for i in del_char:
                    raw_user_password = raw_user_password.replace(i, '')
                raw_user_password = raw_user_password[1::]
                raw_user_password = raw_user_password.encode()
                user_password = encryption.de_encrypt(raw_user_password)
                if self.pwd.GetLineLength == 0:
                    wx.MessageBox("Password Field must not be blank!", 'Error', wx.OK|wx.ICON_ERROR)
                    self.pwd.SetBackgroundColour("red")
                    self.pwd.SetFocus()
                    self.pwd.Refresh()
                elif self.user.GetLineLength == 0:
                    wx.MessageBox("Username Field must not be blank!", 'Error', wx.OK|wx.ICON_ERROR)
                    self.user.SetBackgroundColour("red")
                    self.user.SetFocus()
                    self.user.Refresh()
                elif(user_pwd == user_password) and (user_usr == user_username):
                    self.Hide()
                    pub.sendMessage("frameListener", message="show")
                    SIGNED_IN = open('check.txt', 'w').write("True")
                else:
                    wx.MessageBox("Username or Password incorrect", 'Warning', wx.OK|wx.ICON_WARNING)  
        except (KeyError, InvalidToken) as e:
            wx.MessageBox("No entry detected.", 'Error', wx.OK|wx.ICON_ERROR)

class mainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

class register_website_account(wx.Frame):
    def __init__(self, parent, title, size):
        super(register_website_account, self).__init__(parent=parent, title=title, size=size)
        self.Centre()
        
        title_sizer = wx.BoxSizer(wx.HORIZONTAL)
        title = wx.StaticText(self, label="Add Account")
        title_sizer.Add(title, 0, wx.ALL|wx.LEFT|wx.TOP, 5)
        
        website_name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        website_name_lbl = wx.StaticText(self, label="Website Name:")
        website_name_sizer.Add(website_name_lbl, 0, wx.ALL|wx.LEFT, 5)
        self.website_name_ctrl = wx.TextCtrl(self)
        website_name_sizer.Add(self.website_name_ctrl, 0, wx.ALL, 5)
        
        website_url_sizer = wx.BoxSizer(wx.HORIZONTAL)
        website_url_lbl = wx.StaticText(self, label="Url:")
        website_url_sizer.Add(website_url_lbl, 0, wx.ALL|wx.LEFT, 5)
        self.website_url_ctrl = wx.TextCtrl(self)
        website_url_sizer.Add(self.website_url_ctrl, 0, wx.ALL, 5)
        
        username_sizer = wx.BoxSizer(wx.HORIZONTAL)
        username_lbl = wx.StaticText(self, label="Username:")
        username_sizer.Add(username_lbl, 0, wx.ALL|wx.LEFT, 5)
        self.username_ctrl = wx.TextCtrl(self)
        username_sizer.Add(self.username_ctrl, 0, wx.ALL, 5)
        
        password_sizer = wx.BoxSizer(wx.HORIZONTAL)
        password_lbl = wx.StaticText(self, label="Password:")
        password_sizer.Add(password_lbl, 0, wx.ALL|wx.LEFT, 5)
        self.password_ctrl = wx.TextCtrl(self, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        password_sizer.Add(self.password_ctrl, 0, wx.ALL, 5)
        
        main_frame_sizer = wx.BoxSizer(wx.VERTICAL)
        add_btn = wx.Button(self, label="Add Account")
        add_btn.Bind(wx.EVT_BUTTON, self.addAccount)
        main_frame_sizer.Add(add_btn, 0, wx.ALL|wx.LEFT, 5)
        main_frame_sizer.Add(title_sizer, 0, wx.ALL, 5)
        main_frame_sizer.Add(website_name_sizer, 0, wx.ALL, 5)
        main_frame_sizer.Add(website_url_sizer, 0, wx.ALL, 5)
        main_frame_sizer.Add(username_sizer, 0, wx.ALL, 5)
        main_frame_sizer.Add(password_sizer, 0, wx.ALL, 5)
        
        self.SetSizer(main_frame_sizer)
        self.Show()
    def addAccount(self, event):
        website_name = self.website_name_ctrl.GetValue()
        website_url = self.website_url_ctrl.GetValue()
        username = self.username_ctrl.GetValue()
        password = self.password_ctrl.GetValue()
        if len(website_name) == 0:
            wx.MessageBox("Website Field must not be blank!", 'Error', wx.OK|wx.ICON_ERROR)
            self.website_name_ctrl.SetBackgroundColour("red")
            self.website_name_ctrl.SetFocus()
            self.website_name_ctrl.Refresh()
            return False
        elif len(website_url) == 0:
            wx.MessageBox("Url field must not be blank!", 'Error', wx.OK|wx.ICON_ERROR)
            self.website_url_ctrl.SetBackgroundColour("red")
            self.website_url_ctrl.SetFocus()
            self.website_url_ctrl.Refresh()
            return False
        elif len(username) == 0:
            wx.MessageBox("Username field must not be blank!", 'Error', wx.OK|wx.ICON_ERROR)
            self.username_ctrl.SetBackgroundColour("red")
            self.username_ctrl.SetFocus()
            self.username_ctrl.Refresh()
            return False
        elif len(password) == 0:
            wx.MessageBox("Password Field must not be blank!", 'Error', wx.OK|wx.ICON_ERROR)
            self.password_ctrl.SetBackgroundColour("red")
            self.password_ctrl.SetFocus()
            self.password_ctrl.Refresh()
            return False
        else:
            self.website_name_ctrl.SetBackgroundColour(
                 wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
            self.website_url_ctrl.SetBackgroundColour(
                 wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
            self.username_ctrl.SetBackgroundColour(
                 wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
            self.password_ctrl.SetBackgroundColour(
                 wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
            self.website_name_ctrl.Refresh()
            self.website_url_ctrl.Refresh()
            self.username_ctrl.Refresh()
            self.password_ctrl.Refresh()
            wx.MessageBox("Do you want to add {}?".format(website_name), 'Warning', wx.YES_NO|wx.ICON_WARNING)
            if wx.YES:
                SQLtools.append(website_name, website_url, username, password)
                self.Close()
            return True
        
class mainFrame(wx.Frame):
    def __init__(self, parent, title, size, INITIAL_SETUP_COMPLETED):
        super(mainFrame, self).__init__(parent, title=title, size=size)
        self.panel = mainPanel(self)
        pub.subscribe(self.listener, "frameListener")
        if INITIAL_SETUP_COMPLETED == "False":
            configuration.main()
        elif SIGNED_IN == "False":
            dlg = loginLog()
            dlg.ShowModal()
            dlg.Centre()
        else:
            pub.sendMessage("frameListener", message="show")
            self.menuFrame()
            self.InitUI()
            self.Centre()
        
    def listener(self, message, arg2=None):
        self.Show()    
        
    def InitUI(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        lbl = wx.StaticText(self.panel, label="Testing phase 1.2.1")
        hbox.Add(lbl, 0, wx.ALL|wx.ALIGN_CENTER, 5)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        addAccount_btn = wx.Button(self.panel, label="Add Account")
        addAccount_btn.Bind(wx.EVT_BUTTON, self.appendAccount)
        vbox.Add(addAccount_btn, 0, wx.ALL|wx.LEFT, 5)
        vbox.Add(hbox, 0, wx.ALL, 5)
    
    def menuFrame(self):
        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        quit = wx.MenuItem(filemenu, APP_EXIT, '&Quit\tCtrl+Q')
        #TODO Set bitmap for exit menu item
        filemenu.Append(quit)
        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)
        sign_out = wx.MenuItem(filemenu, 0, '&Sign out\tCtrl+S')
        #TODO Set bitmap for sign out menu item
        filemenu.Append(sign_out)
        self.Bind(wx.EVT_MENU, self.signOut, sign_out)
        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar) 
        
    def onQuit(self, e):
        self.Close()
        self.Destroy()
        
    def signOut(self, s):
        SIGNED_IN = open('check.txt', 'w').write("False")
        user_username = None
        raw_user_password = None
        self.Hide()
        llg = loginLog()
        llg.ShowModal()
        llg.Centre()
    
    def appendAccount(self, a):
        rwa = register_website_account(wx.GetTopLevelParent(self), "Add Account", (650, 550))
        rwa.Centre()
        rwa.Show()
        
def main():
    app = wx.App(False)
    frame = mainFrame(None, "Portal Password Manager", (850, 750), INITIAL_SETUP_COMPLETED)
    app.MainLoop()
    
if __name__ == '__main__':
    main()
    sys.exit()
