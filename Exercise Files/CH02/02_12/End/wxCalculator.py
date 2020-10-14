import wx
class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.rb_op = wx.RadioBox(self.panel, wx.ID_ANY, "Operation", pos=(20,40),\
            choices=['+','-','*','/'])
        self.tc_val1 = wx.TextCtrl(self.panel, wx.ID_ANY, "", pos=(20,100),\
            size=(40,-1))
        wx.StaticText(self.panel, wx.ID_ANY, "op", pos=(65,100))
        self.tc_val2 = wx.TextCtrl(self.panel, wx.ID_ANY, "", pos=(85,100),\
            size=(40,-1))
        wx.StaticText(self.panel, wx.ID_ANY, "=", pos=(130,100))
        self.tc_val3 = wx.TextCtrl(self.panel, wx.ID_ANY, "", pos=(145,100),\
            size=(40,-1), style=wx.TE_READONLY)
        self.b_compute = wx.Button(self.panel, wx.ID_ANY, "Compute", pos=(20,135))
        self.Bind(wx.EVT_BUTTON, self.on_compute, self.b_compute)
        self.lb_audit = wx.ListBox(self.panel, wx.ID_ANY, choices=[],\
            pos=(210,20), size=(140,160))
    def on_compute(self, event):
        val1 = float(self.tc_val1.GetValue())
        val2 = float(self.tc_val2.GetValue())
        if self.rb_op.GetStringSelection()=="+":
            self.tc_val3.SetValue("{:.2f}".format(val1+val2))
        if self.rb_op.GetStringSelection()=="-":
            self.tc_val3.SetValue("{:.2f}".format(val1-val2))
        if self.rb_op.GetStringSelection()=="*":
            self.tc_val3.SetValue("{:.2f}".format(val1*val2))
        if self.rb_op.GetStringSelection()=="/":
            self.tc_val3.SetValue("{:.2f}".format(val1/val2))
        self.lb_audit.Append(self.tc_val1.GetValue()+\
            self.rb_op.GetStringSelection()+\
            self.tc_val2.GetValue()+"="+self.tc_val3.GetValue())    
        event.Skip()               
class myApp(wx.App):
    def OnInit(self):
        self.frame = myFrame(None, wx.ID_ANY, title="wxPython Calculator")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
if __name__ == '__main__':
    app = myApp(0)
    app.MainLoop()                