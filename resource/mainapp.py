# Imports
import sqlite3
import wx
import appResources.resources.encryption.encryption as encryption
import appResources.resources.PWDgenerator.generator as generator
import login

###Portal Password Manager Application

## Variable Definitions

APP_EXIT = 1

## App frame

class mainFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super(mainFrame, self).__init__(parent, title=title, size=size)
        self.menuFrame()
        self.InitUI()
        self.Centre()
        
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
    app = wx.App()
    mf = mainFrame(None, "Portal Password Manager", (850, 750))
    mf.Show()
    app.MainLoop()
    
if __name__ == '__main__':
    main()