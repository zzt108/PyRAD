import wx
class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.b_test = wx.Button(self.panel, wx.ID_ANY, "Testing", pos=(60,60))
        self.Bind(wx.EVT_BUTTON, self.on_test, self.b_test)     
        self.cb_test = wx.ComboBox(self.panel, wx.ID_ANY, \
            choices=["Thor","Odin","Loki","Frigg","Freyr"], \
            pos=(180,60), style=wx.CB_SORT)
        self.cb_test.SetSelection(0)    
        self.Bind(wx.EVT_COMBOBOX, self.on_select, self.cb_test)              
    def on_test(self, event):
        print("Button pressed")
        event.Skip()   
    def on_select(self, event):
        print(self.cb_test.GetValue()+" lives in Valhalla") 
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