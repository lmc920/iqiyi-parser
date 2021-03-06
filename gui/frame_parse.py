# -*- coding: utf-8 -*-

import wx
from gui.listctrl import ListCtrl_Parser

class DialogParser(wx.Dialog):
    def __init__(self, parent, *args):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u'IQIYI视频解析器', pos=wx.DefaultPosition,
                           size=wx.Size(400, 400), style=wx.DEFAULT_DIALOG_STYLE)

        text_resolution = wx.StaticText(self, wx.ID_ANY, u"清晰度：", wx.DefaultPosition, wx.DefaultSize, 0)
        text_resolution.Wrap(-1)

        self.checkbox_100 = wx.CheckBox(self, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0)
        self.checkbox_200 = wx.CheckBox(self, wx.ID_ANY, u"200", wx.DefaultPosition, wx.DefaultSize, 0)
        self.checkbox_300 = wx.CheckBox(self, wx.ID_ANY, u"300", wx.DefaultPosition, wx.DefaultSize, 0)
        self.checkbox_400 = wx.CheckBox(self, wx.ID_ANY, u"400", wx.DefaultPosition, wx.DefaultSize, 0)
        self.checkbox_500 = wx.CheckBox(self, wx.ID_ANY, u"500", wx.DefaultPosition, wx.DefaultSize, 0)
        self.checkbox_600 = wx.CheckBox(self, wx.ID_ANY, u"600", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.checkbox_700 = wx.CheckBox(self, wx.ID_ANY, u"600", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.checkbox_800 = wx.CheckBox(self, wx.ID_ANY, u"600", wx.DefaultPosition, wx.DefaultSize, 0)

        # self.checkbox_100.SetValue(True)
        # self.checkbox_200.SetValue(True)
        # self.checkbox_300.SetValue(True)
        # self.checkbox_400.SetValue(True)
        # self.checkbox_500.SetValue(True)
        self.checkbox_600.SetValue(True)

        sizer_resolution = wx.BoxSizer(wx.HORIZONTAL)
        sizer_resolution.Add(text_resolution, 0, wx.ALL, 5)
        sizer_resolution.Add(self.checkbox_100, 0, wx.ALL, 5)
        sizer_resolution.Add(self.checkbox_200, 0, wx.ALL, 5)
        sizer_resolution.Add(self.checkbox_300, 0, wx.ALL, 5)
        sizer_resolution.Add(self.checkbox_400, 0, wx.ALL, 5)
        sizer_resolution.Add(self.checkbox_500, 0, wx.ALL, 5)
        sizer_resolution.Add(self.checkbox_600, 0, wx.ALL, 5)


        staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        staticline4 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        staticline3 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)

        text_url = wx.StaticText(self, wx.ID_ANY, u"Url", wx.DefaultPosition, wx.DefaultSize, 0)
        text_url.Wrap(-1)

        self.textctrl_url = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_parse = wx.Button(self, wx.ID_ANY, u"解析", wx.DefaultPosition, wx.DefaultSize, 0)

        sizer_url = wx.BoxSizer(wx.HORIZONTAL)
        sizer_url.Add(text_url, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_url.Add(self.textctrl_url, 5, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_url.Add(self.button_parse, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # =================================================================

        self.listctrl_parse = ListCtrl_Parser(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)

        sizer_listctrl = wx.BoxSizer(wx.VERTICAL)
        sizer_listctrl.Add(self.listctrl_parse, 0, wx.ALL | wx.EXPAND, 5)

        # =================================================================

        self.button_copyurl = wx.Button(self, wx.ID_ANY, u"复制下载链接", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_godownload = wx.Button(self, wx.ID_ANY, u"下载选中项", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.button_godownload.Enable(False)
        sizer_control = wx.BoxSizer(wx.HORIZONTAL)
        sizer_control.Add(self.button_copyurl, 0, wx.ALL, 5)
        sizer_control.Add(self.button_godownload, 1, wx.ALIGN_RIGHT | wx.ALL, 5)
        # =================================================================

        text_path = wx.StaticText(self, wx.ID_ANY, u"存放目录：", wx.DefaultPosition, wx.DefaultSize, 0)
        text_path.Wrap(-1)
        self.textctrl_path = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_path = wx.Button(self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size(50, -1), 0)

        sizer_path = wx.BoxSizer(wx.HORIZONTAL)
        sizer_path.Add(text_path, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_path.Add(self.textctrl_path, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_path.Add(self.button_path, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sizer_global = wx.BoxSizer(wx.VERTICAL)
        sizer_global.Add(sizer_resolution, 0, wx.EXPAND, 5)
        sizer_global.Add(staticline1, 0, wx.EXPAND | wx.ALL, 5)
        sizer_global.Add(sizer_url, 0, wx.EXPAND, 5)
        sizer_global.Add(staticline2, 0, wx.EXPAND | wx.ALL, 5)
        sizer_global.Add(sizer_listctrl, 1, wx.EXPAND, 5)
        sizer_global.Add(staticline3, 0, wx.EXPAND | wx.ALL, 5)
        sizer_global.Add(sizer_control, 0, wx.EXPAND, 5)
        sizer_global.Add(staticline4, 0, wx.EXPAND | wx.ALL, 5)
        sizer_global.Add(sizer_path, 0, wx.EXPAND, 5)

        self.SetSizer(sizer_global)
        self.Layout()

        self.Centre(wx.BOTH)

