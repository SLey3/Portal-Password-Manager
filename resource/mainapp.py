# Imports
import sqlite3
import wx
import appResources.resources.encryption.encryption as encryption
import appResources.resources.PWDgenerator.generator as generator
import login
import menu
# App frame

class mainFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super(mainFrame, self).__init__(parent, title=title, size=size)
        
        self.InitUI()
        self.Centre()
        
        
    def InitUI(self):
        pass
def main():
    app = wx.App()
    mf = mainFrame(None, "Portal Password Manager", (850, 750))
    mf.Show()
    app.MainLoop()
    
if __name__ == '__main__':
    main()