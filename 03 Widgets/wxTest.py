import wx
class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.Panel = wx.Panel(self, wx.ID_ANY)
        self.btnTest = wx.Button(self, wx.ID_ANY, label="Test", pos=(60,60))
        self.Bind(wx.EVT_BUTTON, self.OnClickTest, self.btnTest)
        self.btnState = wx.Button(self, wx.ID_ANY, label="Disable", pos=(60,20))
        self.Bind(wx.EVT_BUTTON, self.OnClickState, self.btnState)

    def OnClickTest(self, event): 
        print("Button pressed")
        event.Skip() # allow other subscribers to handle

    def OnClickState(self, event): 
        if self.btnState.GetLabel() == "Disable":
            self.btnState.SetLabel("Enable")
            self.btnTest.Disable()
        else:
            self.btnState.SetLabel("Disable")
            self.btnTest.Enable()
            
        event.Skip() # allow other subscribers to handle


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
