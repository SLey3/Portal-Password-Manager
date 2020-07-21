# Imports
import wx
import os
import sys
import re
import wx.html as html
import appResources.resources.encryption.encryption as encryption
from mainapp import INITIAL_SETUP_COMPLETED
import appResources.resources.setup.apptools as apptools
from time import sleep
import jsonpickle
from appResources.resources.setup.apptools import accountObject

# Variable Definitions
JSON_FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\json\\account.json'

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]")

HTML_FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\docs\\html\\configuration.html'

JSON_LINE_COUNT = apptools.jsonLineCount()

# Setup for application
class setup(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, title="Installing Database", size=(500,650))
        h_box = wx.BoxSizer(wx.HORIZONTAL)
        config_pending = wx.StaticText(self, label="Installing data.db file...")
        h_box.Add(config_pending, 0, wx.ALL|wx.ALIGN_CENTER, 5)
        sleep(1.0)
        apptools.generate_database()
        sleep(1.0)
        config_pending.Hide()
        config_complete = wx.StaticText(self, label='data.db file Installed. Press continue to continue.')
        h_box.Add(config_complete, 0, wx.ALL|wx.ALIGN_CENTER, 5)
        continue_btn = wx.Button(self, label="Continue")
        continue_btn.Bind(wx.EVT_BUTTON, self.cont)
        h_box.Add(continue_btn, 0, wx.ALL|wx.ALIGN_CENTER, 5)
        v_box = wx.BoxSizer(wx.VERTICAL)
        
        v_box.Add(h_box, 0, wx.ALL, 5)
        
        self.SetSizer(v_box)
    
    def cont(self, event):
        self.Destroy()
        rlg = register()
        rlg.ShowModal()
        
class register(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, title="Portal Password Manager Configuration | Register", size=(500,650))
        
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
        accounts = {}
        with open(JSON_FILE_PATH, 'r') as j:
            accounts = jsonpickle.decode(j.read())
        first = self.f_ctrl.GetValue()
        last = self.l_ctrl.GetValue()
        username = self.username_ctrl.GetValue()
        raw_password = self.password_ctrl.GetValue()
        b_password = encryption.encrypt(raw_password)
        password = str(b_password)
        full_name = first + " " + last
        if not EMAIL_REGEX.match(username):
            wx.MessageBox("Email Does not exist", 'Error', wx.OK|wx.ICON_ERROR)
            return

        with open(JSON_FILE_PATH, 'a') as j:
            tempAccount = accountObject(first, last, full_name, username, password)
            accounts[username]=tempAccount
            with open(JSON_FILE_PATH, 'w') as savefile:
                savefile.write(jsonpickle.encode(accounts, indent=4))
            
            sleep(0.5)
            if INITIAL_SETUP_COMPLETED == "True":
                 wx.MessageBox("Registration Complete.", 'Info', wx.OK|wx.ICON_INFORMATION)
            else:
                wx.MessageBox("Registration Complete. Terminating configuration app.", 'Info', wx.OK|wx.ICON_INFORMATION)
                self.Close()
            
        
class configFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(configFrame, self).__init__(*args, **kwargs)
        
        self.htmlScreen()
        
    def htmlScreen(self):
        panel = wx.Panel(self)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        htmlwin = html.HtmlWindow(panel, wx.ID_ANY, style=wx.NO_BORDER)
        htmlwin.LoadPage(HTML_FILE_PATH)
        
        vbox.Add((-1, 10), 0)
        vbox.Add(htmlwin, 1, wx.EXPAND | wx.ALL, 9)
        
        cont_btn = wx.Button(panel, label='continue')
        cont_btn.Bind(wx.EVT_BUTTON, self.configuration, id=wx.ID_ANY)
        hbox.Add(cont_btn, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        vbox.Add(hbox, 0, wx.EXPAND)
        
        panel.SetSizer(vbox)
        self.SetTitle("Portal Password Manager Configuration")
        self.Centre()
        
    def configuration(self, event):
        self.Close()
        s = setup()
        s.Show()
        INITIAL_SETUP_COMPLETED = open('Initial.txt', 'w').write("True")
        
def main():
    app = wx.App()
    frame = configFrame(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
    sys.exit()
