import wx
class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.Panel = wx.Panel(self, wx.ID_ANY)

class myApp(wx.App):
    def __init__(self, windowTitle):
        self._windowTitle = windowTitle
        super().__init__() 

    def OnInit(self):  # creates an instance of the frame class
        self._frame = myFrame(None, wx.ID_ANY, title=self._windowTitle)
        self.SetTopWindow(self._frame)
        self._frame.Show()
        return True

if __name__ == "__main__":
    app = myApp("wxPython Test")
    app.MainLoop()


