import wx
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.Panel = wx.Panel(self, wx.ID_ANY)
        self.btnTest = wx.Button(self.Panel, wx.ID_ANY, label="Test", pos=(60,70))
        self.Bind(wx.EVT_BUTTON, self.OnClickTest, self.btnTest)
        self.btnState = wx.Button(self.Panel, wx.ID_ANY, label="Disable", pos=(60,40))
        self.Bind(wx.EVT_BUTTON, self.OnClickState, self.btnState)

        self.chbDiscount = wx.CheckBox(self.Panel, wx.ID_ANY, "Apply Discount", pos=(60,10) )
        self.Bind(wx.EVT_CHECKBOX, self.OnClickDiscount, self.chbDiscount)

    def OnClickDiscount(self, event):
        print("CheckBox ", "checked" if self.chbDiscount.IsChecked() else "unchecked")

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


class MyApp(wx.App):
    def __init__(self, WindowTitle):
        self._windowTitle = WindowTitle
        super().__init__() 

    def OnInit(self):  # creates an instance of the frame class
        self._frame = MyFrame(None, wx.ID_ANY, title=self._windowTitle)
        self.SetTopWindow(self._frame)
        self._frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp("wxPython Test")
    app.MainLoop()
