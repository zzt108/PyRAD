import wx
class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.b_test = wx.Button(self.panel, wx.ID_ANY, "Testing", pos=(60,60))
        self.Bind(wx.EVT_BUTTON, self.on_test, self.b_test)
        self.rb_mercury = wx.RadioButton(self.panel, wx.ID_ANY, 'mercury',\
            pos=(66,100))
        self.rb_mars    = wx.RadioButton(self.panel, wx.ID_ANY, 'mars',\
            pos=(133,100))
        self.rb_earth = wx.RadioButton(self.panel, wx.ID_ANY, 'earth',\
            pos=(66,120))
    def on_test(self, event):
#        print("Button pressed")
        if self.rb_mercury.GetValue(): print("Mercury selected")
        if self.rb_mars.GetValue():    print("Mars selected")
        if self.rb_earth.GetValue():   print("Earth selected")
        event.Skip()    
class myApp(wx.App):
    def OnInit(self):
        self.frame = myFrame(None, wx.ID_ANY, title="wxPython Test")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
if __name__ == '__main__':
    app = myApp(0)
    app.MainLoop()                