# Imports
import sqlite3
import wx
import wx.html
from pubsub import pub
import appResources.resources.encryption.encryption as encryption
import appResources.resources.PWDgenerator.generator as generator


###Portal Password Manager Application

## Variable Definitions

APP_EXIT = 1

## App frame
class loginLog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, title="Portal Password Manager", size=(850, 750))
        
        usr_sizer = wx.BoxSizer(wx.HORIZONTAL)
        usr_lbl = wx.StaticText(self, label="Username:")
        usr_sizer.Add(usr_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        usr_sizer.Add(self.user, 0, wx.ALL, 5)
        
        pwd_sizer = wx.BoxSizer(wx.HORIZONTAL)
        pwd_lbl = wx.StaticText(self, label="Password:")
        pwd_sizer.Add(pwd_lbl, 0, wx.ALL|wx.CENTER, 5)
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
        #TODO  Create server for checking account values
        user_password = "admin"
        user_username = "ghub4127@gmail.com"
        user_usr = self.user.GetValue()
        user_pwd = self.pwd.GetValue()
        if(user_pwd == user_password) and (user_usr == user_username):
            pub.sendMessage("frameListener", message="show")
            self.Destroy()
        else:
            wx.MessageBox("Username or Password incorrect", 'Warning', wx.OK|wx.ICON_WARNING)
            
    
    def register(self, event):
        #TODO Create server for registering account
        pass
    
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