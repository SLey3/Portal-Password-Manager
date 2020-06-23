#Imports
import wx

# Login Code
class loginFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super(loginFrame, self).__init__(parent, title=title, size=size)
        
        self.InitUI()
        self.Centre()
        
    def InitUI(self):
        #TODO Create Full login if possible with mentor
        pass
     


def main():
    app = wx.App()
    lf = loginFrame(None, "Portal Password Manager", (850,750))
    lf.Show()
    app.MainLoop()
    
if __name__ == '__main__':
    main()