# Imports
import wx
import json
import os
import re
import wx.html as html

# Variable Definitions
JSON_FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\resource\\appResources\\docs\\json\\accounts.json'

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]")

HTML_FILE_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\resource\\appResources\\docs\\html\\configuration.html'


# Setup for application
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
        
        cont_btn = wx.Button(panel, wx.ID_ANY, 'continue')
        self.Bind(wx.EVT_MENU, self.register, id=wx.ID_ANY)
        hbox.Add(cont_btn, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        vbox.Add(hbox, 0, wx.EXPAND)
        
        panel.SetSizer(vbox)
        self.SetTitle("Portal Password Manager Configuration")
        self.Centre()
        
    def register(self):
        pass
        
def main():
    app = wx.App()
    frame = configFrame(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()