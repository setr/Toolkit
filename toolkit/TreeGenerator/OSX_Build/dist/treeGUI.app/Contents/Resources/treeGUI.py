#!/usr/bin/env python2.7
import wx
import os
from textParser import TextParser

class MainWindow(wx.Frame):
    """ Our GUI menu """
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.parser = TextParser()
        self.createControls()
        self.bindEvents()
        self.doLayout()

    def createControls(self):
        self.inputText = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_DONTWRAP)
        self.outputText = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_DONTWRAP)
        font1 = wx.Font(11, wx.TELETYPE, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.outputText.SetFont(font1)

        self.convertButton = wx.Button(self, label="Convert!")
        self.openFileButton = wx.Button(self, label="Open File")
        self.headerText = wx.TextCtrl(self)

    def bindEvents(self):
        # what in the fuck is \
        for control, event, handler in \
            [(self.convertButton, wx.EVT_BUTTON, self.onConvert),
             (self.inputText, wx.EVT_TEXT, self.onInputChange),
             (self.outputText, wx.EVT_TEXT, self.onOutputChange),
             (self.openFileButton, wx.EVT_BUTTON, self.onOpen),
             (self.headerText, wx.EVT_TEXT, self.onHeaderChange)]:
            control.Bind(event, handler)

    def doLayout(self):
        boxSizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        gridSizer = wx.FlexGridSizer(cols=2, vgap=10, hgap=10)
        gridSizer.AddGrowableCol(0,1)
        gridSizer.AddGrowableCol(1,1)
        gridSizer.AddGrowableRow(0,4)
        gridSizer.AddGrowableRow(1,1)

        txtboxOptions=dict(flag=wx.EXPAND, proportion=22)
        buttonOptions = dict(flag=wx.ALIGN_CENTER)
        emptySpace = ((0, 0), dict())

        for control, options in \
                            [(self.inputText, txtboxOptions),
                             (self.outputText, txtboxOptions),
                             (self.openFileButton, buttonOptions),
                             (self.headerText, buttonOptions)]:
            gridSizer.Add(control, **options)

        for control, options in \
                [(gridSizer, dict(border=5, flag=wx.ALL|wx.EXPAND, proportion=1))]:
            boxSizer.Add(control, **options)

        self.SetSizerAndFit(boxSizer)

    def onOpen(self, event):
        """ Open a file, paste content to inputText"""
        dirname = ""
        OpenFileDialog = wx.FileDialog(self, "Open XYZ file", dirname, "", "*.*", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if OpenFileDialog.ShowModal() == wx.ID_CANCEL:
            return     # the user changed his mind ...

        input_stream = OpenFileDialog.GetPath()
        try:
            with open(input_stream, 'r') as f:
                self.inputText.SetValue(f.read())
        except IOError:
            errorDLG = wx.MessageDialog(self, "Could not open file. Are you sure the file path was correct?", "I/O ERROR", wx.ICON_ERROR)
            errorDLG.ShowModal()
            errorDLG.Destroy()
        except UnicodeDecodeError:
            errorDLG = wx.MessageDialog(self, "Could not understand the file. Are you sure this is a text file?", "READ ERROR", wx.ICON_ERROR)
            errorDLG.ShowModal()
            errorDLG.Destroy()

    def onHeaderChange(self, event):
        print "HEPLP"
        newHeader = self.headerText.GetValue().strip()
        print newHeader
        if newHeader is not None and newHeader != "":
            self.parser.HEADER = newHeader
        else:
            self.parser.HEADER = "*"
        self.onInputChange(event)

    def onConvert(self, event):
        raise NotImplementedError

    def onInputChange(self, event):
        text = self.inputText.GetValue()
        root = self.parser.startParse(False, text)
        out = root.printAll()
        out.encode("UTF-8")
        self.outputText.SetValue(out)

        # Auto-copys output to clipboard
        clipdata = wx.TextDataObject()
        clipdata.SetText(out)
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()

    def onOutputChange(self, event):
        pass


if __name__ == '__main__':
    app = wx.App(0)
    frame = MainWindow(None, title='Demo with Notebook')
    frame.Show()
    app.MainLoop()

