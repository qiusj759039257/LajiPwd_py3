# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Laji password holder", pos=wx.DefaultPosition,
                          size=wx.Size(640, 540), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.keyword = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.keyword.ShowSearchButton(True)
        self.keyword.ShowCancelButton(False)
        bSizer1.Add(self.keyword, 0, wx.EXPAND | wx.ALL, 5)

        self.list_data = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_dataViewListColumn5 = self.list_data.AppendTextColumn(u"ID", width=40)
        self.m_dataViewListColumn1 = self.list_data.AppendTextColumn(u"Title", width=150)
        self.m_dataViewListColumn2 = self.list_data.AppendTextColumn(u"Remark", width=200)
        self.m_dataViewListColumn6 = self.list_data.AppendTextColumn(u"Account", width=200)
        self.m_dataViewListColumn3 = self.list_data.AppendTextColumn(u"Create", width=130)
        self.m_dataViewListColumn4 = self.list_data.AppendTextColumn(u"Update", width=130)
        bSizer1.Add(self.list_data, 1, wx.ALL | wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Copy", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Modify", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"Type account", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button8, 0, wx.ALL, 5)

        self.m_button9 = wx.Button(self, wx.ID_ANY, u"Type password", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button9, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"New" + u"\t" + u"Ctrl+N", u"Add a new password",
                                       wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem3)

        self.m_menuItem4 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Copy" + u"\t" + u"Ctrl+C",
                                       u"Copy a password into clipboard", wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem4)

        self.m_menuItem5 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Modify" + u"\t" + u"Ctrl+E", u"Change a password",
                                       wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem5)

        self.m_menuItem6 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Delete" + u"\t" + u"Del", u"Delete a password",
                                       wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem6)

        self.m_menuItem9 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Type account" + u"\t" + u"Ctrl+A",
                                       u"Simulate keyboard typing", wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem9)

        self.m_menuItem10 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Type password" + u"\t" + u"Ctrl+P",
                                        u"Simulate keyboard typing", wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem10)

        self.m_menuItem1 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Change Master Key", u"Change Master Key",
                                       wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem1)

        self.m_menu1.AppendSeparator()

        self.m_menuItem2 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"Exit" + u"\t" + u"Ctrl+W", u"Exit", wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem2)

        self.m_menubar1.Append(self.m_menu1, u"Menu")

        self.SetMenuBar(self.m_menubar1)

        self.m_statusBar1 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.keyword.Bind(wx.EVT_TEXT, self.search)
        self.m_button1.Bind(wx.EVT_BUTTON, self.newPwd)
        self.m_button2.Bind(wx.EVT_BUTTON, self.copyPwd)
        self.m_button3.Bind(wx.EVT_BUTTON, self.updatePwd)
        self.m_button4.Bind(wx.EVT_BUTTON, self.deletePwd)
        self.m_button8.Bind(wx.EVT_BUTTON, self.typeAccount)
        self.m_button9.Bind(wx.EVT_BUTTON, self.typePwd)
        self.Bind(wx.EVT_MENU, self.newPwd, id=self.m_menuItem3.GetId())
        self.Bind(wx.EVT_MENU, self.copyPwd, id=self.m_menuItem4.GetId())
        self.Bind(wx.EVT_MENU, self.updatePwd, id=self.m_menuItem5.GetId())
        self.Bind(wx.EVT_MENU, self.deletePwd, id=self.m_menuItem6.GetId())
        self.Bind(wx.EVT_MENU, self.typeAccount, id=self.m_menuItem9.GetId())
        self.Bind(wx.EVT_MENU, self.typePwd, id=self.m_menuItem10.GetId())
        self.Bind(wx.EVT_MENU, self.changeMasterKey, id=self.m_menuItem1.GetId())
        self.Bind(wx.EVT_MENU, self.close, id=self.m_menuItem2.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def search(self, event):
        event.Skip()

    def newPwd(self, event):
        event.Skip()

    def copyPwd(self, event):
        event.Skip()

    def updatePwd(self, event):
        event.Skip()

    def deletePwd(self, event):
        event.Skip()

    def typeAccount(self, event):
        event.Skip()

    def typePwd(self, event):
        event.Skip()

    def changeMasterKey(self, event):
        event.Skip()

    def close(self, event):
        event.Skip()


###########################################################################
## Class NewPwdDialog
###########################################################################

class NewPwdDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"New password", pos=wx.DefaultPosition,
                           size=wx.Size(340, 470), style=wx.CAPTION | wx.CLOSE_BOX)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Basic"), wx.VERTICAL)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Title", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        fgSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.text_title = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.Size(230, -1), 0)
        fgSizer1.Add(self.text_title, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Remark", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        fgSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.text_remark = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(230, -1), 0)
        fgSizer1.Add(self.text_remark, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Account", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        fgSizer1.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.text_account = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(230, -1), 0)
        fgSizer1.Add(self.text_account, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        fgSizer1.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.text_pwd = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(230, -1), wx.TE_PASSWORD)
        fgSizer1.Add(self.text_pwd, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Confirm", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        fgSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.text_confirm = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(230, -1), wx.TE_PASSWORD)
        fgSizer1.Add(self.text_confirm, 0, wx.ALL, 5)

        sbSizer1.Add(fgSizer1, 1, wx.EXPAND, 5)

        bSizer3.Add(sbSizer1, 0, wx.EXPAND | wx.ALL, 5)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Generator"), wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.cb_num = wx.CheckBox(sbSizer2.GetStaticBox(), wx.ID_ANY, u"0-9", wx.DefaultPosition, wx.DefaultSize, 0)
        self.cb_num.SetValue(True)
        bSizer4.Add(self.cb_num, 0, wx.ALL, 5)

        self.cb_upper = wx.CheckBox(sbSizer2.GetStaticBox(), wx.ID_ANY, u"A-Z", wx.DefaultPosition, wx.DefaultSize, 0)
        self.cb_upper.SetValue(True)
        bSizer4.Add(self.cb_upper, 0, wx.ALL, 5)

        self.cb_lower = wx.CheckBox(sbSizer2.GetStaticBox(), wx.ID_ANY, u"a-z", wx.DefaultPosition, wx.DefaultSize, 0)
        self.cb_lower.SetValue(True)
        bSizer4.Add(self.cb_lower, 0, wx.ALL, 5)

        self.cb_special = wx.CheckBox(sbSizer2.GetStaticBox(), wx.ID_ANY, u"~!@#$%", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.cb_special.SetValue(True)
        bSizer4.Add(self.cb_special, 0, wx.ALL, 5)

        sbSizer2.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.digit = wx.Slider(sbSizer2.GetStaticBox(), wx.ID_ANY, 16, 1, 64, wx.DefaultPosition, wx.Size(200, -1),
                               wx.SL_HORIZONTAL | wx.SL_LABELS)
        bSizer6.Add(self.digit, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btn_generate = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Generate", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bSizer6.Add(self.btn_generate, 0, wx.ALL, 5)

        sbSizer2.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer3.Add(sbSizer2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_save = wx.Button(self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.btn_save, 0, wx.ALL, 5)

        self.btn_cancel = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.btn_cancel, 0, wx.ALL, 5)

        bSizer3.Add(bSizer5, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_generate.Bind(wx.EVT_BUTTON, self.generate)
        self.btn_save.Bind(wx.EVT_BUTTON, self.save)
        self.btn_cancel.Bind(wx.EVT_BUTTON, self.cancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def generate(self, event):
        event.Skip()

    def save(self, event):
        event.Skip()

    def cancel(self, event):
        event.Skip()


###########################################################################
## Class NewMasterPwdDialog
###########################################################################

class NewMasterPwdDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Master Key", pos=wx.DefaultPosition,
                           size=wx.Size(340, 175), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"New Key", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        fgSizer2.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.newKey = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, -1), wx.TE_PASSWORD)
        fgSizer2.Add(self.newKey, 0, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        fgSizer2.Add(self.m_staticText7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.confirmKey = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, -1),
                                      wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        fgSizer2.Add(self.confirmKey, 0, wx.ALL, 5)

        bSizer7.Add(fgSizer2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button10.SetDefault()
        bSizer8.Add(self.m_button10, 1, wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_button11, 1, wx.ALL, 5)

        bSizer7.Add(bSizer8, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.confirmKey.Bind(wx.EVT_TEXT_ENTER, self.confirm)
        self.m_button10.Bind(wx.EVT_BUTTON, self.confirm)
        self.m_button11.Bind(wx.EVT_BUTTON, self.cancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def confirm(self, event):
        event.Skip()

    def cancel(self, event):
        event.Skip()


###########################################################################
## Class CheckMasterPwdDialog
###########################################################################

class CheckMasterPwdDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Master Key", pos=wx.DefaultPosition,
                           size=wx.Size(340, 130), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Enter Master Key", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        fgSizer2.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.key = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1),
                               wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        fgSizer2.Add(self.key, 0, wx.ALL, 5)

        bSizer7.Add(fgSizer2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button10.SetDefault()
        bSizer8.Add(self.m_button10, 1, wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_button11, 1, wx.ALL, 5)

        bSizer7.Add(bSizer8, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.key.Bind(wx.EVT_TEXT_ENTER, self.confirm)
        self.m_button10.Bind(wx.EVT_BUTTON, self.confirm)
        self.m_button11.Bind(wx.EVT_BUTTON, self.cancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def confirm(self, event):
        event.Skip()

    def cancel(self, event):
        event.Skip()
