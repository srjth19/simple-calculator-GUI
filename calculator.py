# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:08:47 2021

@author: Srijith
"""

import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        box = wx.BoxSizer(wx.VERTICAL)
        self.textbox = wx.TextCtrl(self, style = wx.TE_RIGHT, size = (2500, -1))
        box.Add(self.textbox, wx.EXPAND| wx.TOP| wx.BOTTOM, border = 4)
        
        grid = wx.GridSizer(5, 4, 10, 10)
        
        buttons = [
           '7', '8', '9', '/',
           '4', '5', '6', '*',
           '3', '2', '1', '-',
           '0', '.', 'C', '+',
           '='
           ]
       
        for label in buttons:
            button = wx.Button(self, -1, label)
            grid.Add(button, 0, wx.EXPAND)
            self.Bind(wx.EVT_BUTTON, self.button_press, button)
        
        box.Add(grid, proportion = 1, flag = wx.EXPAND)
        self.SetSizer(box)
        
    #function which performs the computation
    def button_press(self, lab):
        
        #get the button pressed
        label = lab.GetEventObject().GetLabel()
        
        #get the expression to compute
        computation = self.textbox.GetValue()
        
        #Event handling for the computation
        if label == '=':
            if not computation:
                return              #if blank expression do nothing
            
            #try block for exception handling due to possibility of incorrect UI usage
            try:
                result = eval(computation)
            except SyntaxError as error:
                wx.LogError('Invalid Syntax. Please check your input and try again.'.format(computation))
                return
            except NameError as error:
                wx.LogError('An error occured. Please check your input and try again.'.format(computation))
                return
            except ZeroDivisionError as error:
                wx.LogError('Cannot divide expression by zero. Please check your input and try again'.format(computation))
                return
            
            self.textbox.SetValue(str(result))
        
        elif label == 'C':
            self.textbox.SetValue('')       #clear values from the display
        else:
            self.textbox.SetValue(computation + label)      #add the button value to the expression
            
    
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size = (320,480))
        panel = MyPanel(self)
        self.Show()
        
if(__name__ == "__main__"):
    app = wx.App()
    MyFrame(None, title = "Calculator")
    app.MainLoop()