import wx
class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.b_test = wx.Button(self.panel, wx.ID_ANY, "Testing", pos=(60,60))
        self.Bind(wx.EVT_BUTTON, self.on_test, self.b_test)   
        self.tc_ctr = wx.TextCtrl(self.panel, wx.ID_ANY, "1", (60,100), (35,-1))
        hispin = self.tc_ctr.GetSize().height
        pospin = self.tc_ctr.GetSize().width + self.tc_ctr.GetPosition().x + 2
        self.sb_ctr = wx.SpinButton(self.panel, wx.ID_ANY, (pospin, 100),\
            (int(hispin*2/3),hispin), wx.SP_VERTICAL) 
        self.sb_ctr.SetRange(1, 100)
        self.sb_ctr.SetValue(1)
        self.Bind(wx.EVT_SPIN, self.on_spin, self.sb_ctr)                       
    def on_test(self, event):
        print("Button pressed")
        event.Skip() 
    def on_spin(self, event):
        self.tc_ctr.SetValue(str(event.GetPosition()))       
class myApp(wx.App):
    def OnInit(self):
        self.frame = myFrame(None, wx.ID_ANY, title="wxPython Test")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
if __name__ == '__main__':
    app = myApp(0)
    app.MainLoop()                