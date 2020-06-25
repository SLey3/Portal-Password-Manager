"""
Menu items for application
"""
# Imports
import wx

class menuFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super(menuFrame, self).__init__(parent, title=title, size=size)
        
        self.Centre()
        

def main():
    app = wx.App()
    mnf = menuFrame(None, "Portal Password Manager", (850, 750))
    mnf.Show()
    app.MainLoop()
    
if __name__ == '__main__':
    main()