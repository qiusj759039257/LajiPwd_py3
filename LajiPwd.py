import os
import sqlite3
import threading
import time
import base64
import sys


import wx
import wx.adv

import Frames
from KeyboardInput import *
from PasswordGenerator import *
from Cipher import *

MAGIC_CODE = 'LajiPwd'
TABLE_DDL = """
CREATE TABLE `password` (
    `id`        INTEGER      PRIMARY KEY AUTOINCREMENT,
    `title`     VARCHAR(255) NOT NULL,
    `remark`    VARCHAR(255) NOT NULL,
    `account`   VARCHAR(255) NOT NULL,
    `password`  VARCHAR(255) NOT NULL,
    `create`    DATETIME     NOT NULL DEFAULT 0,
    `update`    DATETIME     NOT NULL DEFAULT 0,
    `delete`    DATETIME     NOT NULL DEFAULT 0
);"""


class PasswordHolder:
    def __init__(self):
        self.conn = None
        self.key = None
        self.keySalt = None

    def connect(self, init=False):
        self.conn = sqlite3.connect("password.db")
        if init:
            self.initDB()

    def initDB(self):
        self.conn.execute(TABLE_DDL)
        pwd = self.encrypt(MAGIC_CODE)
        self.conn.execute("INSERT INTO `password` "
                          "(`id`, `title`, `remark`, `account`, `password`, `create`, `update`, `delete`)"
                          "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                          (0, 'MAGIC_CODE', 'Magic Code', MAGIC_CODE, pwd, 0, 0, -1))
        self.conn.commit()

    def validateKey(self):
        row = self.getById(0)
        return row[3] == row[4] and row[4] == MAGIC_CODE

    def reKey(self, key):
        everything = self.conn.execute("SELECT * FROM `password`").fetchall()
        everything = [list(row)[0:5] for row in everything]
        for row in everything:
            row[4] = self.decrypt(row[4])
        self.setKey(key)
        for row in everything:
            self.update(row)
        self.reSaltKey()

    def keyXor(self, key: bytes, salt: bytes):
        return bytes([key ^ salt for key, salt in zip(key, salt)])

    def reSaltKey(self):
        self.setKey(self.getKey())

    def setKey(self, key):
        self.keySalt = os.urandom(len(key))
        self.key = self.keyXor(key, self.keySalt)

    def getKey(self):
        return self.keyXor(self.key, self.keySalt)

    def clearKey(self):
        self.key = None
        self.keySalt = None

    def setSalt(self, data):
        salt = 'Salt_'.encode('ascii') + os.urandom(5) + data.encode('ascii')
        return salt

    def stripSalt(self, data):
        return data[10:]

    def encrypt(self, data):
        data = self.setSalt(data)
        data = Cipher.encrypt(data, self.getKey(), os.urandom(16))
        data = base64.b64encode(data)
        self.reSaltKey()
        return data

    def decrypt(self, data):
        data = base64.b64decode(data)
        data = Cipher.decrypt(data, self.getKey())
        data = self.stripSalt(data)
        data = str(data, 'ansi')
        self.reSaltKey()
        return data

    def delete(self, id):
        curs = self.conn.cursor()
        curs.execute("UPDATE `password` SET `delete` = ? WHERE `id` = ?", (time.strftime("%Y-%m-%d %H:%M:%S"), id))
        self.conn.commit()

    def insert(self, data):
        data = list(data)

        data[3] = self.encrypt(data[3])

        data.append(time.strftime("%Y-%m-%d %H:%M:%S"))
        data.append(time.strftime("%Y-%m-%d %H:%M:%S"))
        curs = self.conn.cursor()
        curs.execute("INSERT INTO `password` (`title`, `remark`, `account`, `password`, `create`, `update`)"
                     "VALUES (?, ?, ?, ?, ?, ?)", data)
        self.conn.commit()

    def update(self, data):
        data = list(data)
        data.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        id = data[0]
        del data[0]
        data.append(id)

        data[3] = self.encrypt(data[3])

        curs = self.conn.cursor()
        curs.execute("UPDATE `password` SET `title` = ?, `remark` = ?, `account` = ?, `password` = ?, `update` = ?"
                     "WHERE `id` = ?", data)
        self.conn.commit()

    def getById(self, id):
        curs = self.conn.cursor()
        curs.execute("SELECT * FROM `password` WHERE `id` = ?", (id,))
        result = list(curs.fetchone())
        result[4] = self.decrypt(result[4])
        self.reSaltKey()
        return result

    def getAll(self):
        curs = self.conn.cursor()
        curs.execute("SELECT * FROM `password` WHERE `delete` = 0")
        return curs.fetchall()

    def getByKeyword(self, keyword):
        curs = self.conn.cursor()
        curs.execute("SELECT * FROM `password` WHERE `title` LIKE ? AND `delete` = 0", ("%%%s%%" % keyword,))
        return curs.fetchall()


class TaskBarIcon(wx.adv.TaskBarIcon):
    ID_Show = wx.NewId()
    ID_Close = wx.NewId()

    def __init__(self, frame):
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO))

        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.doubleClick)
        self.Bind(wx.EVT_MENU, self.doubleClick, id=self.ID_Show)
        self.Bind(wx.EVT_MENU, self.close, id=self.ID_Close)

    def doubleClick(self, event):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.ShowWithAuth()
        self.frame.Raise()

    def close(self, event):
        self.Destroy()
        self.frame.Destroy()

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_Show, 'Show')
        menu.Append(self.ID_Close, 'Exit')
        return menu


class NewMasterPwdDialog(Frames.NewMasterPwdDialog):
    def __init__(self, parent):
        Frames.NewMasterPwdDialog.__init__(self, parent)
        self.parent = parent
        self.key = None

    def confirm(self, event):
        pwd_1 = self.newKey.Value
        pwd_2 = self.confirmKey.Value
        if pwd_1 != pwd_2:
            wx.MessageBox('Master Key not match')
        else:
            self.key = pwd_2
            self.Close()

    def cancel(self, event):
        self.Destroy()


class CheckMasterPwdDialog(Frames.CheckMasterPwdDialog):
    def __init__(self, parent):
        Frames.CheckMasterPwdDialog.__init__(self, parent)
        self.parent = parent

    def confirm(self, event):
        key = self.key.Value
        self.parent.holder.setKey(bytes(key, 'ansi'))
        self.Destroy()

    def cancel(self, event):
        self.Destroy()


class MainFrame(Frames.MainFrame):
    def __init__(self):
        Frames.MainFrame.__init__(self, None)
        self.Bind(wx.EVT_ICONIZE, self.iconize)
        self.Bind(wx.EVT_CLOSE, self.close)
        self.taskbar_icon = TaskBarIcon(self)
        self.SetIcon(wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO))
        self.data = None
        self.holder = PasswordHolder()
        flag = False
        if not os.path.exists('password.db'):
            flag = True
            dialog = NewMasterPwdDialog(self)
            dialog.ShowModal()
            if dialog.key is None:
                wx.MessageBox('Empty Master Key')
                sys.exit()
            else:
                self.holder.setKey(bytes(dialog.key, 'ansi'))
                dialog.Destroy()

        self.holder.connect(flag)
        self.load()

    def ShowWithAuth(self):
        check_dialog = CheckMasterPwdDialog(self)
        check_dialog.ShowModal()
        if self.holder.key:
            result = self.holder.validateKey()
            if result is not False:
                self.Show()
            else:
                wx.MessageBox('Master Key invalid')

    def changeMasterKey(self, event):
        dialog = NewMasterPwdDialog(self)
        dialog.ShowModal()
        key = dialog.key
        if key:
            self.holder.reKey(key)
        dialog.Destroy()
        del key
        self.load()

    def close(self, event):
        self.taskbar_icon.Destroy()
        self.Destroy()

    def iconize(self, event):
        self.holder.clearKey()
        self.Iconize(True)
        self.Hide()

    def search(self, event):
        self.load()

    def load(self):
        keyword = self.keyword.Value
        if keyword == "":
            self.data = self.holder.getAll()
        else:
            self.data = self.holder.getByKeyword(keyword)
        self.list_data.DeleteAllItems()
        for i in self.data:
            d = list(i)
            del d[4]
            self.list_data.AppendItem(d)

    def newPwd(self, event):
        new_dialog = NewPwdDialog(self)
        new_dialog.ShowModal()

    def copyPwd(self, event):
        row = self.list_data.GetSelectedRow()
        pwd = self.holder.decrypt(self.data[row][4])
        set_clipboard(pwd)
        t = threading.Thread(target=self.setStatusText, args=('Copied',))
        t.start()

    def updatePwd(self, event):
        row = self.list_data.GetSelectedRow()
        id = self.data[row][0]
        holder = self.holder
        data = holder.getById(id)
        dialog = NewPwdDialog(self)
        dialog.text_title.Value = data[1]
        dialog.text_remark.Value = data[2]
        dialog.text_account.Value = data[3]
        dialog.text_pwd.Value = dialog.text_confirm.Value = data[4]
        dialog.id = id
        dialog.ShowModal()

    def deletePwd(self, event):
        row = self.list_data.GetSelectedRow()
        id = self.data[row][0]
        if wx.YES is wx.MessageBox("Delete id = %d" % id, "Confirm", wx.YES_NO):
            holder = self.holder
            holder.delete(id)
            self.load()

    def typeAccount(self, event):
        row = self.list_data.GetSelectedRow()
        account = self.data[row][3]
        t = threading.Thread(target=MainFrame.delayType, args=(account,))
        t.start()

    def typePwd(self, event):
        row = self.list_data.GetSelectedRow()
        pwd = self.data[row][4]
        pwd = self.holder.decrypt(pwd)
        t = threading.Thread(target=MainFrame.delayType, args=(pwd,))
        t.start()

    @staticmethod
    def delayType(text,):
        if not KeyboardInput.lock:
            KeyboardInput.lock = True
            time.sleep(3)
            KeyboardInput.kb_input(text)
            KeyboardInput.lock = False

    def setStatusText(self, text):
        self.m_statusBar1.SetStatusText(text)
        time.sleep(5)
        self.m_statusBar1.SetStatusText('')


class NewPwdDialog(Frames.NewPwdDialog):
    def __init__(self, parent):
        Frames.NewPwdDialog.__init__(self, parent)
        self.parent = parent
        self.id = None

    def generate(self, event):
        digit = self.digit.Value
        flag = 0
        if self.cb_num.Value is True:
            flag |= PasswordGenerator.NUMERIC

        if self.cb_upper.Value is True:
            flag |= PasswordGenerator.ALPHABET_UPPER

        if self.cb_lower.Value is True:
            flag |= PasswordGenerator.ALPHABET_LOWER

        if self.cb_special.Value is True:
            flag |= PasswordGenerator.SPECIAL_CHAR

        if flag == 0:
            self.text_pwd.Value = self.text_confirm.Value = ""

        generator = PasswordGenerator(flag)

        self.text_pwd.Value = self.text_confirm.Value = generator.generate(digit)
        set_clipboard(self.text_pwd.Value)

    def save(self, event):
        title = self.text_title.Value
        remark = self.text_remark.Value
        account = self.text_account.Value
        pwd = self.text_pwd.Value
        cpwd = self.text_confirm.Value

        if title == "":
            wx.MessageBox("Title empty")
            return

        if account == "":
            wx.MessageBox("Account empty")
            return

        if pwd == "" or cpwd == "":
            wx.MessageBox("Password empty")
            return

        if pwd != cpwd:
            wx.MessageBox("Password not match")
            return
        set_clipboard(pwd)

        holder = self.parent.holder

        if self.id is None:
            holder.insert((title, remark, account, pwd))
        else:
            holder.update((self.id, title, remark, account, pwd))
        self.Close()
        self.Parent.load()

    def cancel(self, event):
        self.Close()


def set_clipboard(text):
    if wx.TheClipboard.Open():
        obj = wx.TextDataObject(text)
        wx.TheClipboard.SetData(obj)


if __name__ == "__main__":
    # os.path.exists('password.db') and os.unlink('password.db')
    app = wx.App()
    frame = MainFrame()
    frame.ShowWithAuth()
    app.MainLoop()
